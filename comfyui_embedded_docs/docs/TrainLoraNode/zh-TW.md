> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/zh-TW.md)

## 概述

TrainLoraNode 會使用提供的潛在變數與條件化資料，在擴散模型上建立並訓練 LoRA（低秩適應）模型。它讓您能夠透過自訂的訓練參數、優化器和損失函數來微調模型。此節點會輸出訓練完成的 LoRA 權重、損失歷史記錄圖，以及總共完成的訓練步數。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要訓練 LoRA 的模型。 |
| `latents` | LATENT | 是 | - | 用於訓練的潛在變數，作為模型的資料集/輸入。 |
| `positive` | CONDITIONING | 是 | - | 用於訓練的正向條件化。 |
| `batch_size` | INT | 是 | 1-10000 | 訓練使用的批次大小（預設值：1）。 |
| `grad_accumulation_steps` | INT | 是 | 1-1024 | 訓練使用的梯度累積步數（預設值：1）。 |
| `steps` | INT | 是 | 1-100000 | 訓練 LoRA 的步數（預設值：16）。 |
| `learning_rate` | FLOAT | 是 | 0.0000001-1.0 | 訓練使用的學習率（預設值：0.0005）。 |
| `rank` | INT | 是 | 1-128 | LoRA 層的秩（預設值：8）。 |
| `optimizer` | COMBO | 是 | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" | 訓練使用的優化器（預設值："AdamW"）。 |
| `loss_function` | COMBO | 是 | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" | 訓練使用的損失函數（預設值："MSE"）。 |
| `seed` | INT | 是 | 0-18446744073709551615 | 訓練使用的種子（用於 LoRA 權重初始化和雜訊取樣的生成器）（預設值：0）。 |
| `training_dtype` | COMBO | 是 | "bf16"<br>"fp32"<br>"none" | 訓練使用的資料類型。'none' 會保留模型原生的計算資料類型，而不會覆蓋它。對於 fp16 模型，會自動啟用 GradScaler（預設值："bf16"）。 |
| `lora_dtype` | COMBO | 是 | "bf16"<br>"fp32" | LoRA 使用的資料類型（預設值："bf16"）。 |
| `quantized_backward` | BOOLEAN | 是 | - | 當使用 `training_dtype` 為 'none' 且在量化模型上訓練時，啟用後會在反向傳播中使用量化矩陣乘法（預設值：False）。 |
| `algorithm` | COMBO | 是 | 提供多個選項 | 訓練使用的演算法。 |
| `gradient_checkpointing` | BOOLEAN | 是 | - | 訓練時使用梯度檢查點（預設值：True）。 |
| `checkpoint_depth` | INT | 是 | 1-5 | 梯度檢查點的深度層級（預設值：1）。 |
| `offloading` | BOOLEAN | 是 | - | 訓練期間將模型權重卸載到 CPU 以節省 GPU 記憶體（預設值：False）。 |
| `existing_lora` | COMBO | 是 | 提供多個選項 | 要附加到的現有 LoRA。設定為 None 以建立新的 LoRA（預設值："[None]"）。 |
| `bucket_mode` | BOOLEAN | 是 | - | 啟用解析度分桶模式。啟用後，預期來自 ResolutionBucket 節點的預分桶潛在變數（預設值：False）。 |
| `bypass_mode` | BOOLEAN | 是 | - | 啟用訓練的旁路模式。啟用後，適配器會透過前向鉤子（forward hooks）應用，而不是修改權重。這對於無法直接修改權重的量化模型特別有用（預設值：False）。 |

**注意：** 正向條件化輸入的數量必須與潛在影像的數量相符。如果只提供一個正向條件化但有多張影像，它會自動對所有影像重複使用。

**關於 `training_dtype` 的注意事項：** 當設定為 "none" 時，會保留模型原生的計算資料類型。對於 fp16 模型，會自動啟用 GradScaler 以防止梯度計算時發生下溢。如果同時啟用了 `fp16_accumulation`（透過 `--fast` 標誌），這種組合可能在數值上不穩定，並可能導致 NaN 值。

**關於 `quantized_backward` 的注意事項：** 此參數僅在 `training_dtype` 設定為 "none" 且模型為量化模型時才有關聯。它會在反向傳播過程中啟用量化矩陣乘法。

**關於 `bypass_mode` 的注意事項：** 啟用後，適配器會透過前向鉤子（forward hooks）應用，而不是直接修改模型權重。這對於無法直接修改權重的量化模型特別有用。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `lora` | LORA_MODEL | 訓練完成的 LoRA 權重，可以儲存或應用於其他模型。 |
| `loss_map` | LOSS_MAP | 一個字典，包含隨時間變化的訓練損失值。 |
| `steps` | INT | 總共完成的訓練步數（包括來自現有 LoRA 的任何先前步數）。 |

---
**Source fingerprint (SHA-256):** `df315ef416ff3ce81e6a526af2c4e5115980e6c35830825967e7189d4f8541d8`
