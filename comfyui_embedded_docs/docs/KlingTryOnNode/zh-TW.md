# Kling Virtual Try-On

使用 Kling 的虛擬試穿功能，讓人物穿上某件服裝。連接一張人物照片和一張服裝照片，節點會回傳該人物穿著該服裝項目的新圖像。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `person_image` | 單一人物的照片，最好為正面或四分之三視角。若圖片任一邊超過 2048 像素，會先進行縮小。 | IMAGE | 是 | N/A |
| `garment_image` | 要穿上的服裝：產品照、平鋪照、人台或模特兒實穿照。模特兒實穿照可能會沿用該套服裝的其餘部分。僅限服裝；不支援鞋子、包包和配件。 | IMAGE | 是 | N/A |
| `keep_pose` | 關閉後可讓姿勢改變，以獲得更佳的服裝呈現效果。進階參數（預設：True）。 | BOOLEAN | 是 | `True`<br>`False` |
| `seed` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果皆為非確定性。此參數具有「生成後控制」功能（預設：42）。 | INT | 是 | 0 至 2147483647 |

**注意：** 結果尺寸與 `person_image` 相同，最長邊上限為 2048 像素。兩個輸入都會上傳至 Kling 的 API，可能需要一些時間。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-----------|-----------|
| `IMAGE` | 穿著該服裝項目的人物。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTryOnNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `03c2f9f1169ec2de3dd58162f9a7718a9c1f9af584aa63f280a0c4feefb70478`
