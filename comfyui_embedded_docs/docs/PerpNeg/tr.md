> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNeg/tr.md)

PerpNeg düğümü, bir modelin örnekleme sürecine dik negatif yönlendirme uygular. Bu düğüm, negatif koşullandırma ve ölçekleme faktörlerini kullanarak gürültü tahminlerini ayarlamak için modelin yapılandırma fonksiyonunu değiştirir. Kullanımdan kaldırılmış olup, gelişmiş işlevsellik için PerpNegGuider düğümü ile değiştirilmiştir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | MODEL | Evet | - | Dik negatif yönlendirmenin uygulanacağı model |
| `boş_koşullandırma` | CONDITIONING | Evet | - | Negatif yönlendirme hesaplamaları için kullanılan boş koşullandırma |
| `neg_ölçek` | FLOAT | Hayır | 0.0 - 100.0 | Negatif yönlendirme için ölçekleme faktörü (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | Dik negatif yönlendirme uygulanmış değiştirilmiş model |

**Not**: Bu düğüm kullanımdan kaldırılmıştır ve yerini PerpNegGuider almıştır. Deneysel olarak işaretlenmiştir ve üretim iş akışlarında kullanılmamalıdır.

---
**Source fingerprint (SHA-256):** `6be4ab03cfbda33ed3966ecd579c1a5e3242bdfb163fecefb9c80073a8827cae`
