CLIPAttentionMultiply düğümü, CLIP modellerinde öz-dikkat katmanlarının farklı bileşenlerine çarpma faktörleri uygulayarak dikkat mekanizmasını ayarlamanıza olanak tanır. Bu düğüm, CLIP modelinin dikkat mekanizmasındaki sorgu, anahtar, değer ve çıktı projeksiyon ağırlıklarını ve biaslarını değiştirerek çalışır. Bu deneysel düğüm, belirtilen ölçekleme faktörleri uygulanmış, girdi CLIP modelinin değiştirilmiş bir kopyasını oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Değiştirilecek CLIP modeli | CLIP | Evet | - |
| `q` | Sorgu projeksiyon ağırlıkları ve biasları için çarpma faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 10.0 |
| `k` | Anahtar projeksiyon ağırlıkları ve biasları için çarpma faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 10.0 |
| `v` | Değer projeksiyon ağırlıkları ve biasları için çarpma faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 10.0 |
| `çıktı` | Çıktı projeksiyon ağırlıkları ve biasları için çarpma faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 10.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CLIP` | Belirtilen dikkat ölçekleme faktörleri uygulanmış değiştirilmiş bir CLIP modeli döndürür | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAttentionMultiply/tr.md)

---
**Source fingerprint (SHA-256):** `43dab83ecfc928f3359eb7560658f43235bf3faa62c81084a2b4f482e3a4638f`
