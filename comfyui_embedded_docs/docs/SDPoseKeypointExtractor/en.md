> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseKeypointExtractor/en.md)

The SDPoseKeypointExtractor node detects human pose keypoints from input images using the SDPose model. It can process full images or specific regions defined by bounding boxes and outputs the detected keypoints in the OpenPose format, which includes the coordinates for each person and a confidence score for each keypoint.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Yes | - | The SDPose model used for keypoint detection. Must be a model with a `heatmap_head` attribute, specifically from the SDPose repository. |
| `vae` | VAE | Yes | - | The VAE model used to encode the input images into the latent space for processing. |
| `image` | IMAGE | Yes | - | The input image or batch of images from which to extract pose keypoints. |
| `batch_size` | INT | No | 1 to 10000 | The number of images to process at once when running in full-image mode (i.e., when `bboxes` is not provided). This can speed up processing. (default: 16) |
| `bboxes` | BOUNDINGBOX | No | - | Optional bounding boxes for more accurate detections. Required for multi-person detection. If provided, the node will extract keypoints from each specified region. |

**Parameter Constraints:**
*   The `model` input must be a specific SDPose model. If the provided model does not have a `heatmap_head` attribute, the node will raise an error.
*   The node operates in two distinct modes based on the `bboxes` input:
    1.  **Bounding Box Mode:** When `bboxes` is provided, it processes each specified region individually. This is required for detecting multiple people in a single image.
    2.  **Full-Image Mode:** When `bboxes` is not provided, it processes the entire image as a batch. The `batch_size` parameter only applies in this mode.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `keypoints` | POSE_KEYPOINT | Keypoints in OpenPose frame format (canvas_width, canvas_height, people). The output contains the detected persons, each with an array of keypoint coordinates (x, y) and their corresponding confidence scores. |