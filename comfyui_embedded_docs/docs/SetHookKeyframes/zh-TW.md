# 設定 Hook 關鍵影格

## 概述

Set Hook Keyframes 節點允許您對現有的鉤子群組套用關鍵幀排程。它接收一個鉤子群組，並可選擇性地套用關鍵幀時間資訊，以控制在生成過程中不同鉤子的執行時機。當提供關鍵幀時，該節點會複製鉤子群組，並為群組內的所有鉤子設定關鍵幀時間。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `hooks` | 將套用關鍵幀排程的鉤子群組 | HOOKS | 是 | - |
| `hook_kf` | 可選的關鍵幀群組，包含鉤子執行的時間資訊 | HOOK_KEYFRAMES | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `hooks` | 已套用關鍵幀排程的修改後鉤子群組（若提供了關鍵幀則為複製版本） | HOOKS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetHookKeyframes/zh-TW.md)

---
**Source fingerprint (SHA-256):** `48908e5247b18e5b7b1d894c2f1adcf6403e499125b0c3eb05978584b3d5759b`
