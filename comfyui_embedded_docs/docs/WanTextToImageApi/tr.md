> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/tr.md)

Wan Metinden Görüntüye düğümü, metin açıklamalarına dayalı görüntüler oluşturur. Yazılı prompt'lardan görsel içerik oluşturmak için AI modellerini kullanır ve hem İngilizce hem de Çince metin girişini destekler. Düğüm, çıktı görüntüsünün boyutunu, kalitesini ve stil tercihlerini ayarlamak için çeşitli kontroller sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | "wan2.5-t2i-preview" | Kullanılacak model (varsayılan: "wan2.5-t2i-preview") |
| `prompt` | STRING | Evet | - | Öğeleri ve görsel özellikleri tanımlamak için kullanılan prompt, İngilizce/Çince destekler (varsayılan: boş) |
| `negative_prompt` | STRING | Hayır | - | Nelerden kaçınılacağını yönlendirmek için kullanılan negatif metin prompt'u (varsayılan: boş) |
| `width` | INT | Hayır | 768-1440 | Görüntü genişliği (piksel cinsinden) (varsayılan: 1024, adım: 32) |
| `height` | INT | Hayır | 768-1440 | Görüntü yüksekliği (piksel cinsinden) (varsayılan: 1024, adım: 32) |
| `seed` | INT | Hayır | 0-2147483647 | Oluşturma için kullanılacak seed değeri (varsayılan: 0) |
| `prompt_extend` | BOOLEAN | Hayır | - | Prompt'un AI yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: True) |
| `watermark` | BOOLEAN | Hayır | - | Sonuca "AI generated" (AI tarafından oluşturuldu) filigranı eklenip eklenmeyeceği (varsayılan: True) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Metin prompt'una dayalı olarak oluşturulan görüntü |