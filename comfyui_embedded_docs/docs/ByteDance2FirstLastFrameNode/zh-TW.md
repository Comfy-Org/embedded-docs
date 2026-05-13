> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/zh-TW.md)

此節點使用 ByteDance 的 Seedance 2.0 模型來生成影片。它根據文字提示和必要的第一幀圖像來創建影片。您可以選擇性地提供最後一幀圖像，以引導影片序列的結尾。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `模型` | COMBO | 是 | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | 用於影片生成的模型。Seedance 2.0 提供最高品質，而 Seedance 2.0 Fast 則針對速度進行了優化。選擇模型後，將顯示 `prompt`、`resolution`、`ratio`、`duration` 和 `generate_audio` 的額外輸入。 |
| `首幀圖像` | IMAGE | 否 | - | 用作影片第一幀的圖像。 |
| `末幀圖像` | IMAGE | 否 | - | 用作影片最後一幀的圖像。 |
| `first_frame_asset_id` | STRING | 否 | - | 用作第一幀的 Seedance asset_id。此項不能與 `首幀圖像` 圖像輸入同時使用。預設為空字串。 |
| `last_frame_asset_id` | STRING | 否 | - | 用作最後一幀的 Seedance asset_id。此項不能與 `末幀圖像` 圖像輸入同時使用。預設為空字串。 |
| `種子` | INT | 否 | 0 到 2147483647 | 種子值。更改此種子值將導致節點重新執行，但結果是非確定性的。預設為 0。 |
| `浮水印` | BOOLEAN | 否 | - | 是否為生成的影片添加浮水印。預設為 False。 |

**參數限制：**
*   您必須提供 **`first_frame` 圖像** 或 **`first_frame_asset_id`** 中的其中一項。同時提供兩者將會導致錯誤。
*   您不能同時為同一幀提供 `last_frame` 圖像和 `last_frame_asset_id`。
*   `model` 輸入是一個動態組合框。選擇模型後，您還必須填寫顯示出來的 `prompt` 欄位（文字描述），並配置其他顯示出來的參數（`resolution`、`ratio`、`duration`、`generate_audio`）。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片。 |

---
**Source fingerprint (SHA-256):** `2c9c1fe8fddd0c3e1c356d2b93a06a07f83db8f7a0380e94629a91ce1ff1e29a`
