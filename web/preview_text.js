import {app} from "/scripts/app.js";
import {ComfyWidgets} from "/scripts/widgets.js";
import {PREVIEW_TEXT_NODE_NAME} from "./constants.js";

console.log(`Captain Node: ${PREVIEW_TEXT_NODE_NAME} extension loaded`)
/**
 * Captain.previewText extension for enhancing the PreviewText node.
 * Adds custom string widget functionality for displaying output text.
 */
app.registerExtension({
  name: `Blibla.${PREVIEW_TEXT_NODE_NAME}`,

  /**
   * Hook into the node definition registration process.
   *
   * @param {Object} nodeType - The type of the node being registered.
   * @param {Object} nodeData - The data associated with the node.
   * @param {Object} app - The application instance.
   */
  async beforeRegisterNodeDef(nodeType, nodeData, app) {
    if (nodeData.name === PREVIEW_TEXT_NODE_NAME) {
      const originalOnNodeCreated = nodeType.prototype.onNodeCreated;

      /**
       * Override the onNodeCreated method to add a custom read-only string widget.
       */
      nodeType.prototype.onNodeCreated = function () {
        const response = originalOnNodeCreated
          ? originalOnNodeCreated.apply(this, arguments)
          : undefined;

        // Generate a unique node name based on the number of existing nodes of this type
        const previewTextNodes = app.graph._nodes.filter(
          (widget) => widget.type === nodeData.name
        );
        const nodeName = `${nodeData.name}_${previewTextNodes.length}`;

        // Create a read-only string widget for displaying text
        const stringWidget = ComfyWidgets.STRING(
          this,
          nodeName,
          [
            "STRING",
            {
              default: "",
              placeholder: "The output will appear here...",
              multiline: true,
            },
          ],
          app
        );
        stringWidget.widget.inputEl.readOnly = true;
        return response;
      };

      /**
       * Function to update the widget value with the provided texts.
       *
       * @param {Array|string} texts - The texts to be displayed in the widget.
       */
      const updateWidgetValue = function (texts) {
        if (texts.length > 0) {
          const widgetIndex = this.widgets.findIndex(
            (widget) => widget.type === "customtext"
          );

          if (Array.isArray(texts)) {
            texts = texts
              .map((text) => text.replace(/\s+/, " ").trim())
              .filter(Boolean)
              .join(" ");
          }

          this.widgets[widgetIndex].value = texts;
          app.graph.setDirtyCanvas(true);
        }
      };

      const originalOnExecuted = nodeType.prototype.onExecuted;

      /**
       * Override the onExecuted method to update the widget value upon execution.
       *
       * @param {Object} texts - The texts returned from node execution.
       */
      nodeType.prototype.onExecuted = function (texts) {
        if (originalOnExecuted) {
          originalOnExecuted.apply(this, arguments);
        }
        if (texts) {
          updateWidgetValue.call(this, texts.string);
        }
      };

      const originalOnConfigure = nodeType.prototype.onConfigure;

      /**
       * Override the onConfigure method to update the widget value upon configuration.
       *
       * @param {Object} widgetConfig - The configuration of the widget.
       */
      nodeType.prototype.onConfigure = function (widgetConfig) {
        originalOnConfigure?.apply(this, arguments);
        if (widgetConfig?.widgets_values?.length) {
          updateWidgetValue.call(this, widgetConfig.widgets_values);
        }
      };
    }
  },
});
