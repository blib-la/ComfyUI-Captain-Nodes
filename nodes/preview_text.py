class PreviewText:
    """
    A node that previews the given text.

    Class methods
    -------------
    INPUT_TYPES (dict):
        Defines input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`tuple`):
        The type of each element in the output tuple.
    FUNCTION (`str`):
        The name of the entry-point method.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    """
    FUNCTION = "preview_text"
    RETURN_TYPES = ("STRING",)
    OUTPUT_NODE = True
    CATEGORY = "Captain/Utilities"

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            },
            "hidden": {
                "prompt": "PROMPT",
                "extra_pnginfo": "EXTRA_PNGINFO"
            },
        }

    def preview_text(self, text, prompt=None, extra_pnginfo=None):
        """ Previews the given text.

        Parameters:
        text (str): The text to preview.
        prompt (str, optional): The prompt associated with the text.
        extra_pnginfo (str, optional): Additional PNG info.

        Returns:
        dict: Contains the preview text in the UI and the result text.
        """
        return {"ui": {"string": [text]}, "result": (text,)}

NODE_CLASS_MAPPINGS = {
    "PreviewText": PreviewText
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PreviewText": "Preview Text"
}
