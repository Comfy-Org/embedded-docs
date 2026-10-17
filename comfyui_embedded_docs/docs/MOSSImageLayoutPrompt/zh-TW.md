# MOSS-Image Layout Prompt

建立 MOSS-Image 所讀取的版面提示（layout prompt）。它接收在 Create Bounding Boxes 節點中繪製的元素，並輸出一個 JSON 版面，其中每個框各有一筆項目：其標籤、其說明文字，以及其在目標畫布像素空間中的矩形。將 `width` 與 `height` 設為你打算生成的圖片尺寸，然後把輸出連接到文字編碼器的提示輸入。若未連接任何元素，提示文字會原樣返回。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt` | 整張圖片的描述。它會成為版面的說明文字。 | STRING | 是 | - |
| `element` | 要放置的元素，取自 Create Bounding Boxes 節點。每個框都會貢獻其說明文字；文字框還會貢獻其文字內容，而帶有調色盘的框則會保留該調色盘。 | ARRAY | 是 | - |
| `width` | 生成圖片的寬度（像素）。框會被轉換到此像素網格中，因此請使用你打算生成的圖片尺寸（預設：1024）。 | INT | 是 | 16 至 16384（步進值：16） |
| `height` | 生成圖片的高度（像素）。框會被轉換到此像素網格中，因此請使用你打算生成的圖片尺寸（預設：1024）。 | INT | 是 | 16 至 16384（步進值：16） |
| `character_boxes` | 要標記為角色（而非物件）的框編號，即在 Create Bounding Boxes 預覽中所標記的編號，例如 "1, 3"。字串中的每個數字都會被讀取，因此任何分隔符皆可（預設：空）。 | STRING | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `prompt` | 版面提示：一個 JSON 物件，包含說明文字、每個框各一筆項目，以及框座標格式。若未連接任何元素，則會直接傳遞輸入文字。 | STRING |

## 注意事項

框的矩形會由 Create Bounding Boxes 以 0 到 1000 之間的標準化座標傳入，並以相對於畫布中心的像素、依 `yxyx` 順序寫入版面。因此 `width` 與 `height` 的值必須與你生成的圖片相符，否則框會落在錯誤的位置。

含有文字的框一律標記為文字，編號列於 `character_boxes` 中的框會標記為角色，其餘每個框則標記為物件。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MOSSImageLayoutPrompt/zh-TW.md)

---
**Source fingerprint (SHA-256):** `da012a8d0dceaf6391110c90bd677d7929920d60fe961c00e5011b037206aa9a`
