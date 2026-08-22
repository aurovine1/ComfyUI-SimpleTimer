import { app } from "../../scripts/app.js";
import { api } from "../../scripts/api.js";

let startTime = 0;

app.registerExtension({
    name: "Custom.GlobalTimer",
    setup() {
        // Create the UI element
        const timerDisplay = document.createElement("div");
        timerDisplay.style.padding = "8px";
        timerDisplay.style.margin = "4px 0";
        timerDisplay.style.backgroundColor = "#222";
        timerDisplay.style.color = "#0f0";
        timerDisplay.style.textAlign = "center";
        timerDisplay.style.borderRadius = "4px";
        timerDisplay.style.fontFamily = "monospace";
        timerDisplay.innerText = "Ready: 0.00s";
        
        // Append it to the main ComfyUI menu panel
        const menu = document.querySelector(".comfy-menu");
        if (menu) {
            menu.prepend(timerDisplay);
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