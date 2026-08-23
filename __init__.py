import time

class SimpleTimerNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent_in": ("LATENT",), 
            },
        }

    RETURN_TYPES = ("LATENT", "FLOAT", "STRING")
    RETURN_NAMES = ("latent_passthrough", "time_float", "time_string")
    
    FUNCTION = "get_time"
    CATEGORY = "utils"

    def get_time(self, latent_in):
        current_time = time.time()
        
        # Formats the raw timestamp into a clean local clock time (e.g., 18:42:15)
        formatted_time = time.strftime("%H:%M:%S", time.localtime(current_time))
        
        return (latent_in, current_time, formatted_time)

NODE_CLASS_MAPPINGS = {
    "SimpleTimer": SimpleTimerNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleTimer": "Simple Timer"
}

WEB_DIRECTORY = "./js"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']

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