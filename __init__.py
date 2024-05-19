import importlib
import os

def do_install():
    try:
        # Construct the file path to install.py
        install_script_path = os.path.join(os.path.dirname(__file__), 'install.py')
        
        # Check if the install script actually exists
        if not os.path.exists(install_script_path):
            print("Captain says: Installation script not found. Please check the presence of 'install.py'.")
            return
        
        # Load and execute the installation script
        spec = importlib.util.spec_from_file_location('captain_install', install_script_path)
        captain_install = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(captain_install)
        print("Captain says: Dependencies installed successfully.")
    except Exception as e:
        print(f"Captain says: Failed to install dependencies: {str(e)}")

do_install()

node_list = [ #Add list of .py files containing nodes here
    "join_text",
    "openai_chat",
    "openai_image_analysis",
    "image_to_base64"
]

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

for module_name in node_list:
    module_path = ".nodes." + module_name  # Adjusted to include the subfolder
    imported_module = importlib.import_module(module_path, __name__)

    NODE_CLASS_MAPPINGS = {**NODE_CLASS_MAPPINGS, **imported_module.NODE_CLASS_MAPPINGS}
    if hasattr(imported_module, "NODE_DISPLAY_NAME_MAPPINGS"):
        NODE_DISPLAY_NAME_MAPPINGS = {**NODE_DISPLAY_NAME_MAPPINGS, **imported_module.NODE_DISPLAY_NAME_MAPPINGS}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
