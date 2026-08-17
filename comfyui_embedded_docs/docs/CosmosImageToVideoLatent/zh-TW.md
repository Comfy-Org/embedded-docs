# Cosmos 圖片轉影片潛在編碼

CosmosImageToVideoLatent 節點建立用於影像轉影片生成的影片潛在空間。它從空白潛在空間開始，可選擇性地將起始影像和/或結束影像編碼到影片序列的第一個或最後一個幀。當提供影像時，它也會產生一個雜訊遮罩，將已編碼的幀標記為在生成過程中保持固定。

## 輸入
| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `vae` | 用於將輸入影像編碼到潛在空間的 VAE 模型 | VAE | 是 | - |
| `width` | 輸出影片的寬度（以像素為單位，預設：1280） | INT | 是 | 16 to MAX_RESOLUTION (step 16) |
| `height` | 輸出影片的高度（以像素為單位，預設：704） | INT | 是 | 16 to MAX_RESOLUTION (step 16) |
| `length` | 影片序列中的幀數（預設：121） | INT | 是 | 1 to MAX_RESOLUTION (step 8) |
| `batch_size` | 輸出批次中要生成的影片潛在空間數量（預設：1） | INT | 是 | 1 to 4096 |
| `start_image` | 可選擇性地在影片序列開頭編碼的影像或影像序列 | IMAGE | 否 | - |
| `end_image` | 可選擇性地在影片序列結尾編碼的影像或影像序列 | IMAGE | 否 | - |

**注意：** 當未提供 `start_image` 和 `end_image` 時，節點會回傳沒有雜訊遮罩的空白潛在空間。當至少提供一張影像時，會包含 `noise_mask`：從提供的影像編碼而來的潛在幀其遮罩值為 0（保持固定），而其餘幀的遮罩值為 1（待生成）。影像在編碼前會調整大小至目標 `width` 和 `height`，而取自輸入影像的幀數等於其批次維度，最多為 `length`。潛在空間有 16 個通道，空間維度為 `width / 8` 和 `height / 8`，以及 `((length - 1) // 8) + 1` 個幀。當提供影像時，潛在空間及其雜訊遮罩會重複 `batch_size` 次以形成輸出批次。

## 輸出
| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `latent` | 一個 LATENT，包含影片潛在空間 `samples`，並在提供 `start_image` 或 `end_image` 時，包含一個將已編碼幀標記為固定的 `noise_mask` | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0b06ccfcb14c27c81eeebbbff519da1e187970d4cfc19c8796fc3da20688245c`
