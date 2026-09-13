# Çözünürlük Kovası

Bu düğüm, latent görüntülerden oluşan bir listeyi ve bunlara karşılık gelen koşullandırma verilerini çözünürlüklerine göre düzenler. Aynı yükseklik ve genişliği paylaşan öğeleri bir araya gruplar ve her benzersiz çözünürlük için ayrı batch’ler oluşturur. Bu işlem, verileri verimli eğitim için hazırlamada kullanışlıdır; çünkü modellerin aynı boyuttaki birden çok öğeyi birlikte işlemesine olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `latentler` | Çözünürlüğe göre gruplandırılacak latent sözlükleri listesi. | LATENT | Evet | N/A |
| `koşullandırma` | Koşullandırma listeleri listesi (`latents` uzunluğuyla eşleşmelidir). | CONDITIONING | Evet | N/A |

**Not:** Her iki girdi de liste türünde girdilerdir; yani düğüm her biri için bir öğe listesi alır. `latents` listesindeki öğe sayısı, `conditioning` listesindeki öğe sayısıyla tam olarak eşleşmelidir; sayılar eşleşmezse düğüm hata verir. Her latent sözlüğü bir örneklem batch’i içerebilir ve ilgili koşullandırma listesi bu batch için eşleşen sayıda koşullandırma öğesi içermelidir; çünkü batch’teki her örneklem kendi koşullandırma girdisiyle eşleştirilir. Latent örneklemleri görüntüler için (B, C, H, W) veya videolar için (B, T, C, H, W) şeklinde olabilir; düğüm bunları yalnızca yükseklik ve genişliğe göre gruplar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latents` | Çözünürlük grubu başına bir tane olacak şekilde, batch’lenmiş latent sözlükleri listesi. | LATENT |
| `conditioning` | Çözünürlük grubu başına bir tane olacak şekilde, koşullandırma listeleri listesi. | CONDITIONING |

**Not:** Her iki çıktı da liste türünde çıktılardır. Her çıktı listesi, girdide bulunan her benzersiz çözünürlük (yükseklik ve genişlik) için bir giriş içerir; bu girişler çözünürlüklerin ilk karşılaşılma sırasına göredir. Her gruptaki latentler yeni bir batch boyutu boyunca yığılır.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/tr.md)

---
**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`
