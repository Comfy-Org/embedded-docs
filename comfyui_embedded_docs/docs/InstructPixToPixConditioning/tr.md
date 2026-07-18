InstructPixToPixConditioning düğümü, pozitif ve negatif metin yönlendirmelerini görüntü verileriyle birleştirerek InstructPix2Pix görüntü düzenlemesi için koşullandırma verilerini hazırlar. Giriş görüntülerini bir VAE kodlayıcı aracılığıyla işleyerek gizli temsiller oluşturur ve bu gizli temsilleri hem pozitif hem de negatif koşullandırma verilerine ekler. Düğüm, VAE kodlama süreciyle uyumluluk için görüntü boyutlarını 8 pikselin katlarına kırparak otomatik olarak işler.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | İstenen görüntü özellikleri için metin yönlendirmeleri ve ayarları içeren pozitif koşullandırma verileri | CONDITIONING | Evet | - |
| `negatif` | İstenmeyen görüntü özellikleri için metin yönlendirmeleri ve ayarları içeren negatif koşullandırma verileri | CONDITIONING | Evet | - |
| `vae` | Giriş görüntülerini gizli temsillere kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `pikseller` | İşlenecek ve gizli uzaya kodlanacak giriş görüntüsü | IMAGE | Evet | - |

**Not:** Giriş görüntüsü boyutları, VAE kodlama süreciyle uyumluluğu sağlamak için genişlik ve yükseklikte en yakın 8 piksel katına kırpılarak otomatik olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Eklenmiş gizli görüntü temsili ile pozitif koşullandırma verileri | CONDITIONING |
| `negatif` | Eklenmiş gizli görüntü temsili ile negatif koşullandırma verileri | CONDITIONING |
| `gizli` | Kodlanmış görüntü ile aynı boyutlara sahip boş gizli tensör | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `4b2383c9d64efdb558758359bf544fc5a1be65c12b23b54152e2df79a6dd8d79`
