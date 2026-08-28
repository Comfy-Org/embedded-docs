# InstructPixToPixKoşullandırma

InstructPixToPixConditioning düğümü, pozitif ve negatif metin istemlerini görüntü verileriyle birleştirerek InstructPix2Pix görüntü düzenleme için koşullandırma verileri hazırlar. Giriş görüntülerini bir VAE kodlayıcı aracılığıyla işleyerek latent temsiller oluşturur ve bu latentleri hem pozitif hem de negatif koşullandırma verilerine ekler. Düğüm, VAE kodlama süreciyle uyumluluk için görüntü boyutlarını 8 pikselin katlarına kırparak otomatik olarak yönetir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | İstenen görüntü özellikleri için metin istemleri ve ayarlarını içeren pozitif koşullandırma verileri | CONDITIONING | Evet | - |
| `negatif` | İstenmeyen görüntü özellikleri için metin istemleri ve ayarlarını içeren negatif koşullandırma verileri | CONDITIONING | Evet | - |
| `vae` | Giriş görüntülerini latent temsillere kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `pikseller` | İşlenecek ve latent uzaya kodlanacak giriş görüntüsü | IMAGE | Evet | - |

**Not:** Giriş görüntüsünün boyutları, VAE kodlama süreciyle uyumluluğu sağlamak amacıyla hem genişlik hem de yükseklikte merkezden kırpılarak otomatik olarak 8 pikselin katlarına ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Üzerine latent görüntü temsili eklenmiş pozitif koşullandırma verileri | CONDITIONING |
| `negatif` | Üzerine latent görüntü temsili eklenmiş negatif koşullandırma verileri | CONDITIONING |
| `gizli` | Kodlanmış görüntüyle aynı boyutlara sahip boş latent tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
