> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetCrossAttentionMultiply/tr.md)

UNetCrossAttentionMultiply düğümü, bir UNet modelindeki çapraz dikkat mekanizmasına çarpma faktörleri uygular. Farklı dikkat davranışlarını ve etkilerini denemek için çapraz dikkat katmanlarının sorgu, anahtar, değer ve çıktı bileşenlerini ölçeklendirmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Dikkat ölçeklendirme faktörleriyle değiştirilecek UNet modeli |
| `q` | FLOAT | Hayır | 0.0 - 10.0 | Çapraz dikkatte sorgu bileşenleri için ölçeklendirme faktörü (varsayılan: 1.0) |
| `k` | FLOAT | Hayır | 0.0 - 10.0 | Çapraz dikkatte anahtar bileşenleri için ölçeklendirme faktörü (varsayılan: 1.0) |
| `v` | FLOAT | Hayır | 0.0 - 10.0 | Çapraz dikkatte değer bileşenleri için ölçeklendirme faktörü (varsayılan: 1.0) |
| `çıktı` | FLOAT | Hayır | 0.0 - 10.0 | Çapraz dikkatte çıktı bileşenleri için ölçeklendirme faktörü (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Ölçeklendirilmiş çapraz dikkat bileşenlerine sahip değiştirilmiş UNet modeli |

---
**Source fingerprint (SHA-256):** `2623858c11e93ab5952194670c9e4ea74bba4e2ea32089540665eea361dc1491`
