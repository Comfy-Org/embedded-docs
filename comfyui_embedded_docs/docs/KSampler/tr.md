> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSampler/tr.md)

KSampler şu şekilde çalışır: sağlanan orijinal gizli görüntü bilgisini belirli bir model ve hem pozitif hem de negatif koşullara dayanarak değiştirir.
İlk olarak, ayarlanan **seed** ve **denoise strength** değerlerine göre orijinal görüntü verisine gürültü ekler, ardından önceden ayarlanmış **Model**'i **pozitif** ve **negatif** yönlendirme koşullarıyla birleştirerek görüntüyü oluşturmak için kullanır.

## Girdiler

| Parametre Adı          | Veri Türü    | Zorunlu  | Varsayılan | Aralık/Seçenekler         | Açıklama                                                                           |
| ---------------------- | ------------ | -------- | ------- | ------------------------ | ---------------------------------------------------------------------------------- |
| Model                  | checkpoint   | Evet     | Yok     | -                        | Gürültü giderme işlemi için kullanılan giriş modeli                                |
| seed                   | Int          | Evet     | 0       | 0 ~ 18446744073709551615 | Rastgele gürültü oluşturmak için kullanılır, aynı "seed" değeri aynı görüntüleri üretir |
| steps                  | Int          | Evet     | 20      | 1 ~ 10000                | Gürültü giderme işleminde kullanılacak adım sayısı, daha fazla adım daha doğru sonuçlar anlamına gelir |
| cfg                    | float        | Evet     | 8.0     | 0.0 ~ 100.0              | Oluşturulan görüntünün giriş koşullarına ne kadar yakın eşleşeceğini kontrol eder, 6-8 önerilir |
| sampler_name           | UI Option    | Evet     | Yok     | Çoklu algoritmalar       | Gürültü giderme için örnekleyici seçin, üretim hızını ve stilini etkiler           |
| scheduler              | UI Option    | Evet     | Yok     | Çoklu planlayıcılar      | Gürültünün nasıl kaldırılacağını kontrol eder, üretim sürecini etkiler             |
| Positive               | conditioning | Evet     | Yok     | -                        | Gürültü gidermeyi yönlendiren pozitif koşullar, görüntüde görünmesini istediğiniz öğeler |
| Negative               | conditioning | Evet     | Yok     | -                        | Gürültü gidermeyi yönlendiren negatif koşullar, görüntüde olmasını istemediğiniz öğeler |
| Latent_Image           | Latent       | Evet     | Yok     | -                        | Gürültü giderme için kullanılan gizli görüntü                                       |
| denoise                | float        | Hayır    | 1.0     | 0.0 ~ 1.0                | Gürültü kaldırma oranını belirler, düşük değerler giriş görüntüsüyle daha az bağlantı anlamına gelir |
| control_after_generate | UI Option    | Hayır    | Yok     | Rastgele/Artır/Azalt/Koru | Her prompt sonrasında seed değerini değiştirme yeteneği sağlar                     |

## Çıktı

| Parametre | İşlev                                   |
| -------------- | ------------------------------------------ |
| Latent         | Örnekleyici gürültü gidermesinden sonraki gizli çıktıyı verir |

## Kaynak Kodu

[15 Mayıs 2025 tarihinde güncellendi]

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