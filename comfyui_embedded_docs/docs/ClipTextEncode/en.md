`CLIP Text Encode (CLIPTextEncode)` acts like a translator, converting your creative text descriptions into a special "language" that AI can understand, helping the AI accurately interpret what kind of image you want to create.

Imagine communicating with a foreign artist - you need a translator to help accurately convey the artwork you want. This node acts as that translator, using the CLIP model (an AI model trained on vast amounts of image-text pairs) to understand your text descriptions and convert them into "instructions" that the AI art model can understand.

## Inputs

| Parameter | Data Type | Input Method | Default | Range | Description |
|-----------|-----------|--------------|---------|--------|-------------|
| text | STRING | Text Input | Empty | Any text | Like detailed instructions to an artist, enter your image description here. Supports multi-line text for detailed descriptions. |
| clip | CLIP | Model Selection | None | Loaded CLIP models | Like choosing a specific translator, different CLIP models are like different translators with slightly different understandings of artistic styles. |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| CONDITIONING | CONDITIONING | These are the translated "painting instructions" containing detailed creative guidance that the AI model can understand. These instructions tell the AI model how to create an image matching your description. |

## Usage Tips

1. **Basic Text Prompt Usage**
   - Write detailed descriptions like you're writing a short essay
   - More specific descriptions lead to more accurate results
   - Use English commas to separate different descriptive elements

2. **Special Feature: Using Embedding Models**
   - Embedding models are like preset art style packages that can quickly apply specific artistic effects
   - Currently supports .safetensors, .pt, and .bin file formats, and you don't necessarily need to use the complete model name
   - How to use:
     1. Place the embedding model file (in .pt format) in the `ComfyUI/models/embeddings` folder
     2. Use `embedding:model_name` in your text
     Example: If you have a model called `EasyNegative.pt`, you can use it like this:

     ```
     a beautiful landscape, embedding:EasyNegative, high quality
     ```

3. **Prompt Weight Adjustment**
   - Use parentheses to adjust the importance of certain descriptions
   - For example: `(beautiful:1.2)` will make the "beautiful" feature more prominent
   - Regular parentheses `()` have a default weight of 1.1
   - Use keyboard shortcuts `ctrl + up/down arrow` to quickly adjust weights
   - The weight adjustment step size can be modified in settings

4. **Important Notes**
   - Ensure the CLIP model is properly loaded
   - Use positive and clear text descriptions
   - When using embedding models, make sure the file name is correct and compatible with your current main model's architecture
