import importlib
import os
import shutil


comfy_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
captain_path = os.path.abspath(os.path.dirname(__file__))

def setup_js():
    try:
        js_dest_path = os.path.join(comfy_path, "web", "extensions",  "ComfyUI-Captain-Nodes")
        js_src_path = os.path.join(captain_path, "extensions")
        print(js_src_path)
        print(js_dest_path)
        if os.path.exists(js_dest_path):
            shutil.rmtree(js_dest_path)

        shutil.copytree(js_src_path, js_dest_path)
        
    except Exception as e:
        print(f"An error occurred: {e}")

setup_js()


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

# Ensure dependencies are installed before loading any custom nodes
do_install()

# List of node files
node_list = [ 
    "join_text",
    "openai_chat",
    "openai_image_analysis",
    "image_to_base64",
    "preview_text"
]

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

for module_name in node_list:
    module_path = ".nodes." + module_name  # Adjusted to include the subfolder
    try:
        imported_module = importlib.import_module(module_path, __name__)
        NODE_CLASS_MAPPINGS = {**NODE_CLASS_MAPPINGS, **imported_module.NODE_CLASS_MAPPINGS}
        if hasattr(imported_module, "NODE_DISPLAY_NAME_MAPPINGS"):
            NODE_DISPLAY_NAME_MAPPINGS = {**NODE_DISPLAY_NAME_MAPPINGS, **imported_module.NODE_DISPLAY_NAME_MAPPINGS}
    except ModuleNotFoundError as e:
        print(f"Captain says: Failed to load module {module_name}. Error: {e}")
    except Exception as e:
        print(f"Captain says: An error occurred while loading module {module_name}. Error: {e}")

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
