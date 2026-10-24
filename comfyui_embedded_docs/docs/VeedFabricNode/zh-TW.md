# VEED Fabric 1.0

使用 VEED Fabric 將靜態影像和語音軌轉換為會說話、對嘴同步的影片。只要臉部清晰可見，它可處理照片、插圖和吉祥物；影片會保持影像的長寬比，長度與音訊相同。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的模型。選取模型後會顯示其專屬參數：`image`、`audio` 和 `resolution`。 | DYNAMIC_COMBO | 是 | `"fabric-1.0"` |
| `image` | 臉部清晰可見的影像。影片會保持其長寬比。 | IMAGE | 是 | - |
| `audio` | 要對嘴同步的語音，最長 300 秒。會設定影片長度。 | AUDIO | 是 | 最多 300 秒 |
| `resolution` | 輸出尺寸等級：`"480p"` 時約 0.4 百萬像素（16:9 下為 864x480），`"720p"` 時約 0.9 百萬像素（16:9 下為 1312x736）。（預設值：`"720p"`） | COMBO | 是 | `"480p"`<br>`"720p"` |

當語音軌長度超過 300 秒時，此節點會停止並顯示錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `VIDEO` | 會說話的影片：輸入影像會動畫化以配合語音軌。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedFabricNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `69cabfa5f03885ce770e8502419305dacee49d7e89a748f31abe3775d682a33a`
