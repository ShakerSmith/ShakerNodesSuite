import json

class ShakerConcatAny:
    """
    A lazy string concatenation node for the ShakerNodes Suite. 
    Ignores empty/null/whitespace-only inputs and merges valid text.
    Features dynamic expansion from 4 to 20 inputs.
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "delimiter": ("STRING", {"default": ", "}),
                "use_linebreaks": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                # ComfyUI will show these first 4 by default
                "input_1": ("STRING", {"forceInput": True}),
                "input_2": ("STRING", {"forceInput": True}),
                "input_3": ("STRING", {"forceInput": True}),
                "input_4": ("STRING", {"forceInput": True}),
                # The remaining slots are defined so the backend can grow dynamically
                **{f"input_{i}": ("STRING", {"forceInput": True}) for i in range(5, 21)}
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "concatenate"
    CATEGORY = "ShakerNodes/Logic"

    def concatenate(self, delimiter, use_linebreaks, **kwargs):
        valid_strings = []
        
        # Sort keys numerically (1, 2, 3...) rather than alphabetically (1, 10, 11...)
        sorted_keys = sorted(kwargs.keys(), key=lambda x: int(x.split('_')[-1]))

        for key in sorted_keys:
            val = kwargs[key]
            
            # Lazy Logic: Only keep it if it's a non-empty string
            if val is not None and isinstance(val, str):
                cleaned_val = val.strip()
                if cleaned_val:
                    valid_strings.append(cleaned_val)

        if not valid_strings:
            return ("",)

        # Handle the separator logic
        # If use_linebreaks is True, we use double newline; otherwise use custom delimiter
        actual_delimiter = "\n\n" if use_linebreaks else delimiter
        
        result = actual_delimiter.join(valid_strings)
        
        return (result,)

# Mapping for ComfyUI to recognize the node
NODE_CLASS_MAPPINGS = {
    "ShakerConcatAny": ShakerConcatAny
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ShakerConcatAny": "🔗 Shaker Concatenate Any"
}