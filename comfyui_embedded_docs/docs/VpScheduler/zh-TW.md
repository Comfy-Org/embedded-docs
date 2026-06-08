VPScheduler 節點旨在根據變異數保持（VP）排程方法生成一系列噪聲級別（sigmas）。此序列對於引導擴散模型中的去噪過程至關重要，可實現對圖像或其他數據類型的受控生成。

## 輸入

| 參數 | 描述 | 資料類型 |
| --- | --- | --- |
| `步驟數` | 指定擴散過程中的步驟數，影響所生成噪聲級別的細粒度。 | INT |
| `beta_d` | 決定整體噪聲級別分佈，影響所生成噪聲級別的變異數。 | FLOAT |
| `beta_min` | 設定噪聲級別的最小邊界，確保噪聲不會低於特定閾值。 | FLOAT |
| `eps_s` | 調整起始 epsilon 值，微調擴散過程中的初始噪聲級別。 | FLOAT |

## 輸出

| 參數 | 描述 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 基於 VP 排程方法生成的一系列噪聲級別（sigmas），用於引導擴散模型中的去噪過程。 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VPScheduler/zh-TW.md)
