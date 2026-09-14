# LoopProgress

LoopProgress 是一個僅供開發使用的輔助節點，會將迴圈的進度回報至 ComfyUI 伺服器介面。每次執行時，它會將文字「Iteration X / Y」傳送給用戶端，並原樣傳回目前的迭代位置，這讓它可以內嵌在迴圈中，而不會改變資料流。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `start_id` | 進度訊息所屬的提示/迴圈執行個體識別碼。會使用所提供清單的第一個項目，將進度文字路由至正確的執行中作業。 | STRING | 是 | - |
| `position` | 目前的迭代位置（索引）。所提供清單的第一個項目會用於進度訊息，也會作為輸出傳回。 | INT | 是 | - |
| `total` | 迭代總數。會與 `position` 一起用來建立「Iteration X / Y」進度訊息。 | INT | 是 | - |

注意：此節點是以清單輸入（`is_input_list=True`）宣告，並接受所有輸入，因此每個連接的值都會被視為清單，且只會讀取其第一個元素。此節點一律會執行（其輸入指紋固定），因此每輪迴圈都會重新執行。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `position` | 目前的迭代位置，會從 `position` 輸入原樣傳遞。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopProgress/zh-TW.md)

---
**Source fingerprint (SHA-256):** `505ba814b93533679516b4f4239f5eee0dbac125d7ea16746c6cdbb7a68f803d`
