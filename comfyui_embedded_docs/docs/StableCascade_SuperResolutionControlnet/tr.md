StableCascade_SuperResolutionControlnet düğümü, Stable Cascade süper çözünürlük işleme için girdileri hazırlar. Bir girdi görüntüsünü alır ve bir VAE kullanarak kodlayarak controlnet girdisi oluşturur; aynı zamanda Stable Cascade hattının C aşaması ve B aşaması için yer tutucu gizil temsiller üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Süper çözünürlük için işlenecek girdi görüntüsü | IMAGE | Evet | - |
| `vae` | Girdi görüntüsünü kodlamak için kullanılan VAE modeli | VAE | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `kontrol_ağı_girişi` | Controlnet girdisi için uygun kodlanmış görüntü temsili | IMAGE |
| `aşama_c` | Stable Cascade işleminin C aşaması için yer tutucu gizil temsil | LATENT |
| `aşama_b` | Stable Cascade işleminin B aşaması için yer tutucu gizil temsil | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/tr.md)

---
**Source fingerprint (SHA-256):** `78b6e5a02c48ac37a205ef9d8532a3aca19134de4ec7be98b2ee55969dab7b53`
