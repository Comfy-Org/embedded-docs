`ExponentialScheduler` 節點旨在為擴散取樣過程生成遵循指數排程的 sigma 值序列。它提供了一種可自訂的方法來控制擴散過程中每一步應用的噪聲水平，從而實現對取樣行為的精細調整。

## 輸入

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `步驟數` | 指定擴散過程中的步驟數。它會影響生成的 sigma 序列的長度，進而影響噪聲應用的粒度。 | INT |
| `最大 sigma` | 定義最大 sigma 值，設定擴散過程中噪聲強度的上限。它在決定應用的噪聲水平範圍方面起著關鍵作用。 | FLOAT |
| `最小 sigma` | 設定最小 sigma 值，建立噪聲強度的下限。此參數有助於微調噪聲應用的起始點。 | FLOAT |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 根據指數排程生成的 sigma 值序列。這些值用於控制擴散過程中每一步的噪聲水平。 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExponentialScheduler/zh-TW.md)
