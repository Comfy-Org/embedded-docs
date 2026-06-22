# 載入影格插值模型

## 概述

此節點從檔案載入影格插值模型，並將其準備好用於工作流程中。它會自動偵測模型類型（FILM 或 RIFE），並根據您的硬體配置模型以達到最佳效能。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型名稱` | 選擇要載入的影格插值模型。模型必須放置在 'frame_interpolation' 資料夾中。 | STRING | 是 | `frame_interpolation` 資料夾中的模型檔案列表 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | 已載入並配置完成的影格插值模型，可直接用於其他節點。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `497c20d5123bcbfd321dc4a659250ce3e0903e55c3a0274d3ed45710d75573d9`
