import { app } from "../../scripts/app.js";
import { api } from "../../scripts/api.js";

let startTime = 0;

app.registerExtension({
    name: "Custom.GlobalTimer",
    setup() {
        // Create the UI element
        const timerDisplay = document.createElement("div");
        timerDisplay.style.padding = "8px 12px";
        timerDisplay.style.backgroundColor = "rgba(0, 0, 0, 0.8)";
        timerDisplay.style.color = "#0f0";
        timerDisplay.style.textAlign = "center";
        timerDisplay.style.borderRadius = "4px";
        timerDisplay.style.fontFamily = "monospace";
        timerDisplay.style.fontSize = "14px";
        timerDisplay.style.zIndex = "9999"; // Ensure it sits above other UI elements
        timerDisplay.innerText = "Ready: 0.00s";
        
        // Try to find the old menu first
        const oldMenu = document.querySelector(".comfy-menu");
        
        if (oldMenu) {
            // If on the old UI, attach it there
            timerDisplay.style.margin = "4px 0";
            oldMenu.prepend(timerDisplay);
        } else {
            // If on the NEW UI (v1), make it a floating widget at the bottom right
            timerDisplay.style.position = "fixed";
            timerDisplay.style.bottom = "20px";
            timerDisplay.style.right = "20px";
            timerDisplay.style.border = "1px solid #333";
            document.body.appendChild(timerDisplay);
        }

        // Listen for when the queue starts
        api.addEventListener("execution_start", () => {
            startTime = performance.now();
            timerDisplay.innerText = "Generating...";
            timerDisplay.style.color = "#ffaa00";
        });

        // Listen for node execution updates
        api.addEventListener("executing", (event) => {
            // When event.detail is null, the entire prompt has finished executing
            if (!event.detail) {
                const endTime = performance.now();
                const elapsed = ((endTime - startTime) / 1000).toFixed(2);
                timerDisplay.innerText = `Done: ${elapsed}s`;
                timerDisplay.style.color = "#0f0";
            }
        });
    }
});