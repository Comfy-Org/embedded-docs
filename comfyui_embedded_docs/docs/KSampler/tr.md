# KSampler

KSampler şu şekilde çalışır: Belirtilen modele ve hem pozitif hem de negatif koşullara dayanarak sağlanan orijinal gizli (latent) görüntü bilgisini değiştirir.
İlk olarak, belirlenen **seed** (tohum) ve **denoise** (gürültü giderme) gücüne göre orijinal görüntü verisine gürültü ekler, ardından önceden ayarlanmış **Model**'i **pozitif** ve **negatif** yönlendirme koşullarıyla birleştirerek görüntüyü oluşturur.

## Girişler

| Parametre Adı | Açıklama | Veri Türü | Zorunlu | Varsayılan | Aralık/Seçenekler |
| --- | --- | --- | --- | --- | --- |
| Model | Gürültü giderme işlemi için kullanılan giriş modeli | checkpoint | Evet | Yok | - |
| seed | Rastgele gürültü oluşturmak için kullanılır, aynı "seed" aynı görüntüleri üretir | INT | Evet | 0 | 0 ~ 18446744073709551615 |
| steps | Gürültü giderme işleminde kullanılacak adım sayısı, daha fazla adım daha doğru sonuç | INT | Evet | 20 | 1 ~ 10000 |
| cfg | Oluşturulan görüntünün giriş koşullarına ne kadar yakın olacağını kontrol eder, 6-8 önerilir | FLOAT | Evet | 8.0 | 0.0 ~ 100.0 |
| sampler_name | Gürültü giderme için örnekleyici seçin, üretim hızını ve stilini etkiler | UI Seçeneği | Evet | Yok | Birden çok algoritma |
| scheduler | Gürültünün nasıl kaldırılacağını kontrol eder, üretim sürecini etkiler | UI Seçeneği | Evet | Yok | Birden çok zamanlayıcı |
| Positive | Gürültü gidermeyi yönlendiren pozitif koşullar, görüntüde görmek istedikleriniz | conditioning | Evet | Yok | - |
| Negative | Gürültü gidermeyi yönlendiren negatif koşullar, görüntüde istemedikleriniz | conditioning | Evet | Yok | - |
| Latent_Image | Gürültü giderme için kullanılan gizli (latent) görüntü | Latent | Evet | Yok | - |
| denoise | Gürültü giderme oranını belirler, düşük değerler giriş görüntüsüyle daha az bağlantı | FLOAT | Hayır | 1.0 | 0.0 ~ 1.0 |
| control_after_generate | Her istemden sonra seed'i değiştirme imkanı sağlar | UI Seçeneği | Hayır | Yok | Rastgele/Artır/Azalt/Sabit |

## Çıktı

| Parametre | İşlev                                              |
| -------------- | -------------------------------------------------- |
| Latent         | Örnekleyici gürültü giderme işleminden sonra gizli (latent) çıktıyı verir |

## Kaynak Kodu

[15 Mayıs 2025'te Güncellendi]

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
                "model": ("MODEL", {"tooltip": "Giriş gizli (latent) görüntüsünün gürültüsünü gidermek için kullanılan model."}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "control_after_generate": True, "tooltip": "Gürültü oluşturmak için kullanılan rastgele tohum (seed)."}),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000, "tooltip": "Gürültü giderme işleminde kullanılan adım sayısı."}),
                "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0, "step":0.1, "round": 0.01, "tooltip": "Sınıflandırıcısız Kılavuzluk (CFG) ölçeği, yaratıcılık ile isteme bağlılık arasındaki dengeyi sağlar. Daha yüksek değerler, görüntülerin istemle daha yakından eşleşmesini sağlar ancak çok yüksek değerler kaliteyi olumsuz etkileyebilir."}),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS, {"tooltip": "Örnekleme sırasında kullanılan algoritma, oluşturulan çıktının kalitesini, hızını ve stilini etkileyebilir."}),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, {"tooltip": "Zamanlayıcı, görüntüyü oluşturmak için gürültünün kademeli olarak nasıl kaldırılacağını kontrol eder."}),
                "positive": ("CONDITIONING", {"tooltip": "Görüntüye dahil etmek istediğiniz nitelikleri tanımlayan koşullandırma."}),
                "negative": ("CONDITIONING", {"tooltip": "Görüntüden çıkarmak istediğiniz nitelikleri tanımlayan koşullandırma."}),
                "latent_image": ("LATENT", {"tooltip": "Gürültüsü giderilecek gizli (latent) görüntü."}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01, "tooltip": "Uygulanan gürültü giderme miktarı, daha düşük değerler ilk görüntünün yapısını koruyarak görüntüden görüntüye örneklemeye olanak tanır."}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    OUTPUT_TOOLTIPS = ("Gürültüsü giderilmiş gizli (latent) görüntü.",)
    FUNCTION = "sample"

    CATEGORY = "sampling"
    DESCRIPTION = "Gizli (latent) görüntünün gürültüsünü gidermek için sağlanan modeli, pozitif ve negatif koşullandırmayı kullanır."

    def sample(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=1.0):
        return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)

```

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSampler/tr.md)
