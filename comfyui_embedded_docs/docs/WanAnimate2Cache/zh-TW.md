# WanAnimate2Cache

Caches the pose-video's per-block activations once so they do not need to be recomputed on every sampling step, which roughly halves generation time. The tradeoff is extra memory usage: about 12.5 GB of system RAM at 480x832 resolution with 81 frames in bf16, scaling with resolution and video length.

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要附加快取的 Wan Animate2 模型。 | MODEL | 是 | |
| `device` | 要將快取保存在何處。cpu（RAM）是安全選擇，在典型尺寸下，快取無法與模型一同放入 VRAM。gpu（VRAM）若放得下則可能更快。（預設值："cpu"） | STRING | 是 | "cpu"<br>"gpu" |
| `dtype` | 儲存精度。default 會以模型的計算 dtype 儲存啟用值。int8 將快取減半，int4 將其縮減為四分之一，convrot 用於保持精確度。（預設值："default"） | STRING | 是 | "default"<br>"int8"<br>"int4" |

注意：使用上下文視窗時，每個視窗會分別快取，因此記憶體使用量會隨視窗數量擴增。應使用 static_standard 排程，因為 uniform 排程會在每個步驟移動視窗，導致快取永遠無法重複使用。

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model` | 附加了姿態影片啟用值快取的克隆模型。生成完成時會自動釋放快取。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimate2Cache/zh-TW.md)

---
**Source fingerprint (SHA-256):** `06305432601afd7c797ef29ef4be3f2bb1aa660e05edde270499e94ccdd54f84`
