import cv2
import numpy as np
from io import BytesIO
import base64
from PIL import Image

class ImageToBase64:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {"default": ""}),  # Expecting an image input
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "image_to_base64"
    CATEGORY = "🧑‍✈️ Captain/🖼️ Image"

    def image_to_base64(self, image):
        """Converts an image to a Base64 string.

        Parameters:
        image (Image): The image to convert, received as a PIL Image.

        Returns:
        tuple: Contains the Base64 string of the image.
        """
        # Convert PIL Image to a NumPy array
        image_np = np.array(image)

        # Handle batch or extra dimension if present
        if image_np.shape[0] == 1:  # Assuming batch size of 1
            image_np = image_np.squeeze(0)  # Remove the batch dimension

        # Debugging output
        print("Adjusted Image shape:", image_np.shape)
        print("Adjusted Image dtype:", image_np.dtype)

        # Convert float to uint8 if necessary
        if image_np.dtype != np.uint8:
            image_np = (image_np * 255).astype(np.uint8)

        # Encode the image using OpenCV
        retval, buffer = cv2.imencode('.png', image_np)
        if retval:
            # Convert to base64 string
            base64_str = base64.b64encode(buffer).decode('utf-8')
            return (base64_str,)
        else:
            return ("Failed to convert image",)

NODE_CLASS_MAPPINGS = {
    "Captain__ImageToBase64": ImageToBase64,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Captain__ImageToBase64": "🧑‍✈️ Convert Image to Base64",
}
