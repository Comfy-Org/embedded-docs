# Recraft 向量化圖片

從輸入影像產生 SVG 向量圖形。此節點會將點陣影像轉換為可縮放向量格式，方式是將每張影像傳送至 Recraft API，並在單一 SVG 輸出中傳回結果。該輸出會為每張已處理的影像保存個別的 SVG 文件；這些文件不會合併為一個。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `圖片` | 要轉換為 SVG 格式的輸入影像。支援批次處理多張影像。 | IMAGE | 是 | - |
| `version` | 向量化工具版本：`v1` 是標準版本，而 `v1_pro`（Vectorizer Pro）可產生更乾淨的 SVG，具有平滑曲線、直線和銳利轉角，最適合字體設計和複雜形狀（預設："v1"）。 | COMBO | 否 | "v1"<br>"v1_pro" |
| `shape_stacking` | 形狀在 SVG 中的堆疊方式：`hierarchical` 會將形狀層層疊加；`cut_out` 會產生永不重疊的形狀，適用於繪圖機、乙烯基切割機和網版印刷（預設："hierarchical"）。 | COMBO | 否 | "hierarchical"<br>"cut_out" |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `SVG` | 產生的向量圖形。單一 SVG 輸出會為每張已處理的影像保存個別的 SVG 文件。 | SVG |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b7f8245de0597e8d3ceeef5a15b378e0903965a7e15c1825cacdf2387b278c7e`
