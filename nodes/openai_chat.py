import json
from openai import OpenAI

class OpenAIChat:
    """
    A node that creates a formatted message object with a system message and a user message,
    then sends it to the OpenAI API using the provided API key and prints the response.

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
    CATEGORY = "Captain/Chat"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": "Enter your OpenAI API key"
                }),
                 "model": (["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo", "gpt-4o"], {
                    "default": "gpt-3.5-turbo"
                }),
                "system_message": ("STRING", {
                    "multiline": True,
                    "default": "System message goes here."
                }),
                "user_message": ("STRING", {
                    "multiline": True,
                    "default": "User message goes here."
                }),
                "seed": ("INT", {
                    "default": 0, 
                    "display": "number"
                }),
            },
        }

    ## @classmethod
    ## def IS_CHANGED(cls):
    ##     # Force re-evaluation of the node
    ##     return float("NaN")
    
    def execute(self, api_key, model, system_message, user_message, seed):
        """ Sends formatted messages to OpenAI API using the provided API key and prints the response.

        Parameters:
        api_key (str): The OpenAI API key.
        model (str): The OpenAI model.
        system_message (str): The message from the system.
        user_message (str): The message from the user.

        Returns:
        tuple: Contains the response from the API.
        """
    
        client = OpenAI(
            api_key=api_key
        )

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]
        completion = client.chat.completions.create(
            model = model,
            messages = messages
        )
        return (completion.choices[0].message.content,)

NODE_CLASS_MAPPINGS = {
    "OpenAIChat": OpenAIChat
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OpenAIChat": "OpenAI Chat"
}
