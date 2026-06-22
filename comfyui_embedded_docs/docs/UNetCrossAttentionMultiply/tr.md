# UNetÇaprazDikkatÇarpımı

UNetCrossAttentionMultiply düğümü, bir UNet modelindeki çapraz dikkat mekanizmasına çarpma faktörleri uygular. Farklı dikkat davranışlarını ve etkilerini denemek için çapraz dikkat katmanlarının sorgu, anahtar, değer ve çıktı bileşenlerini ölçeklendirmenize olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Dikkat ölçeklendirme faktörleriyle değiştirilecek UNet modeli | MODEL | Evet | - |
| `q` | Çapraz dikkatte sorgu bileşenleri için ölçeklendirme faktörü (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |
| `k` | Çapraz dikkatte anahtar bileşenleri için ölçeklendirme faktörü (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |
| `v` | Çapraz dikkatte değer bileşenleri için ölçeklendirme faktörü (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |
| `çıktı` | Çapraz dikkatte çıktı bileşenleri için ölçeklendirme faktörü (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Ölçeklendirilmiş çapraz dikkat bileşenlerine sahip değiştirilmiş UNet modeli | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetCrossAttentionMultiply/tr.md)

---
**Source fingerprint (SHA-256):** `2623858c11e93ab5952194670c9e4ea74bba4e2ea32089540665eea361dc1491`
