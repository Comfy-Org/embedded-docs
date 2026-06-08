## 概述

LatentBlend 節點透過使用指定的混合因子將兩個潛在樣本混合在一起。它接收兩個潛在輸入，並建立一個新的輸出，其中第一個樣本由混合因子加權，第二個樣本則由反向因子加權。如果輸入樣本具有不同的形狀，第二個樣本會自動調整大小以符合第一個樣本的尺寸。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `samples1` | 要混合的第一個潛在樣本 | LATENT | 是 | - |
| `samples2` | 要混合的第二個潛在樣本 | LATENT | 是 | - |
| `混合係數` | 控制兩個樣本之間的混合比例（預設值：0.5） | FLOAT | 是 | 0 到 1 |

**注意：** 如果 `samples1` 和 `samples2` 具有不同的形狀，`samples2` 將使用雙三次插值搭配中心裁切，自動調整大小以符合 `samples1` 的尺寸。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `latent` | 結合兩個輸入樣本的混合潛在樣本 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBlend/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a19808c5b606a8c05f2685fcd78d9f08c1ba51613a4029b36cf0ce5305618c2f`
