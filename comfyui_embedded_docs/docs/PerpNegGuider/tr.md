> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNegGuider/tr.md)

PerpNegGuider düğümü, dik negatif koşullandırma kullanarak görüntü oluşturmayı kontrol etmek için bir kılavuzluk sistemi oluşturur. Pozitif, negatif ve boş koşullandırma girdilerini alır ve oluşturma sürecini yönlendirmek için özelleştirilmiş bir kılavuzluk algoritması uygular. Bu düğüm test amaçları için tasarlanmıştır ve kılavuzluk gücü ile negatif ölçeklendirme üzerinde hassas kontrol sağlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Kılavuzluk oluşturma için kullanılacak model |
| `pozitif` | CONDITIONING | Evet | - | Oluşturmayı istenen içeriğe yönlendiren pozitif koşullandırma |
| `negatif` | CONDITIONING | Evet | - | Oluşturmayı istenmeyen içerikten uzaklaştıran negatif koşullandırma |
| `boş_koşullandırma` | CONDITIONING | Evet | - | Temel referans olarak kullanılan boş veya nötr koşullandırma |
| `cfg` | FLOAT | Hayır | 0.0 - 100.0 | Koşullandırmanın oluşturma üzerindeki etkisinin ne kadar güçlü olduğunu kontrol eden sınıflandırıcısız kılavuzluk ölçeği (varsayılan: 8.0) |
| `neg_ölçek` | FLOAT | Hayır | 0.0 - 100.0 | Negatif koşullandırmanın gücünü ayarlayan negatif ölçeklendirme faktörü (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `guider` | GUIDER | Oluşturma işlem hattında kullanıma hazır yapılandırılmış bir kılavuzluk sistemi |