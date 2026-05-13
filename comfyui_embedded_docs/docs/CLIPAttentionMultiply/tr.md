> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAttentionMultiply/tr.md)

CLIPAttentionMultiply düğümü, CLIP modellerinde öz-dikkat katmanlarının farklı bileşenlerine çarpma faktörleri uygulayarak dikkat mekanizmasını ayarlamanıza olanak tanır. Bu düğüm, CLIP modelinin dikkat mekanizmasındaki sorgu, anahtar, değer ve çıktı projeksiyon ağırlıklarını ve biaslarını değiştirerek çalışır. Bu deneysel düğüm, belirtilen ölçekleme faktörleri uygulanmış, girdi CLIP modelinin değiştirilmiş bir kopyasını oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | - | Değiştirilecek CLIP modeli |
| `q` | FLOAT | Evet | 0.0 - 10.0 | Sorgu projeksiyon ağırlıkları ve biasları için çarpma faktörü (varsayılan: 1.0) |
| `k` | FLOAT | Evet | 0.0 - 10.0 | Anahtar projeksiyon ağırlıkları ve biasları için çarpma faktörü (varsayılan: 1.0) |
| `v` | FLOAT | Evet | 0.0 - 10.0 | Değer projeksiyon ağırlıkları ve biasları için çarpma faktörü (varsayılan: 1.0) |
| `çıktı` | FLOAT | Evet | 0.0 - 10.0 | Çıktı projeksiyon ağırlıkları ve biasları için çarpma faktörü (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Belirtilen dikkat ölçekleme faktörleri uygulanmış değiştirilmiş bir CLIP modeli döndürür |

---
**Source fingerprint (SHA-256):** `43dab83ecfc928f3359eb7560658f43235bf3faa62c81084a2b4f482e3a4638f`
