UNetSelfAttentionMultiply düğümü, bir UNet modelindeki öz-dikkat mekanizmasının sorgu (query), anahtar (key), değer (value) ve çıktı (output) bileşenlerine çarpma faktörleri uygular. Dikkat ağırlıklarının model davranışını nasıl etkilediğini denemek için dikkat hesaplamasının farklı bölümlerini ölçeklendirmenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Dikkat ölçeklendirme faktörleriyle değiştirilecek UNet modeli | MODEL | Evet | - |
| `q` | Sorgu bileşeni için çarpma faktörü (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |
| `k` | Anahtar bileşeni için çarpma faktörü (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |
| `v` | Değer bileşeni için çarpma faktörü (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |
| `çıktı` | Çıktı bileşeni için çarpma faktörü (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Ölçeklendirilmiş dikkat bileşenlerine sahip değiştirilmiş UNet modeli | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetSelfAttentionMultiply/tr.md)

---
**Source fingerprint (SHA-256):** `ee6328c6cba44d30d2e219a2af04bb3d3d9adeaabb959a46f87b3b299dfe2f43`
