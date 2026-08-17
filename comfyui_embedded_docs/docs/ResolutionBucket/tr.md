# Çözünürlük Kovası

Bu düğüm, bir latent listesini ve bunlara karşılık gelen koşullama verilerini çözünürlüklerine göre düzenler. Aynı yükseklik ve genişliğe sahip öğeleri bir araya gruplayarak benzersiz çözünürlükler için ayrı batch'ler oluşturur. Bu işlem, modellerin aynı boyuttaki birden fazla öğeyi birlikte işlemesine olanak tanıdığı için verimli eğitim için veri hazırlamada kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `latents` | Çözünürlüğe göre gruplanacak latent sözlüklerinin listesi. | LATENT | Evet | N/A |
| `conditioning` | Koşullama listelerinin listesi (latents uzunluğuyla eşleşmelidir). | CONDITIONING | Evet | N/A |

**Not:** `latents` listesindeki öğe sayısı, `conditioning` listesindeki öğe sayısıyla tam olarak eşleşmelidir. Her latent sözlüğü bir batch örnek içerebilir ve karşılık gelen koşullama listesi, bu batch için eşleşen sayıda koşullama öğesi içermelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latents` | Her çözünürlük grubu için bir tane olmak üzere batch haline getirilmiş latent sözlüklerinin listesi. | LATENT |
| `conditioning` | Her çözünürlük grubu için bir tane olmak üzere koşul listelerinin listesi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/tr.md)

---
**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`
