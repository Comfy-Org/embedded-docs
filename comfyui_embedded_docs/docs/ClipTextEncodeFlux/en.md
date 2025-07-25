`CLIPTextEncodeFlux` is an advanced text encoding node in ComfyUI, specifically designed for the Flux architecture. It uses a dual-encoder mechanism (CLIP-L and T5XXL) to process both structured keywords and detailed natural language descriptions, providing the Flux model with more accurate and comprehensive text understanding for improved text-to-image generation quality.

This node is based on a dual-encoder collaboration mechanism:

1. The `clip_l` input is processed by the CLIP-L encoder, extracting style, theme, and other keyword features—ideal for concise descriptions.
2. The `t5xxl` input is processed by the T5XXL encoder, which excels at understanding complex and detailed natural language scene descriptions.
3. The outputs from both encoders are fused, and combined with the `guidance` parameter to generate unified conditioning embeddings (`CONDITIONING`) for downstream Flux sampler nodes, controlling how closely the generated content matches the text description.

## Inputs

| Parameter | Data Type | Input Method | Default | Range | Description |
|-----------|----------|-------------|---------|-------|-------------|
| `clip`    | CLIP     | Node input  | None    | -     | Must be a CLIP model supporting the Flux architecture, including both CLIP-L and T5XXL encoders |
| `clip_l`  | STRING   | Text box    | None    | Up to 77 tokens | Suitable for concise keyword descriptions, such as style or theme |
| `t5xxl`   | STRING   | Text box    | None    | Nearly unlimited | Suitable for detailed natural language descriptions, expressing complex scenes and details |
| `guidance`| FLOAT    | Slider      | 3.5     | 0.0 - 100.0 | Controls the influence of text conditions on the generation process; higher values mean stricter adherence to the text |

## Outputs

| Output Name   | Data Type    | Description |
|--------------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Contains the fused embeddings from both encoders and the guidance parameter, used for conditional image generation |

## Usage Examples

### Prompt Examples

- **clip_l input** (keyword style):
  - Use structured, concise keyword combinations
  - Example: `masterpiece, best quality, portrait, oil painting, dramatic lighting`
  - Focus on style, quality, and main subject

- **t5xxl input** (natural language description):
  - Use complete, fluent scene descriptions
  - Example: `A highly detailed portrait in oil painting style, featuring dramatic chiaroscuro lighting that creates deep shadows and bright highlights, emphasizing the subject's features with renaissance-inspired composition.`
  - Focus on scene details, spatial relationships, and lighting effects

### Notes

1. Make sure to use a CLIP model compatible with the Flux architecture
2. It is recommended to fill in both `clip_l` and `t5xxl` to leverage the dual-encoder advantage
3. Note the 77-token limit for `clip_l`
4. Adjust the `guidance` parameter based on the generated results
