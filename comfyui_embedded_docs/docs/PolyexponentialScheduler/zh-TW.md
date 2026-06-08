PolyexponentialScheduler 節點旨在根據多指數噪聲調度生成一系列噪聲級別（sigma）。此調度是 sigma 對數的多項式函數，允許在擴散過程中實現靈活且可自訂的噪聲級別進程。

## 輸入

| 參數 | 描述 | 資料類型 |
| --- | --- | --- |
| `步驟數` | 指定擴散過程中的步驟數，影響生成噪聲級別的粒度。 | INT |
| `最大 sigma` | 最大噪聲級別，設定噪聲調度的上限。 | FLOAT |
| `最小 sigma` | 最小噪聲級別，設定噪聲調度的下限。 | FLOAT |
| `rho` | 控制多指數噪聲調度形狀的參數，影響噪聲級別在最小值與最大值之間的進程方式。 | FLOAT |

## 輸出

| 參數 | 描述 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 輸出是根據指定的多指數噪聲調度量身定制的一系列噪聲級別（sigma）。 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PolyexponentialScheduler/zh-TW.md)
