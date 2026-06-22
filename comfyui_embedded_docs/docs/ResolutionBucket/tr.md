# Çözünürlük Kovası

Bu düğüm, gizli görüntülerin (latent images) bir listesini ve bunlara karşılık gelen koşullandırma (conditioning) verilerini çözünürlüklerine göre düzenler. Aynı yükseklik ve genişliğe sahip öğeleri bir araya getirerek her benzersiz çözünürlük için ayrı gruplar oluşturur. Bu işlem, verileri verimli eğitim için hazırlamada kullanışlıdır çünkü modellerin aynı boyuttaki birden fazla öğeyi birlikte işlemesine olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `latentler` | Çözünürlüğe göre gruplanacak gizli sözlüklerin listesi. | LATENT | Evet | Yok |
| `koşullandırma` | Koşullandırma listelerinin listesi (`latentler` uzunluğuyla eşleşmelidir). | CONDITIONING | Evet | Yok |

**Not:** `latents` listesindeki öğe sayısı, `conditioning` listesindeki öğe sayısıyla tam olarak eşleşmelidir. Her gizli sözlük bir grup örnek içerebilir ve karşılık gelen koşullandırma listesi, bu grup için eşleşen sayıda koşullandırma öğesi içermelidir.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latentler` | Çözünürlük grubu başına bir tane olmak üzere gruplanmış gizli sözlüklerin listesi. | LATENT |
| `koşullandırma` | Çözünürlük grubu başına bir tane olmak üzere koşullandırma listelerinin listesi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/tr.md)

---
**Source fingerprint (SHA-256):** `2858de5f0827812002ca72ba5d7ce56411d1ef97e9a12a65fc4bea193a1a0ec0`
