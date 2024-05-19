class JoinTextsNode:
    """
    A node that joins two input strings with a newline.

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
    FUNCTION = "execute"
    RETURN_TYPES = ("STRING",)
    CATEGORY = "Captain/Utilities"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first_string": ("STRING", {
                    "multiline": True,
                    "default": "First String"
                }),
                "second_string": ("STRING", {
                    "multiline": True,
                    "default": "Second String"
                }),
                 "delimiter": ("STRING", {
                    "multiline": False,
                    "default": ", "
                }),
            },
        }

    def execute(self, first_string, second_string, delimiter):
        """ Joins two strings with a newline.

        Parameters:
        first_string (str): The first string to join.
        second_string (str): The second string to join.
        delimiter (str): The delimiter used to join the two strings.

        Returns:
        tuple: Contains the joined strings.
        """
        return (f"{first_string}{delimiter}{second_string}",)

NODE_CLASS_MAPPINGS = {
    "JoinTextsNode": JoinTextsNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "JoinTextsNode": "Join Texts Node"
}
