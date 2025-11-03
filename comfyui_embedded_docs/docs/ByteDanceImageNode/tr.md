> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageNode/tr.md)

ByteDance Image düğümü, metin istemlerine dayalı olarak bir API aracılığıyla ByteDance modellerini kullanarak görüntüler oluşturur. Farklı modeller seçmenize, görüntü boyutlarını belirtmenize ve seed veya guidance scale gibi çeşitli üretim parametrelerini kontrol etmenize olanak tanır. Düğüm, ByteDance'ın görüntü oluşturma hizmetine bağlanır ve oluşturulan görüntüyü döndürür.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seedream_3 | Text2ImageModelName seçenekleri | Model adı |
| `prompt` | STRING | STRING | - | - | Görseli oluşturmak için kullanılan metin istemi |
| `size_preset` | STRING | COMBO | - | RECOMMENDED_PRESETS etiketleri | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Özel'i seçin |
| `width` | INT | INT | 1024 | 512-2048 (adım 64) | Görsel için özel genişlik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında çalışır |
| `height` | INT | INT | 1024 | 512-2048 (adım 64) | Görsel için özel yükseklik. Değer yalnızca `size_preset` `Custom` olarak ayarlandığında çalışır |
| `seed` | INT | INT | 0 | 0-2147483647 (adım 1) | Üretim için kullanılacak seed (isteğe bağlı) |
| `guidance_scale` | FLOAT | FLOAT | 2.5 | 1.0-10.0 (adım 0.01) | Daha yüksek değer, görselin istemi daha yakından takip etmesini sağlar (isteğe bağlı) |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Görsele "AI generated" filigranı eklenip eklenmeyeceği (isteğe bağlı) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | ByteDance API'sinden oluşturulan görsel |