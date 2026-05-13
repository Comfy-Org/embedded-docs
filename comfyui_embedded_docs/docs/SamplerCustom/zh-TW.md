> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustom/zh-TW.md)

SamplerCustom 節點旨在為各種應用提供靈活且可自訂的取樣機制。它讓使用者能夠根據特定需求選擇和配置不同的取樣策略，從而提升取樣過程的適應性與效率。

## 輸入

| 參數 | 資料類型 | 說明 |
|-----------|--------------|-------------|
| `model` | `MODEL` | 'model' 輸入類型指定用於取樣的模型，在決定取樣行為與輸出結果中扮演關鍵角色。 |
| `add_noise` | `BOOLEAN` | 'add_noise' 輸入類型允許使用者指定是否在取樣過程中添加雜訊，這會影響生成樣本的多樣性與特性。 |
| `noise_seed` | `INT` | 'noise_seed' 輸入類型為雜訊生成提供一個種子值，確保在添加雜訊時取樣過程的可重複性與一致性。 |
| `cfg` | `FLOAT` | 'cfg' 輸入類型設定取樣過程的配置，允許對取樣參數與行為進行微調。 |
| `positive` | `CONDITIONING` | 'positive' 輸入類型代表正向條件資訊，引導取樣過程朝向生成符合指定正向屬性的樣本。 |
| `negative` | `CONDITIONING` | 'negative' 輸入類型代表負向條件資訊，引導取樣過程遠離生成具有指定負向屬性的樣本。 |
| `sampler` | `SAMPLER` | 'sampler' 輸入類型選擇要採用的特定取樣策略，直接影響生成樣本的性質與品質。 |
| `sigmas` | `SIGMAS` | 'sigmas' 輸入類型定義取樣過程中使用的雜訊級別，影響樣本空間的探索程度與輸出的多樣性。 |
| `latent_image` | `LATENT` | 'latent_image' 輸入類型為取樣過程提供初始的潛在影像，作為樣本生成的起點。 |

## 輸出

| 參數 | 資料類型 | 說明 |
|-----------|--------------|-------------|
| `output` | `LATENT` | 'output' 代表取樣過程的主要結果，包含生成的樣本。 |
| `denoised_output` | `LATENT` | 'denoised_output' 代表經過降噪處理後的樣本，可能提升生成樣本的清晰度與品質。 |