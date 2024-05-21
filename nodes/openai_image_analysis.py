import json
from openai import OpenAI


class ImageAnalysis:
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
    CATEGORY = "🧑‍✈️ Captain/💬 LLM"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": "sk-xxxxxxxxxx"
                }),
                "model": (["gpt-4-vision-preview", "gpt-4o"], {
                    "default": "gpt-4o"
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
                "base64": ("STRING", {
                    "multiline": True,
                })
            },
        }

    def execute(self, api_key, model, system_message, user_message, seed, base64):
        """ Sends formatted messages to OpenAI API using the provided API key and prints the response.

        Parameters:
        api_key (str): The OpenAI API key.
        model (str): The OpenAI model.
        system_message (str): The message from the system.
        user_message (str): The message from the user.
        seed (str): The seed of the generation.
        base64 (str): The image from the user.

        Returns:
        tuple: Contains the response from the API.
        """

        client = OpenAI(
            api_key=api_key
        )

        messages = [
            {"role": "system", "content": system_message},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_message},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64}"
                        },
                    },
                ],
            }
        ]
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            seed=seed
        )
        return (completion.choices[0].message.content,)


NODE_CLASS_MAPPINGS = {
    "Captain__ImageAnalysis": ImageAnalysis
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Captain__ImageAnalysis": "🧑‍✈️ OpenAI Image Analysis"
}
