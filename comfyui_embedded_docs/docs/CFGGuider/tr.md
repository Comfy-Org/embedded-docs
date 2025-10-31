> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/tr.md)

CFGGuider düğümü, görüntü oluşturma sürecindeki örnekleme işlemini kontrol etmek için bir kılavuzluk sistemi oluşturur. Bir modeli, olumlu ve olumsuz koşullandırma girdileriyle alır ve ardından, istenmeyen öğelerden kaçınırken oluşturma işlemini istenen içeriğe yönlendirmek için sınıflandırıcısız bir kılavuzluk ölçeği uygular. Bu düğüm, görüntü oluşturma yönünü kontrol etmek için örnekleme düğümleri tarafından kullanılabilecek bir kılavuz nesnesi çıktılar.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | Gerekli | - | - | Kılavuzluk için kullanılacak model |
| `positive` | CONDITIONING | Gerekli | - | - | Oluşturma işlemini istenen içeriğe yönlendiren olumlu koşullandırma |
| `negative` | CONDITIONING | Gerekli | - | - | Oluşturma işlemini istenmeyen içerikten uzaklaştıran olumsuz koşullandırma |
| `cfg` | FLOAT | Gerekli | 8.0 | 0.0 - 100.0 | Koşullandırmanın oluşturma işlemini ne kadar güçlü etkilediğini kontrol eden sınıflandırıcısız kılavuzluk ölçeği |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | Oluşturma sürecini kontrol etmek için örnekleme düğümlerine aktarılabilen bir kılavuz nesnesi |