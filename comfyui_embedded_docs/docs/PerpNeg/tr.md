> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNeg/tr.md)

PerpNeg düğümü, bir modelin örnekleme sürecine dik negatif yönlendirme uygular. Bu düğüm, negatif koşullandırma ve ölçeklendirme faktörleri kullanarak gürültü tahminlerini ayarlamak için modelin yapılandırma işlevini değiştirir. Kullanımı artık önerilmemekte ve geliştirilmiş işlevsellik için PerpNegGuider düğümü ile değiştirilmiştir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Dik negatif yönlendirme uygulanacak model |
| `boş_koşullandırma` | CONDITIONING | Evet | - | Negatif yönlendirme hesaplamalarında kullanılan boş koşullandırma |
| `neg_ölçek` | FLOAT | Hayır | 0.0 - 100.0 | Negatif yönlendirme için ölçeklendirme faktörü (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Dik negatif yönlendirme uygulanmış değiştirilmiş model |

**Not**: Bu düğümün kullanımı artık önerilmemekte ve PerpNegGuider ile değiştirilmiştir. Deneysel olarak işaretlenmiştir ve üretim iş akışlarında kullanılmamalıdır.