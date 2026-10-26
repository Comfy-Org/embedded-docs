# ModelMergeMOSSImage

ModelMergeMOSSImage 節點透過逐區塊混合兩個 MOSS 影像模型的對應權重來合併它們，因此結果的一部分可來自基礎模型，其餘部分則來自微調模型或第二個模型。架構中的每個主要元件都有各自的混合比例：影片嵌入器、文字嵌入器、時間嵌入、共享區塊調變、全部 42 個 transformer 層，以及輸出頭。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model1` | 要合併的第一個模型。第二個模型未貢獻的部分皆保留自此模型 | MODEL | 是 | - |
| `model2` | 要合併的第二個模型。其權重會依據下列比例混合進來 | MODEL | 是 | - |
| `video_embedder.` | 影片嵌入器區塊的混合比例（預設值：1.0） | FLOAT | 是 | 0.0 到 1.0（步進值：0.01） |
| `text_embedder.proj.` | 文字嵌入器投影層的混合比例（預設值：1.0） | FLOAT | 是 | 0.0 到 1.0（步進值：0.01） |
| `text_embedder.blocks.0.` 與 `text_embedder.blocks.1.` | 兩個文字嵌入器區塊各自的混合比例（預設值：1.0） | FLOAT | 是 | 0.0 到 1.0（步進值：0.01） |
| `time_embedding.` | 時間嵌入區塊的混合比例（預設值：1.0） | FLOAT | 是 | 0.0 到 1.0（步進值：0.01） |
| `shared_block_modulation.` | transformer 區塊所使用之共享調變層的混合比例（預設值：1.0） | FLOAT | 是 | 0.0 到 1.0（步進值：0.01） |
| `layers.0.` 到 `layers.41.` | 42 個 transformer 層各自的混合比例（預設值：1.0） | FLOAT | 是 | 0.0 到 1.0（步進值：0.01） |
| `final_norm_video.` | 影片串流最終正規化的混合比例（預設值：1.0） | FLOAT | 是 | 0.0 到 1.0（步進值：0.01） |
| `final_linear_video.` | 影片串流最終線性層的混合比例（預設值：1.0） | FLOAT | 是 | 0.0 到 1.0（步進值：0.01） |
| `video_head_modulation.` | 影片輸出頭調變層的混合比例（預設值：1.0） | FLOAT | 是 | 0.0 到 1.0（步進值：0.01） |

比例為 0.0 時會讓該元件維持 `model1` 中的原樣，比例為 1.0 時則完全取自 `model2`，介於兩者之間的值會產生加權混合。兩個輸入都必須是架構相同的 MOSS 影像模型；不符合上述任何前綴的權重會退回使用 `video_embedder.` 的比例。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 合併後的模型，依指定比例組合兩個輸入 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMOSSImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3b7d9c806a8d53ad00044bf30f5e63431fea7ee565414acb70a56e3059164288`
