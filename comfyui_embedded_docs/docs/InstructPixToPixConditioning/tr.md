# InstructPixToPixKoşullandırma

InstructPixToPixConditioning düğümü, pozitif ve negatif metin istemlerini görüntü verileriyle birleştirerek InstructPix2Pix görüntü düzenleme için koşullandırma verilerini hazırlar. Girdi görüntüsünü bir VAE aracılığıyla latent temsile kodlar ve bu latentı hem pozitif hem de negatif koşullandırmaya ekler; ayrıca eşleşen boş bir latent döndürür. Görüntü boyutları, VAE'nin işleyebilmesi için otomatik olarak 8 pikselin katlarına kırpılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | İstenen görüntü özellikleri için metin istemlerini ve ayarları içeren pozitif koşullandırma verisi | CONDITIONING | Evet | - |
| `negative` | İstenmeyen görüntü özellikleri için metin istemlerini ve ayarları içeren negatif koşullandırma verisi | CONDITIONING | Evet | - |
| `vae` | Girdi görüntülerini latent temsillere kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `pixels` | Latent uzayına işlenecek ve kodlanacak girdi görüntüsü | IMAGE | Evet | - |

**Not:** Girdi görüntü boyutları, VAE kodlama süreciyle uyumluluğu sağlamak için hem genişlik hem de yükseklikte 8 pikselin katlarına merkezden kırpılarak otomatik olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Kodlanmış görüntü latentı `concat_latent_image` olarak eklenmiş pozitif koşullandırma verisi | CONDITIONING |
| `negative` | Kodlanmış görüntü latentı `concat_latent_image` olarak eklenmiş negatif koşullandırma verisi | CONDITIONING |
| `latent` | Kodlanmış görüntüyle aynı boyutlara sahip sıfırlardan oluşan latent tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
