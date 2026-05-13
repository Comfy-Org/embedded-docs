> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/zh-TW.md)

## 概述

BasicGuider 節點為取樣過程建立一個簡單的引導機制。它接收模型和條件資料作為輸入，並產生一個可用於在取樣過程中引導生成流程的引導器物件。此節點提供了受控生成所需的基本引導功能。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 用於引導的模型 |
| `conditioning` | CONDITIONING | 是 | - | 引導生成過程的條件資料 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | 一個引導器物件，可在取樣過程中使用以引導生成 |

---
**Source fingerprint (SHA-256):** `012171caea6aacfadaabacb746be104ca783ae5ea5834cc4a67088233b835654`
