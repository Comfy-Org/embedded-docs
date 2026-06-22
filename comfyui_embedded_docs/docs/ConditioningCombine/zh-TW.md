# 條件（合併）

此節點將兩個條件輸入合併為單一輸出，有效融合其資訊。兩個條件透過列表串接的方式進行合併。

## 輸入

| 參數名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `conditioning_1` | 第一個要合併的條件輸入。在合併過程中與 `conditioning_2` 具有同等重要性。 | `CONDITIONING` |
| `conditioning_2` | 第二個要合併的條件輸入。在合併過程中與 `conditioning_1` 具有同等重要性。 | `CONDITIONING` |

## 輸出

| 參數名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `conditioning` | 合併 `conditioning_1` 和 `conditioning_2` 的結果，封裝了融合後的資訊。 | `CONDITIONING` |

## 使用場景

請比較以下兩組結果：左側使用 ConditioningCombine 節點，右側顯示正常輸出。

![比較](./asset/compare.jpg)

在此範例中，`Conditioning Combine` 中使用的兩個條件具有同等重要性。因此，您可以針對圖像風格、主體特徵等使用不同的文字編碼，讓提示詞特徵更完整地輸出。第二個提示詞使用合併後的完整提示詞，但語義理解可能會編碼出完全不同的條件。

使用此節點，您可以實現：

- 基本文字合併：將兩個 `CLIP Text Encode` 節點的輸出連接到 `Conditioning Combine` 的兩個輸入埠
- 複雜提示詞組合：結合正面與負面提示詞，或分別編碼主要描述與風格描述後再合併
- 條件鏈式組合：可串聯使用多個 `Conditioning Combine` 節點，實現多個條件的逐步組合

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningCombine/zh-TW.md)
