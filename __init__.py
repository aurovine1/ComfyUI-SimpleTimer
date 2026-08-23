import time

# 1. Define a basic backend class so ComfyUI knows the node exists
import time

class SimpleTimerNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # Forces the timer to wait for the sampler to finish
                "latent_in": ("LATENT",), 
            },
        }

    # Added LATENT to the outputs so it can act as a bridge
    RETURN_TYPES = ("LATENT", "FLOAT", "STRING")
    RETURN_NAMES = ("latent_passthrough", "time_float", "time_string")
    
    FUNCTION = "get_time"
    CATEGORY = "utils"

    def get_time(self, latent_in):
        # 1. Grab the exact time the latent arrived
        current_time = time.time()
        
        # 2. Pass the latent through untouched, along with the timestamps
        return (latent_in, current_time, str(current_time))


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