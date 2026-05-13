> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseFaceBBoxes/en.md)

The SDPoseFaceBBoxes node processes pose keypoint data to detect and generate bounding boxes around human faces. It analyzes the 2D face keypoints for each person in a frame, calculates a bounding box based on those points, and can adjust the box's size and shape. The resulting bounding boxes are formatted to be compatible with other nodes in the SDPose workflow, such as the SDPoseKeypointExtractor.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `keypoints` | POSE_KEYPOINT | Yes | - | The pose keypoint data containing information about detected people and their body/face landmarks per frame. |
| `scale` | FLOAT | No | 1.0 - 10.0 | Multiplier for the bounding box area around each detected face. A larger value creates a larger box. (default: 1.5) |
| `force_square` | BOOLEAN | No | - | Expand the shorter bbox axis so the crop region is always square. (default: True) |

**Note:** The `keypoints` input must be in the specific format produced by nodes like SDPoseKeypointExtractor, containing `canvas_height`, `canvas_width`, and `people` data with `face_keypoints_2d` for each person.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `bboxes` | BOUNDINGBOX | A list of face bounding boxes for each frame. Each bounding box is defined by its top-left coordinates (`x`, `y`), `width`, and `height`. This output is compatible with the `bboxes` input of the SDPoseKeypointExtractor node. |

---
**Source fingerprint (SHA-256):** `bffbcddb882f6743a6cace6a4884fa5a257b746897c79ba9260c15260fab874e`
