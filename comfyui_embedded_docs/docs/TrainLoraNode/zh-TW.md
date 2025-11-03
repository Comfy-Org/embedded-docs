> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/zh-TW.md)

TrainLoraNode 使用提供的潛空間資料和條件化資料，在擴散模型上建立並訓練 LoRA（低秩適應）模型。它允許您使用自訂的訓練參數、優化器和損失函數來微調模型。該節點輸出應用 LoRA 後的已訓練模型、LoRA 權重、訓練損失指標以及完成的總訓練步數。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要訓練 LoRA 的基礎模型。 |
| `latents` | LATENT | 是 | - | 用於訓練的潛空間資料，作為模型的資料集/輸入。 |
| `positive` | CONDITIONING | 是 | - | 用於訓練的正向條件化資料。 |
| `batch_size` | INT | 是 | 1-10000 | 訓練時使用的批次大小（預設值：1）。 |
| `grad_accumulation_steps` | INT | 是 | 1-1024 | 訓練時使用的梯度累積步數（預設值：1）。 |
| `steps` | INT | 是 | 1-100000 | 訓練 LoRA 的步數（預設值：16）。 |
| `learning_rate` | FLOAT | 是 | 0.0000001-1.0 | 訓練時使用的學習率（預設值：0.0005）。 |
| `rank` | INT | 是 | 1-128 | LoRA 層的秩（預設值：8）。 |
| `optimizer` | COMBO | 是 | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" | 訓練時使用的優化器（預設值："AdamW"）。 |
| `loss_function` | COMBO | 是 | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" | 訓練時使用的損失函數（預設值："MSE"）。 |
| `seed` | INT | 是 | 0-18446744073709551615 | 訓練時使用的種子（用於 LoRA 權重初始化和噪聲採樣的生成器）（預設值：0）。 |
| `training_dtype` | COMBO | 是 | "bf16"<br>"fp32" | 訓練時使用的資料類型（預設值："bf16"）。 |
| `lora_dtype` | COMBO | 是 | "bf16"<br>"fp32" | LoRA 使用的資料類型（預設值："bf16"）。 |
| `algorithm` | COMBO | 是 | 多個選項可用 | 訓練時使用的演算法。 |
| `gradient_checkpointing` | BOOLEAN | 是 | - | 訓練時是否使用梯度檢查點（預設值：True）。 |
| `existing_lora` | COMBO | 是 | 多個選項可用 | 要附加到的現有 LoRA。設定為 None 以建立新的 LoRA（預設值："[None]"）。 |

**注意：** 正向條件化輸入的數量必須與潛空間影像的數量相符。如果只提供一個正向條件化但有多個影像，該條件化將自動重複應用於所有影像。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model_with_lora` | MODEL | 應用已訓練 LoRA 後的原始模型。 |
| `lora` | LORA_MODEL | 已訓練的 LoRA 權重，可儲存或應用於其他模型。 |
| `loss` | LOSS_MAP | 包含隨時間變化的訓練損失值的字典。 |
| `steps` | INT | 完成的總訓練步數（包括現有 LoRA 的任何先前步數）。 |