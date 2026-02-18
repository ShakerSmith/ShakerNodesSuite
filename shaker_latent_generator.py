import torch
import random
import time

class LatentGenerator:
    RESOLUTIONS = {
        "Large": {
            "Square (1:1)": (1360, 1360),
            "Portrait (2:3)": (1104, 1656),
            "Wide (3:2)": (1656, 1104),
            "Cinema (16:9)": (1792, 1024),
            "Ultrawide (2.39:1)": (2048, 856)
        },
        "Medium": {
            "Square (1:1)": (1024, 1024),
            "Portrait (2:3)": (832, 1248),
            "Wide (3:2)": (1248, 832),
            "Cinema (16:9)": (1344, 768),
            "Ultrawide (2.39:1)": (1536, 640)
        },
        "Small": {
            "Square (1:1)": (512, 512),
            "Portrait (2:3)": (416, 624),
            "Wide (3:2)": (640, 360),
            "Cinema (16:9)": (640, 360),
            "Ultrawide (2.39:1)": (768, 320)
        }
    }

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "random_mode": (["manual", "random all", "random select", "custom"], {"default": "manual"}),
                "size_model": (["Large (Z-Image)", "Medium (SDXL)", "Small (SD1.5)"], {"default": "Medium (SDXL)"}),
                "sq_1_1": ("BOOLEAN", {"default": True, "label_on": "Square (1:1)", "label_off": "Square (1:1)"}),
                "por_2_3": ("BOOLEAN", {"default": False, "label_on": "Portrait (2:3)", "label_off": "Portrait (2:3)"}),
                "wide_3_2": ("BOOLEAN", {"default": False, "label_on": "Wide (3:2)", "label_off": "Wide (3:2)"}),
                "cin_16_9": ("BOOLEAN", {"default": False, "label_on": "Cinema (16:9)", "label_off": "Cinema (16:9)"}),
                "ult_2_39": ("BOOLEAN", {"default": False, "label_on": "Ultrawide (2.39:1)", "label_off": "Ultrawide (2.39:1)"}),
                "custom_width": ("INT", {"default": 1024, "min": 64, "max": 8192}),
                "custom_height": ("INT", {"default": 1024, "min": 64, "max": 8192}),
                "multiplier": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 4.0, "step": 0.1}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 64}),
            },
            "optional": {
                "testing_override": ("BOOLEAN", {"default": False, "label_on": "64px (TEST)", "label_off": "Full Size"}),
            }
        }

    RETURN_TYPES = ("LATENT", "INT", "INT")
    RETURN_NAMES = ("latent", "width", "height")
    FUNCTION = "generate"
    CATEGORY = "ShakerNodes"

    @classmethod
    def IS_CHANGED(s, random_mode, **kwargs):
        if "random" in random_mode:
            return float("nan")
        return time.time()

    def generate(self, random_mode, size_model, sq_1_1, por_2_3, wide_3_2, cin_16_9, ult_2_39, 
                 custom_width, custom_height, multiplier, batch_size, testing_override=False):
        
        applied_label = ""
        width, height = 1024, 1024
        size_key = "Large" if "Large" in size_model else "Medium" if "Medium" in size_model else "Small"

        if random_mode == "custom":
            width = int(custom_width * multiplier)
            height = int(custom_height * multiplier)
            applied_label = "Custom"
        else:
            mapping = {
                "Square (1:1)": sq_1_1,
                "Portrait (2:3)": por_2_3,
                "Wide (3:2)": wide_3_2,
                "Cinema (16:9)": cin_16_9,
                "Ultrawide (2.39:1)": ult_2_39
            }
            selected_ratios = [k for k, v in mapping.items() if v]

            if random_mode == "random all":
                active_ratio = random.choice(list(self.RESOLUTIONS[size_key].keys()))
            elif random_mode == "random select" and selected_ratios:
                active_ratio = random.choice(selected_ratios)
            else:
                active_ratio = selected_ratios[0] if selected_ratios else "Square (1:1)"
            
            base_w, base_h = self.RESOLUTIONS[size_key][active_ratio]
            width = int(base_w * multiplier)
            height = int(base_h * multiplier)
            applied_label = active_ratio

        if testing_override:
            width, height = 64, 64
            applied_label = "Testing"

        width = (width // 8) * 8
        height = (height // 8) * 8
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        
        return {
            "ui": {"applied_res": [f"{applied_label} ({width}x{height})"]},
            "result": ({"samples": latent}, width, height)
        }

NODE_CLASS_MAPPINGS = {"LatentGenerator": LatentGenerator}
NODE_DISPLAY_NAME_MAPPINGS = {"LatentGenerator": "⚖️ Shaker Latent Generator"}