> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNode/tr.md)

ByteDance Seedream 4 düğümü, 4K çözünürlüğe kadar birleşik metinden görüntü oluşturma ve hassas tek cümlelik düzenleme yetenekleri sağlar. Metin istemlerinden yeni görseler oluşturabilir veya mevcut görselleri metin talimatları kullanarak düzenleyebilir. Düğüm, hem tek görsel oluşturmayı hem de birden fazla ilişkili görselin sıralı oluşturulmasını destekler.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | "seedream-4-0-250828" | ["seedream-4-0-250828"] | Model adı |
| `prompt` | STRING | STRING | "" | - | Bir görsel oluşturmak veya düzenlemek için metin istemi. |
| `image` | IMAGE | IMAGE | - | - | Görselden-görsele oluşturma için girdi görsel(ler)i. Tekil veya çoklu referanslı oluşturma için 1-10 görsel listesi. |
| `size_preset` | STRING | COMBO | RECOMMENDED_PRESETS_SEEDREAM_4 içindeki ilk önayar | RECOMMENDED_PRESETS_SEEDREAM_4 içindeki tüm etiketler | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Özel'i seçin. |
| `width` | INT | INT | 2048 | 1024-4096 (adım 64) | Görsel için özel genişlik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında çalışır. |
| `height` | INT | INT | 2048 | 1024-4096 (adım 64) | Görsel için özel yükseklik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında çalışır. |
| `sequential_image_generation` | STRING | COMBO | "disabled" | ["disabled", "auto"] | Grup görsel oluşturma modu. 'disabled' tek bir görsel oluşturur. 'auto', modelin birden fazla ilişkili görsel oluşturup oluşturmayacağına karar vermesine izin verir (örneğin, hikaye sahneleri, karakter varyasyonları). |
| `max_images` | INT | INT | 1 | 1-15 | sequential_image_generation='auto' olduğunda oluşturulacak maksimum görsel sayısı. Toplam görsel sayısı (girdi + oluşturulan) 15'i aşamaz. |
| `seed` | INT | INT | 0 | 0-2147483647 | Oluşturma için kullanılacak tohum değeri. |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Görsele "Yapay Zeka ile Oluşturulmuştur" filigranı eklenip eklenmeyeceği. |
| `fail_on_partial` | BOOLEAN | BOOLEAN | True | - | Etkinleştirilirse, herhangi bir istenen görsel eksikse veya bir hata döndürürse yürütmeyi durdurur. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Girdi parametrelerine ve isteme dayalı olarak oluşturulan görsel(ler) |