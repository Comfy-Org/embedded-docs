# BriaVideoEraser

使用 Bria 將每一幀遮罩所覆蓋的內容從影片中抹除，並填補留下的空缺。遮罩中欲抹除的區域必須為白色，其餘區域為黑色。Bria 接受最長 5.1 秒、影格率 20 至 30 fps、像素尺寸為偶數的片段；預設會保留音訊。回傳的片段可能比輸入少幾個影格。

## 輸入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `video` | 要從中抹除內容的片段。 | VIDEO | 是 | - |
| `mask` | 影片每一幀對應一個遮罩，欲抹除物件所在的區域為白色。請擇一提供 `mask` 或 `mask_video`，不可同時提供。 | MASK | No | - |
| `mask_video` | 已編碼的遮罩影片，其尺寸與影格數必須與影片相同。請擇一提供 `mask` 或 `mask_video`，不可同時提供。 | VIDEO | No | - |
| `preserve_audio` | 保留輸入的音軌。預設值：true。 | BOOLEAN | No | `true`<br>`false` |

**限制條件說明：**

- `mask` 與 `mask_video` 必須恰好連接其中一個。若兩者皆未提供，或兩者同時提供，都會引發錯誤。
- 影片長度不得超過 5.1 秒，且影格率必須為 20 至 30 fps。如有需要，可使用 Get Video Components 與 Create Video 重新調整片段的時間。
- 影片的像素尺寸必須為偶數（寬與高皆須能被 2 整除）。否則請先進行裁切或縮放。
- 使用 `mask` 時，每一個影片影格必須對應一個遮罩影格，且其長寬比必須與影片相符。遮罩會以 50% 為界進行二值化：不透明度低於一半的區域會被忽略，而空白的遮罩會引發錯誤。若遮罩解析度與影片不同，會將其縮放至影片尺寸。
- 使用 `mask_video` 時，其尺寸與影格數必須與影片完全相同。

## 輸出

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `video` | 已抹除遮罩區域並填補空缺的編輯後片段。可能比輸入片段少幾個影格。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoEraser/zh-TW.md)

---
**Source fingerprint (SHA-256):** `525b90013b9d9ea4b224caf1f32479493c96f90e28acbf3cf7a4d16a6ca91a45`
