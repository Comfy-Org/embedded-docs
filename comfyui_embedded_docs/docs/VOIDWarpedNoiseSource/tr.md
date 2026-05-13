> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/tr.md)

## Genel Bakış

Bu düğüm, bir LATENT'i (VOIDWarpedNoise düğümünün çıktısı gibi) bir NOISE kaynağına dönüştürür. Bu sayede, daha kontrollü görüntü üretimi için çarpıtılmış gürültüyü SamplerCustomAdvanced düğümüyle kullanabilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `warped_noise` | LATENT | Evet | Yok | VOIDWarpedNoise düğümünden gelen çarpıtılmış gürültü latent'i |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `NOISE` | NOISE | SamplerCustomAdvanced ile kullanılabilen bir gürültü kaynağı |

---
**Source fingerprint (SHA-256):** `ff798d223da5cf705a40ad1f36cc403030105331d0cc4173e9553cd3718c5d93`
