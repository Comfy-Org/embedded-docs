> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningCombine/zh-TW.md)

此節點將兩個條件輸入合併為單一輸出，有效地整合它們的資訊。這兩個條件是透過列表串接的方式進行合併。

## 輸入參數

| 參數名稱             | 資料類型           | 描述 |
|----------------------|--------------------|------|
| `conditioning_1`     | `CONDITIONING`     | 要合併的第一個條件輸入。在合併過程中與 `conditioning_2` 具有同等重要性。 |
| `conditioning_2`     | `CONDITIONING`     | 要合併的第二個條件輸入。在合併過程中與 `conditioning_1` 具有同等重要性。 |

## 輸出參數

| 參數名稱             | 資料類型           | 描述 |
|----------------------|--------------------|------|
| `conditioning`       | `CONDITIONING`     | 合併 `conditioning_1` 和 `conditioning_2` 的結果，封裝了整合後的資訊。 |

## 使用情境

比較以下兩組：左側使用 ConditioningCombine 節點，右側顯示正常輸出。

![比較](./asset/compare.jpg)

在此範例中，`Conditioning Combine` 中使用的兩個條件具有同等重要性。因此，您可以針對影像風格、主體特徵等使用不同的文字編碼，讓提示詞特徵能夠更完整地輸出。第二個提示詞使用了合併後的完整提示詞，但語義理解可能會編碼出完全不同的條件。

使用此節點，您可以實現：

- 基本文字合併：將兩個 `CLIP Text Encode` 節點的輸出連接到 `Conditioning Combine` 的兩個輸入端口
- 複雜提示詞組合：合併正向和負向提示詞，或分別編碼主要描述和風格描述後再進行合併
- 條件鏈組合：可以串聯多個 `Conditioning Combine` 節點來實現多個條件的漸進式組合