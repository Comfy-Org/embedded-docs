> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/tr.md)

ByteDance Image Edit düğümü, bir API aracılığıyla ByteDance'ın AI modellerini kullanarak görselleri düzenlemenize olanak tanır. Bir girdi görseli ve istenen değişiklikleri açıklayan bir metin istemi sağlarsınız; düğüm de talimatlarınıza göre görseli işler. Düğüm, API iletişimini otomatik olarak halleder ve düzenlenmiş görseli döndürür.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seededit_3 | Image2ImageModelName seçenekleri | Model adı |
| `image` | IMAGE | IMAGE | - | - | Düzenlenecek temel görsel |
| `prompt` | STRING | STRING | "" | - | Görseli düzenleme talimatı |
| `seed` | INT | INT | 0 | 0-2147483647 | Üretim için kullanılacak seed değeri |
| `guidance_scale` | FLOAT | FLOAT | 5.5 | 1.0-10.0 | Daha yüksek değer, görselin istemi daha yakından takip etmesini sağlar |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Görsele "AI tarafından oluşturuldu" filigranı eklenip eklenmeyeceği |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | ByteDance API'sından dönen düzenlenmiş görsel |