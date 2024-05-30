# ComfyUI Captain Nodes

Welcome to the ComfyUI Captain Nodes repository! This collection of nodes enhances [Captain](https://get-captain.com)—a desktop tool that allows you to run AI models locally on your computer. With Captain, you can quickly start applications, search data using natural language, and build custom AI apps, all while keeping your data private and offline.

<div align="center">
  <img src="https://github.com/blib-la/ComfyUI-Captain-Nodes/assets/1148334/01c09224-6788-438d-a006-2bae4afcd78a" alt="nodes example"/ >
</div>

## Features of ComfyUI Captain Nodes

> [!NOTE]
> This set of nodes is compatible with a native ComfyUI installation

This package extends Captain's capabilities by providing specialized nodes for AI integration and utility functions, making it easier to harness powerful AI features directly on your desktop:

### Included Nodes

- **[Image to Base64](nodes/image_to_base64.py)**: Converts images to Base64, facilitating easier image handling and storage.
- **[Join Text](nodes/join_text.py)**: Combines multiple text inputs into one string, simplifying data aggregation.
- **[Preview Text](nodes/previw_text.py)**: Outputs a preview of the generated text and passes it through.
- **[OpenAI Chat](nodes/openai_chat.py)**: Integrates OpenAI’s conversational models to enable dynamic interactions with AI.
- **[OpenAI Image Analysis](nodes/openai_image_analysis.py)**: Utilizes AI to analyze and interpret images, providing detailed insights and descriptions.

## Getting Started

### Automatic Installation

To install these nodes, open the integrated marketplace within the Captain application, search for "Captain Nodes", and download the package. A restart of Captain will be required upon completion to fully integrate the new nodes.

### Manual Installation

If you prefer to install the nodes manually or need to install them from a local source, follow these steps:

1. **Locate the Captain Downloads Directory**:

   - Find the `custom_nodes` folder within Captain, typically located at `C:\Users\<USERNAME>\AppData\Roaming\captain\Captain_Data\downloads\comfyui\custom_nodes`. This directory is persistent through updates and is the recommended location for placing custom nodes.

2. **Clone the Repository**:

   - Open a terminal or command prompt and navigate to the `custom_nodes` directory:

     ```sh
     cd C:\Users\<USERNAME>\AppData\Roaming\captain\Captain_Data\downloads\comfyui\custom_nodes
     ```

   - Clone this repository into the `custom_nodes` directory:

     ```sh
     git clone https://github.com/blib-la/ComfyUI-Captain-Nodes.git
     ```

   - Ensure the cloned files are placed directly in the `custom_nodes` folder to be recognized by Captain. For example, the path should look like this: `C:\Users\<USERNAME>\AppData\Roaming\captain\Captain_Data\downloads\comfyui\custom_nodes\ComfyUI-Captain-Nodes\install.py`.

For more detailed instructions and support, visit the [official Captain documentation](https://get-captain.com) or the [Captain GitHub repository](https://github.com/blib-la/captain).

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository, create a pull request, or open an issue with the tag "enhancement".

## License

This project is licensed under the AGPL-3.0 License - see the [LICENSE](LICENSE) file for details.
