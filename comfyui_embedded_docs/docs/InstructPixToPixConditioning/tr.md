> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/tr.md)

InstructPixToPixConditioning düğümü, pozitif ve negatif metin prompt'larını görüntü verileriyle birleştirerek InstructPix2Pix görüntü düzenleme için conditioning verilerini hazırlar. Girdi görüntülerini bir VAE kodlayıcı üzerinden işleyerek latent temsiller oluşturur ve bu latent'leri hem pozitif hem de negatif conditioning verilerine ekler. Düğüm, VAE kodlama işlemiyle uyumluluk sağlamak için görüntü boyutlarını otomatik olarak 8 pikselin katlarına kırparak işler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | - | İstenen görüntü özellikleri için metin prompt'ları ve ayarları içeren pozitif conditioning verisi |
| `negatif` | CONDITIONING | Evet | - | İstenmeyen görüntü özellikleri için metin prompt'ları ve ayarları içeren negatif conditioning verisi |
| `vae` | VAE | Evet | - | Girdi görüntülerini latent temsillere kodlamak için kullanılan VAE modeli |
| `pikseller` | IMAGE | Evet | - | İşlenecek ve latent uzaya kodlanacak girdi görüntüsü |

**Not:** Girdi görüntüsünün boyutları, VAE kodlama işlemiyle uyumluluğu sağlamak için hem genişlik hem de yükseklikte otomatik olarak en yakın 8 piksel katına kırparak ayarlanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | Ekli latent görüntü temsili içeren pozitif conditioning verisi |
| `gizli` | CONDITIONING | Ekli latent görüntü temsili içeren negatif conditioning verisi |
| `latent` | LATENT | Kodlanmış görüntüyle aynı boyutlara sahip boş latent tensör |