> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetSelfAttentionMultiply/tr.md)

UNetSelfAttentionMultiply düğümü, bir UNet modelindeki öz-dikkat mekanizmasının sorgu (query), anahtar (key), değer (value) ve çıktı (output) bileşenlerine çarpma faktörleri uygular. Dikkat ağırlıklarının model davranışını nasıl etkilediğini denemek için dikkat hesaplamasının farklı bölümlerini ölçeklendirmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Dikkat ölçeklendirme faktörleriyle değiştirilecek UNet modeli |
| `q` | FLOAT | Hayır | 0.0 - 10.0 | Sorgu bileşeni için çarpma faktörü (varsayılan: 1.0) |
| `k` | FLOAT | Hayır | 0.0 - 10.0 | Anahtar bileşeni için çarpma faktörü (varsayılan: 1.0) |
| `v` | FLOAT | Hayır | 0.0 - 10.0 | Değer bileşeni için çarpma faktörü (varsayılan: 1.0) |
| `çıktı` | FLOAT | Hayır | 0.0 - 10.0 | Çıktı bileşeni için çarpma faktörü (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `MODEL` | MODEL | Ölçeklendirilmiş dikkat bileşenlerine sahip değiştirilmiş UNet modeli |

---
**Source fingerprint (SHA-256):** `ee6328c6cba44d30d2e219a2af04bb3d3d9adeaabb959a46f87b3b299dfe2f43`
