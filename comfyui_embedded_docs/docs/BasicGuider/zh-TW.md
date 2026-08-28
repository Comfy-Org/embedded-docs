# 基礎引導器

BasicGuider 節點為採樣過程建立了一個簡單的引導機制。它接收模型和條件資料作為輸入，並產生一個可在採樣期間用於引導生成過程的引導器物件。此節點提供了受控生成所需的基本引導功能。

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於引導的模型 | MODEL | 是 | - |
| `條件設定` | 引導生成過程的條件資料 | CONDITIONING | 是 | - |

## 輸出
| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `GUIDER` | 一個可用於採樣過程中引導生成的引導器物件 | GUIDER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8ea6b56be58ae99baaf13a04c4fadbf8ad921801d8f2ce2aecce768cc34a3b20`
