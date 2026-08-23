import time

# 1. Define a basic backend class so ComfyUI knows the node exists
class SimpleTimerNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # You can add inputs here later if needed
            },
        }

    # What the node outputs (e.g., a time value)
    RETURN_TYPES = ("FLOAT", "STRING")
    RETURN_NAMES = ("time_float", "time_string")
    
    FUNCTION = "get_time"
    
    # This determines where it appears in the right-click menu
    CATEGORY = "utils"

    def get_time(self):
        # A basic backend execution: returns the current time
        current_time = time.time()
        return (current_time, str(current_time))

# 2. Map the class so ComfyUI populates it in the menu
NODE_CLASS_MAPPINGS = {
    "SimpleTimer": SimpleTimerNode
}

# 3. Give it a readable, human-friendly name in the UI
NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleTimer": "Simple Timer"
}

# 4. Keep your frontend JS directory linked
WEB_DIRECTORY = "./js"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']