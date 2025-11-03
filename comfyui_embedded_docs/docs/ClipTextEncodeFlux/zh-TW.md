> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeFlux/zh-TW.md)

`CLIPTextEncodeFlux` 是 ComfyUI 中專為 Flux 架構設計的進階文字編碼節點。它採用雙編碼器機制（CLIP-L 和 T5XXL）來處理結構化關鍵字和詳細的自然語言描述，為 Flux 模型提供更準確、更全面的文字理解，從而提升文字生成圖像的品質。

此節點基於雙編碼器協作機制：

1. `clip_l` 輸入由 CLIP-L 編碼器處理，提取風格、主題等關鍵字特徵——適合簡潔的描述。
2. `t5xxl` 輸入由 T5XXL 編碼器處理，擅長理解複雜且詳細的自然語言場景描述。
3. 兩個編碼器的輸出會進行融合，並結合 `guidance` 參數生成統一的條件嵌入（`CONDITIONING`），供下游 Flux 採樣器節點使用，以控制生成內容與文字描述的貼合程度。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入方式 | 預設值 | 數值範圍 | 描述 |
|-----------|----------|-------------|---------|-------|-------------|
| `clip`    | CLIP     | 節點輸入  | 無    | -     | 必須是支援 Flux 架構的 CLIP 模型，包含 CLIP-L 和 T5XXL 編碼器 |
| `clip_l`  | STRING   | 文字框    | 無    | 最多 77 個 token | 適合簡潔的關鍵字描述，例如風格或主題 |
| `t5xxl`   | STRING   | 文字框    | 無    | 幾乎無限制 | 適合詳細的自然語言描述，表達複雜的場景和細節 |
| `引導`| FLOAT    | 滑桿      | 3.5     | 0.0 - 100.0 | 控制文字條件對生成過程的影響程度；數值越高表示越嚴格遵循文字描述 |

## 輸出參數

| 輸出名稱   | 資料類型    | 描述 |
|--------------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | 包含來自兩個編碼器的融合嵌入和引導參數，用於條件式圖像生成 |

## 使用範例

### 提示詞範例

- **clip_l 輸入**（關鍵字風格）：
  - 使用結構化、簡潔的關鍵字組合
  - 範例：`masterpiece, best quality, portrait, oil painting, dramatic lighting`
  - 重點在風格、品質和主要主題

- **t5xxl 輸入**（自然語言描述）：
  - 使用完整、流暢的場景描述
  - 範例：`A highly detailed portrait in oil painting style, featuring dramatic chiaroscuro lighting that creates deep shadows and bright highlights, emphasizing the subject's features with renaissance-inspired composition.`
  - 重點在場景細節、空間關係和光影效果

### 注意事項

1. 請確保使用與 Flux 架構相容的 CLIP 模型
2. 建議同時填寫 `clip_l` 和 `t5xxl` 以發揮雙編碼器優勢
3. 請注意 `clip_l` 的 77 個 token 限制
4. 根據生成結果調整 `guidance` 參數