# PhotoMaker 編碼

PhotoMakerEncode 節點將參考影像與文字提示結合，以建立用於影像生成的 conditioning 資料。當文字中包含「photomaker」一詞時，節點會使用 PhotoMaker 模型，將參考影像的視覺特徵插入到提示中該位置的 conditioning 中。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `photomaker` | 用於處理參考影像並生成基於影像之嵌入的 PhotoMaker 模型 | PHOTOMAKER | 是 | - |
| `影像` | 為 conditioning 提供視覺特徵的參考影像 | IMAGE | 是 | - |
| `clip` | 用於文字分詞與文字編碼的 CLIP 模型 | CLIP | 是 | - |
| `文字` | 用於生成 conditioning 的文字提示。支援多行文字與動態提示（預設值：「photograph of photomaker」） | STRING | 是 | Any string |

**注意：** 當文字包含獨立單詞「photomaker」時，節點會從編碼後的提示中移除該詞，並使用 PhotoMaker 模型在該位置套用參考影像的特徵。如果文字中未找到「photomaker」，節點將返回不帶影像影響的標準文字 conditioning。

## 輸出

| 輸出名 | 描述 | 資料型別 |
| --- | --- | --- |
| `CONDITIONING` | 包含引導影像生成之文字與影像嵌入的 conditioning 資料，以及來自 CLIP 文字編碼器的池化輸出 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `490a90c504ade253c2bb055e0efb1eb015ba6d7faf8f2370cac188871f678986`
