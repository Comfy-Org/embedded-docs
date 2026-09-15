# SD_4X_Büyütme_Koşullandırma

SD_4XUpscale_Conditioning düğümü, görüntüleri difüzyon modelleriyle büyütmek için koşullandırma verilerini hazırlar. Girdi görüntülerini seçilen bir oranla ölçekler, isteğe bağlı gürültü artırımı ekler ve büyütülmüş boyut için boş bir latent ile birlikte değiştirilmiş pozitif ve negatif koşullandırmayı döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görüntüler` | Büyütülecek girdi görüntüleri. | IMAGE | Evet | - |
| `pozitif` | Üretimi istenen içeriğe yönlendiren pozitif koşullandırma verisi. | CONDITIONING | Evet | - |
| `negatif` | Üretimi istenmeyen içerikten uzaklaştıran negatif koşullandırma verisi. | CONDITIONING | Evet | - |
| `ölçek_oranı` | Büyütülmüş koşullandırma ve latent hazırlanırken girdi görüntü boyutlarına uygulanan çarpan (varsayılan: 4.0). | FLOAT | Evet | 0.0 - 10.0 (adım 0.01) |
| `gürültü_artırımı` | Büyütme işlemi sırasında eklenecek gürültü miktarı (varsayılan: 0.0). | FLOAT | Evet | 0.0 - 1.0 (adım 0.001) |

Not: `noise_augmentation` gelişmiş bir parametredir ve düğüm arayüzünde "Gelişmiş" anahtarının altında gösterilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Ölçeklenmiş görüntü verileri ve gürültü artırımı ayarları uygulanmış, değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Ölçeklenmiş görüntü verileri ve gürültü artırımı ayarları uygulanmış, değiştirilmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Büyütülmüş boyutlarla eşleşen boş latent temsili. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`
