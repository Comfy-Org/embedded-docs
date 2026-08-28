# Çözünürlük Kovası

Bu düğüm, bir latent görüntü listesini ve bunlara karşılık gelen conditioning verilerini çözünürlüklerine göre düzenler. Aynı yükseklik ve genişliğe sahip öğeleri gruplandırarak her benzersiz çözünürlük için ayrı gruplar (batch) oluşturur. Bu işlem, modellerin aynı boyuttaki birden çok öğeyi birlikte işlemesine olanak tanıdığından, verimli eğitim için veri hazırlamada kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `latentler` | Çözünürlüğe göre gruplanacak latent sözlüklerinin listesi. | LATENT | Evet | N/A |
| `koşullandırma` | Conditioning listelerinin listesi (`latents` uzunluğuyla eşleşmelidir). | CONDITIONING | Evet | N/A |

**Not:** `latents` listesindeki öğe sayısı, `conditioning` listesindeki öğe sayısıyla tam olarak eşleşmelidir. Sayılar eşleşmezse düğüm bir hata verir. Her latent sözlüğü bir grup örnek içerebilir ve ilgili conditioning listesi, bu grup için eşleşen sayıda conditioning öğesi içermelidir. Latent örnekleri, görüntüler için (B, C, H, W) veya videolar için (B, T, C, H, W) şeklinde olabilir; düğüm bunları yalnızca yükseklik ve genişliğe göre gruplar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `latentler` | Çözünürlük grubu başına bir tane olacak şekilde gruplandırılmış latent sözlüklerinin listesi. | LATENT |
| `koşullandırma` | Çözünürlük grubu başına bir tane olacak şekilde conditioning listelerinin listesi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/tr.md)

---
**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`
