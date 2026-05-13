> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/zh-TW.md)

## 概述

ControlNetInpaintingAliMamaApply 節點透過將正向與負向條件化結合控制影像和遮罩，將 ControlNet 條件化應用於修補任務。它處理輸入影像和遮罩，以建立修改後的條件化，引導生成過程，從而精確控制影像中哪些區域需要修補。該節點支援強度調整和時序控制，以便在生成過程的不同階段微調 ControlNet 的影響。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `正向` | CONDITIONING | 是 | - | 引導生成朝向所需內容的正向條件化 |
| `負向` | CONDITIONING | 是 | - | 引導生成遠離不需要內容的負向條件化 |
| `control_net` | CONTROL_NET | 是 | - | 提供對生成過程額外控制的 ControlNet 模型 |
| `vae` | VAE | 是 | - | 用於編碼和解碼影像的 VAE（變分自編碼器） |
| `影像` | IMAGE | 是 | - | 作為 ControlNet 控制引導的輸入影像 |
| `遮罩` | MASK | 是 | - | 定義影像中哪些區域應被修補的遮罩 |
| `強度` | FLOAT | 是 | 0.0 至 10.0 | ControlNet 效果的強度（預設值：1.0） |
| `起始百分比` | FLOAT | 是 | 0.0 至 1.0 | ControlNet 影響在生成過程中開始的起點（以百分比表示）（預設值：0.0） |
| `結束百分比` | FLOAT | 是 | 0.0 至 1.0 | ControlNet 影響在生成過程中結束的終點（以百分比表示）（預設值：1.0） |

**注意：** 當 ControlNet 啟用 `concat_mask` 時，遮罩會被反轉並在處理前應用於影像，且遮罩會包含在發送給 ControlNet 的額外串接資料中。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `負向` | CONDITIONING | 已套用 ControlNet 進行修補的修改後正向條件化 |
| `負向` | CONDITIONING | 已套用 ControlNet 進行修補的修改後負向條件化 |

---
**Source fingerprint (SHA-256):** `30b49991b5ead039122a282fb48e3ed30477f89ce1430c371529bc42f921020d`
