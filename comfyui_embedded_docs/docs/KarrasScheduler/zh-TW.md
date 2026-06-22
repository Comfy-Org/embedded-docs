# Karras 排程器

KarrasScheduler 節點旨在根據 Karras 等人（2022 年）提出的噪聲調度生成一系列噪聲級別（sigmas）。此調度器對於控制生成模型中的擴散過程非常有用，可對生成過程中每一步應用的噪聲級別進行精細調整。

## 輸入

| 參數 | 描述 | 資料類型 |
| --- | --- | --- |
| `步驟數` | 指定噪聲調度中的步數，影響生成的 sigmas 序列的粒度。 | INT |
| `最大 sigma` | 噪聲調度中的最大 sigma 值，設定噪聲級別的上限。 | FLOAT |
| `最小 sigma` | 噪聲調度中的最小 sigma 值，設定噪聲級別的下限。 | FLOAT |
| `rho` | 控制噪聲調度曲線形狀的參數，影響噪聲級別從 sigma_min 到 sigma_max 的進展方式。 | FLOAT |

## 輸出

| 參數 | 描述 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 根據 Karras 等人（2022 年）噪聲調度生成的噪聲級別（sigmas）序列。 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KarrasScheduler/zh-TW.md)
