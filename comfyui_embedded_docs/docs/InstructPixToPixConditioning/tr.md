> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/tr.md)

InstructPixToPixConditioning düğümü, pozitif ve negatif metin yönlendirmelerini görüntü verileriyle birleştirerek InstructPix2Pix görüntü düzenlemesi için koşullandırma verilerini hazırlar. Giriş görüntülerini bir VAE kodlayıcı aracılığıyla işleyerek gizli temsiller oluşturur ve bu gizli temsilleri hem pozitif hem de negatif koşullandırma verilerine ekler. Düğüm, VAE kodlama süreciyle uyumluluk için görüntü boyutlarını 8 pikselin katlarına kırparak otomatik olarak işler.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `pozitif` | CONDITIONING | Evet | - | İstenen görüntü özellikleri için metin yönlendirmeleri ve ayarları içeren pozitif koşullandırma verileri |
| `negatif` | CONDITIONING | Evet | - | İstenmeyen görüntü özellikleri için metin yönlendirmeleri ve ayarları içeren negatif koşullandırma verileri |
| `vae` | VAE | Evet | - | Giriş görüntülerini gizli temsillere kodlamak için kullanılan VAE modeli |
| `pikseller` | IMAGE | Evet | - | İşlenecek ve gizli uzaya kodlanacak giriş görüntüsü |

**Not:** Giriş görüntüsü boyutları, VAE kodlama süreciyle uyumluluğu sağlamak için genişlik ve yükseklikte en yakın 8 piksel katına kırpılarak otomatik olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `negatif` | CONDITIONING | Eklenmiş gizli görüntü temsili ile pozitif koşullandırma verileri |
| `gizli` | CONDITIONING | Eklenmiş gizli görüntü temsili ile negatif koşullandırma verileri |
| `latent` | LATENT | Kodlanmış görüntü ile aynı boyutlara sahip boş gizli tensör |

---
**Source fingerprint (SHA-256):** `4b2383c9d64efdb558758359bf544fc5a1be65c12b23b54152e2df79a6dd8d79`
