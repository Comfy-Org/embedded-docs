> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/tr.md)

StableCascade_SuperResolutionControlnet düğümü, Stable Cascade süper çözünürlük işleme için girdileri hazırlar. Bir girdi görüntüsünü alır ve bir VAE kullanarak kodlayarak controlnet girdisi oluşturur; aynı zamanda Stable Cascade hattının C aşaması ve B aşaması için yer tutucu gizil temsiller üretir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `görüntü` | IMAGE | Evet | - | Süper çözünürlük için işlenecek girdi görüntüsü |
| `vae` | VAE | Evet | - | Girdi görüntüsünü kodlamak için kullanılan VAE modeli |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `aşama_c` | IMAGE | Controlnet girdisi için uygun kodlanmış görüntü temsili |
| `aşama_b` | LATENT | Stable Cascade işleminin C aşaması için yer tutucu gizil temsil |
| `stage_b` | LATENT | Stable Cascade işleminin B aşaması için yer tutucu gizil temsil |

---
**Source fingerprint (SHA-256):** `78b6e5a02c48ac37a205ef9d8532a3aca19134de4ec7be98b2ee55969dab7b53`
