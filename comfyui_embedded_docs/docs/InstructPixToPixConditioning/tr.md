# InstructPixToPixKoşullandırma

InstructPixToPixConditioning düğümü, bir girdi görüntüsünü pozitif ve negatif metin istemi koşullandırmasıyla birleştirerek InstructPix2Pix görüntü düzenleme için koşullandırma verilerini hazırlar. Görüntüyü VAE ile gizli bir temsile kodlar, bu gizli temsili her iki koşullandırma kümesine ekler ve eşleşen boyutlarda sıfırlarla doldurulmuş bir gizli değişken oluşturur. Görüntü genişliği veya yüksekliği 8 pikselin katı değilse, görüntü kodlamadan önce otomatik olarak kırpılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | İstenilen görüntü özellikleri için metin istemleri ve ayarları içeren pozitif koşullandırma verileri. | CONDITIONING | Evet | - |
| `negative` | İstenmeyen görüntü özellikleri için metin istemleri ve ayarları içeren negatif koşullandırma verileri. | CONDITIONING | Evet | - |
| `vae` | Girdi görüntüsünü gizli bir temsile kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `pixels` | İşlenecek ve gizli uzaya kodlanacak girdi görüntüsü. | IMAGE | Evet | - |

**Not:** Girdi görüntüsü, VAE kodlama süreciyle uyumluluğu sağlamak için hem genişlik hem de yükseklikte aşağı yuvarlanarak otomatik olarak 8 pikselin katına kırpılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Kodlanmış görüntü gizli değişkeni eklenmiş pozitif koşullandırma verileri. | CONDITIONING |
| `negative` | Kodlanmış görüntü gizli değişkeni eklenmiş negatif koşullandırma verileri. | CONDITIONING |
| `latent` | Kodlanmış görüntüyle aynı boyutlara sahip sıfırlarla doldurulmuş gizli değişken tensörü. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
