> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSampler/zh-TW.md)

## 節點概述

KSampler 的工作原理如下：它根據特定的模型以及正面和負面條件來修改提供的原始潛在圖像資訊。
首先，它根據設定的 **seed** 和 **denoise** 強度向原始圖像資料添加噪聲，然後輸入預設的 **Model** 結合 **positive** 和 **negative** 引導條件來生成圖像。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 預設值 | 範圍/選項 | 描述 |
| ---------------------- | ------------ | -------- | ------- | ------------------------ | ---------------------------------------------------------------------------------- |
| `Model` | CHECKPOINT | 是 | 無 | - | 用於去噪過程的輸入模型 |
| `seed` | INT | 是 | 0 | 0 ~ 18446744073709551615 | 用於生成隨機噪聲，使用相同的 "seed" 會生成相同的圖像 |
| `steps` | INT | 是 | 20 | 1 ~ 10000 | 去噪過程中使用的步數，步數越多結果越精確 |
| `cfg` | FLOAT | 是 | 8.0 | 0.0 ~ 100.0 | 控制生成圖像與輸入條件的匹配程度，建議值為 6-8 |
| `sampler_name` | UI_OPTION | 是 | 無 | 多種演算法 | 選擇用於去噪的取樣器，影響生成速度和風格 |
| `scheduler` | UI_OPTION | 是 | 無 | 多種排程器 | 控制噪聲的移除方式，影響生成過程 |
| `Positive` | CONDITIONING | 是 | 無 | - | 引導去噪的正面條件，即您希望在圖像中出現的內容 |
| `Negative` | CONDITIONING | 是 | 無 | - | 引導去噪的負面條件，即您不希望出現在圖像中的內容 |
| `Latent_Image` | LATENT | 是 | 無 | - | 用於去噪的潛在圖像 |
| `denoise` | FLOAT | 否 | 1.0 | 0.0 ~ 1.0 | 決定噪聲移除比例，較低的值表示與輸入圖像的關聯較少 |
| `control_after_generate` | UI_OPTION | 否 | 無 | Random/Inc/Dec/Keep | 提供在每次提示後更改種子的能力 |

## 輸出結果

| 參數 | 功能 |
| -------------- | ------------------------------------------ |
| `Latent` | 輸出取樣器去噪後的潛在圖像 |

## 原始碼

[更新於 2025年5月15日]

```Python

def common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent, denoise=1.0, disable_noise=False, start_step=None, last_step=None, force_full_denoise=False):
    latent_image = latent["samples"]
    latent_image = comfy.sample.fix_empty_latent_channels(model, latent_image)

    if disable_noise:
        noise = torch.zeros(latent_image.size(), dtype=latent_image.dtype, layout=latent_image.layout, device="cpu")
    else:
        batch_inds = latent["batch_index"] if "batch_index" in latent else None
        noise = comfy.sample.prepare_noise(latent_image, seed, batch_inds)

    noise_mask = None
    if "noise_mask" in latent:
        noise_mask = latent["noise_mask"]

    callback = latent_preview.prepare_callback(model, steps)
    disable_pbar = not comfy.utils.PROGRESS_BAR_ENABLED
    samples = comfy.sample.sample(model, noise, steps, cfg, sampler_name, scheduler, positive, negative, latent_image,
                                  denoise=denoise, disable_noise=disable_noise, start_step=start_step, last_step=last_step,
                                  force_full_denoise=force_full_denoise, noise_mask=noise_mask, callback=callback, disable_pbar=disable_pbar, seed=seed)
    out = latent.copy()
    out["samples"] = samples
    return (out, )
class KSampler:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL", {"tooltip": "The model used for denoising the input latent."}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "control_after_generate": True, "tooltip": "The random seed used for creating the noise."}),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000, "tooltip": "The number of steps used in the denoising process."}),
                "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0, "step":0.1, "round": 0.01, "tooltip": "The Classifier-Free Guidance scale balances creativity and adherence to the prompt. Higher values result in images more closely matching the prompt however too high values will negatively impact quality."}),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS, {"tooltip": "The algorithm used when sampling, this can affect the quality, speed, and style of the generated output."}),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, {"tooltip": "The scheduler controls how noise is gradually removed to form the image."}),
                "positive": ("CONDITIONING", {"tooltip": "The conditioning describing the attributes you want to include in the image."}),
                "negative": ("CONDITIONING", {"tooltip": "The conditioning describing the attributes you want to exclude from the image."}),
                "latent_image": ("LATENT", {"tooltip": "The latent image to denoise."}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01, "tooltip": "The amount of denoising applied, lower values will maintain the structure of the initial image allowing for image to image sampling."}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    OUTPUT_TOOLTIPS = ("The denoised latent.",)
    FUNCTION = "sample"

    CATEGORY = "sampling"
    DESCRIPTION = "Uses the provided model, positive and negative conditioning to denoise the latent image."

    def sample(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=1.0):
        return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)

```