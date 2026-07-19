# Perp-Neg (PerpNegGuider tarafından ESKİ)

PerpNeg düğümü, bir modelin örnekleme sürecine dik negatif yönlendirme uygular. Bu düğüm, negatif koşullandırma ve ölçekleme faktörlerini kullanarak gürültü tahminlerini ayarlamak için modelin yapılandırma fonksiyonunu değiştirir. Kullanımdan kaldırılmış olup, gelişmiş işlevsellik için PerpNegGuider düğümü ile değiştirilmiştir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Dik negatif yönlendirmenin uygulanacağı model | MODEL | Evet | - |
| `boş_koşullandırma` | Negatif yönlendirme hesaplamaları için kullanılan boş koşullandırma | CONDITIONING | Evet | - |
| `neg_ölçek` | Negatif yönlendirme için ölçekleme faktörü (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Dik negatif yönlendirme uygulanmış değiştirilmiş model | MODEL |

**Not**: Bu düğüm kullanımdan kaldırılmıştır ve yerini PerpNegGuider almıştır. Deneysel olarak işaretlenmiştir ve üretim iş akışlarında kullanılmamalıdır.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNeg/tr.md)

---
**Source fingerprint (SHA-256):** `6be4ab03cfbda33ed3966ecd579c1a5e3242bdfb163fecefb9c80073a8827cae`
