# KSampler

KSampler 的運作方式如下：它根據指定的模型以及正向與負向條件，來修改所提供的原始潛在影像資訊。
首先，它會根據設定的 **seed** 和 **denoise** 強度，將雜訊添加到原始影像資料中，然後輸入預設的 **Model** 以及 **positive** 和 **negative** 引導條件來生成影像。

## 輸入

| 參數名稱 | 說明 | 資料類型 | 必要 | 預設值 | 範圍/選項 |
| --- | --- | --- | --- | --- | --- |
| Model | 用於去噪過程的輸入模型 | checkpoint | 是 | 無 | - |
| seed | 用於生成隨機雜訊，使用相同的「seed」會生成完全相同的影像 | Int | 是 | 0 | 0 ~ 18446744073709551615 |
| steps | 去噪過程中使用的步數，步數越多結果越精確 | Int | 是 | 20 | 1 ~ 10000 |
| cfg | 控制生成影像與輸入條件的符合程度，建議值為 6-8 | float | 是 | 8.0 | 0.0 ~ 100.0 |
| sampler_name | 選擇用於去噪的取樣器，會影響生成速度與風格 | UI Option | 是 | 無 | 多種演算法 |
| scheduler | 控制雜訊的移除方式，影響生成過程 | UI Option | 是 | 無 | 多種排程器 |
| Positive | 引導去噪的正向條件，即你希望影像中出現的內容 | conditioning | 是 | 無 | - |
| Negative | 引導去噪的負向條件，即你不希望影像中出現的內容 | conditioning | 是 | 無 | - |
| Latent_Image | 用於去噪的潛在影像 | Latent | 是 | 無 | - |
| denoise | 決定雜訊移除的比例，數值越低表示與輸入影像的關聯性越低 | float | 否 | 1.0 | 0.0 ~ 1.0 |
| control_after_generate | 提供在每次提示後更改 seed 的能力 | UI Option | 否 | 無 | Random/Inc/Dec/Keep |

## 輸出

| 參數 | 功能 |
| -------------- | ------------------------------------------ |
| Latent         | 輸出取樣器去噪後的潛在資料 |

## 原始碼

[更新於 2025 年 5 月 15 日]

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
                "model": ("MODEL", {"tooltip": "用於對輸入潛在影像進行去噪的模型。"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "control_after_generate": True, "tooltip": "用於創建雜訊的隨機種子。"}),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000, "tooltip": "去噪過程中使用的步數。"}),
                "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0, "step":0.1, "round": 0.01, "tooltip": "無分類器引導尺度，用於平衡創造力與對提示的遵循程度。數值越高，生成的影像越符合提示，但過高會對品質產生負面影響。"}),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS, {"tooltip": "取樣時使用的演算法，會影響生成輸出的品質、速度和風格。"}),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, {"tooltip": "排程器控制如何逐步移除雜訊以形成影像。"}),
                "positive": ("CONDITIONING", {"tooltip": "描述你希望影像中包含的屬性的條件。"}),
                "negative": ("CONDITIONING", {"tooltip": "描述你希望從影像中排除的屬性的條件。"}),
                "latent_image": ("LATENT", {"tooltip": "要進行去噪的潛在影像。"}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01, "tooltip": "應用的去噪量，較低的值將保持初始影像的結構，允許進行影像到影像的取樣。"}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    OUTPUT_TOOLTIPS = ("去噪後的潛在資料。",)
    FUNCTION = "sample"

    CATEGORY = "sampling"
    DESCRIPTION = "使用提供的模型、正向和負向條件對潛在影像進行去噪。"

    def sample(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=1.0):
        return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)

```

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSampler/zh-TW.md)
