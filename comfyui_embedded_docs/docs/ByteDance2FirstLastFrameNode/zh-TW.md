> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/zh-TW.md)

此節點使用字節跳動的 Seedance 2.0 模型來生成影片。它根據文字提示和必需的首幀圖像來創建影片。您可以選擇性地提供一個尾幀圖像來引導影片序列的結尾。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | 用於影片生成的模型。Seedance 2.0 用於最高品質，而 Seedance 2.0 Fast 則針對速度進行了優化。選擇模型後，將顯示 `prompt`、`resolution`、`ratio`、`duration` 和 `generate_audio` 的額外輸入欄位。 |
| `first_frame` | IMAGE | 否 | - | 用作影片第一幀的圖像。 |
| `last_frame` | IMAGE | 否 | - | 用作影片最後一幀的圖像。 |
| `first_frame_asset_id` | STRING | 否 | - | 用作第一幀的 Seedance asset_id。此參數不能與 `first_frame` 圖像輸入同時使用。預設為空字串。 |
| `last_frame_asset_id` | STRING | 否 | - | 用作最後一幀的 Seedance asset_id。此參數不能與 `last_frame` 圖像輸入同時使用。預設為空字串。 |
| `seed` | INT | 否 | 0 至 2147483647 | 種子值。更改此種子將導致節點重新運行，但結果是非確定性的。預設為 0。 |
| `watermark` | BOOLEAN | 否 | - | 是否在生成的影片中添加浮水印。預設為 False。 |

**參數限制：**
*   您必須提供 **`first_frame` 圖像** 或 **`first_frame_asset_id`** 中的一項。同時提供兩者將導致錯誤。
*   您不能為同一幀同時提供 `last_frame` 圖像和 `last_frame_asset_id`。
*   `model` 輸入是一個動態組合框。選擇模型後，您還必須填寫顯示的 `prompt` 欄位（文字描述）並配置其他顯示的參數（`resolution`、`ratio`、`duration`、`generate_audio`）。

## 輸出

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片。 |