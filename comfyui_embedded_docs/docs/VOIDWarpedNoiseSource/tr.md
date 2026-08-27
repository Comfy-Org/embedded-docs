# VOIDWarpedNoiseSource

## Genel Bakış

Bu düğüm, bir LATENT'i (VOIDWarpedNoise düğümünün çıktısı gibi) bir NOISE kaynağına dönüştürür. Bu, çarpıtılmış gürültüyü SamplerCustomAdvanced düğümüyle kullanarak daha kontrollü görüntü üretimi yapmanızı sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `warped_noise` | VOIDWarpedNoise düğümünden alınan çarpıtılmış gürültü latent'i | LATENT | Evet | N/A |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `NOISE` | SamplerCustomAdvanced ile kullanılabilen bir gürültü kaynağı | NOISE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/tr.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
