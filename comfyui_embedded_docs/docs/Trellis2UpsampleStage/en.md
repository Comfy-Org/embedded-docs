# Trellis2 Upsample Stage

This node upscales a 512-resolution shape latent into high-resolution sparse coordinates and prepares the second shape-stage sampling pass at the target resolution. It attaches per-stage metadata to the conditioning so the model can consume it during generation.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `positive` | The positive conditioning to which the upsampling-stage shape metadata is attached. | CONDITIONING | Yes | |
| `negative` | The negative conditioning to which the upsampling-stage shape metadata is attached. | CONDITIONING | Yes | |
| `shape_latent` | The 512-resolution shape latent output from the first shape-stage KSampler. | LATENT | Yes | |
| `vae` | The Trellis2 VAE used to decode the shape latent into high-resolution sparse coordinates. | VAE | Yes | |
| `target_resolution` | Voxel resolution of the upsampled shape. Higher = more detail, more VRAM. Default: 1024. | INT | Yes | 1024 - 2048 (step 128) |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `positive` | Positive conditioning with the upsampling-stage shape metadata attached. | CONDITIONING |
| `negative` | Negative conditioning with the upsampling-stage shape metadata attached. | CONDITIONING |
| `latent` | Zero-filled latent prepared for the second shape-stage sampling pass at the target resolution, carrying the upsampled coordinates, per-sample coordinate counts, and coordinate resolution metadata. | LATENT |

## Using a 64-resolution shape latent

The current `Trellis2UpsampleStage` implementation scales coordinates as though the input came from a 32-resolution structure latent. Its four upsampling blocks produce a 512-grid from that input. A 64-resolution latent produces a 1024-grid, so sending it through this node uses mismatched coordinate scales and can corrupt the mesh.

As a workaround for a 64-resolution workflow, bypass `Trellis2UpsampleStage` and its second shape-sampling pass. Connect the first shape-stage sampler directly to the shape decoder, such as `VaeDecodeShapeTrellis`. This avoids the mismatched rescaling, but also skips the high-resolution upsampling pass, so the output can differ. Direct shape decoding can still produce a very dense mesh; decimate it before memory-intensive mesh operations when needed. This workaround does not guarantee that later texture or baking stages will fit in memory.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2UpsampleStage/en.md)

---
**Source fingerprint (SHA-256):** `0582579bfab487718d69789de508a5ec243d98a0e06ad7165c406154a64677d6`
