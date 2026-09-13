# LTXVRehberleriKırp

LTXVCropGuides düğümü, bir video oluşturma iş akışından anahtar kare yönlendirme verilerini kaldırır. Pozitif koşullandırmada kayıtlı anahtar kareleri sayar, latent örneklerinin ve gürültü maskesinin sonundan bu sayıda kareyi kırpar ve her iki koşullandırma girdisinden anahtar kare indeksini ve kılavuz dikkat kayıtlarını temizler. Hiç anahtar kare bulunamadığında, koşullandırma girdileri değiştirilmeden döndürülür ve latent, klonlanmış bir örnek tensörü ve kendi gürültü maskesiyle geçirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Üretim için yönlendirme bilgilerini içeren pozitif koşullandırma girdisi. İçerdiği anahtar kare sayısı, latentten kaç karenin kırpılacağını belirler. | CONDITIONING | Evet | - |
| `negative` | Üretimde kaçınılacak şeylere ilişkin yönlendirme bilgilerini içeren negatif koşullandırma girdisi. Anahtar kare verileri, pozitif koşullandırmayla birlikte temizlenir. | CONDITIONING | Evet | - |
| `latent` | Görüntü örneklerini ve gürültü maskesi verilerini içeren latent temsili. Anahtar kareler mevcut olduğunda, son anahtar kareler hem örneklerden hem de gürültü maskesinden kaldırılır. | LATENT | Evet | - |

Not: Kırpma yalnızca pozitif koşullandırmada anahtar kare indeksleri algılandığında gerçekleşir. Hiç anahtar kare algılanmazsa, pozitif ve negatif koşullandırma değiştirilmeden döndürülür; latent ise yine klonlanmış bir örnek tensörü ve açık bir gürültü maskesiyle döndürülür (girdi latentinde yoksa tümü birlerden oluşan bir maske oluşturulur).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Anahtar kare indeksleri ve kılavuz dikkat kayıtları temizlenmiş işlenmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Anahtar kare indeksleri ve kılavuz dikkat kayıtları temizlenmiş işlenmiş negatif koşullandırma | CONDITIONING |
| `latent` | Örnekleri ve gürültü maskesi ayarlanmış, anahtar kare bölümlerinin kaldırıldığı kırpılmış latent temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/tr.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`
