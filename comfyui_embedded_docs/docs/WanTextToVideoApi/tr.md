> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToVideoApi/tr.md)

Wan Metinden Videoya düğümü, metin açıklamalarına dayalı olarak video içeriği oluşturur. Prompt'lardan video oluşturmak için AI modellerini kullanır ve çeşitli video boyutları, süreleri ve isteğe bağlı ses girişlerini destekler. Düğüm, gerektiğinde otomatik olarak ses oluşturabilir ve prompt geliştirme ve filigran ekleme seçenekleri sunar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | "wan2.5-t2v-preview" | Kullanılacak model (varsayılan: "wan2.5-t2v-preview") |
| `prompt` | STRING | Evet | - | Öğeleri ve görsel özellikleri tanımlamak için kullanılan prompt, İngilizce/Çince destekler (varsayılan: "") |
| `negative_prompt` | STRING | Hayır | - | Nelerden kaçınılacağını yönlendirmek için kullanılan negatif metin prompt'u (varsayılan: "") |
| `size` | COMBO | Hayır | "480p: 1:1 (624x624)"<br>"480p: 16:9 (832x480)"<br>"480p: 9:16 (480x832)"<br>"720p: 1:1 (960x960)"<br>"720p: 16:9 (1280x720)"<br>"720p: 9:16 (720x1280)"<br>"720p: 4:3 (1088x832)"<br>"720p: 3:4 (832x1088)"<br>"1080p: 1:1 (1440x1440)"<br>"1080p: 16:9 (1920x1080)"<br>"1080p: 9:16 (1080x1920)"<br>"1080p: 4:3 (1632x1248)"<br>"1080p: 3:4 (1248x1632)" | Video çözünürlüğü ve en-boy oranı (varsayılan: "480p: 1:1 (624x624)") |
| `duration` | INT | Hayır | 5-10 | Mevcut süreler: 5 ve 10 saniye (varsayılan: 5) |
| `audio` | AUDIO | Hayır | - | Ses, net, yüksek sesli bir konuşma içermeli, fazladan gürültü, arka plan müziği olmamalı |
| `seed` | INT | Hayır | 0-2147483647 | Oluşturma için kullanılacak seed değeri (varsayılan: 0) |
| `generate_audio` | BOOLEAN | Hayır | - | Ses girişi yoksa, otomatik olarak ses oluştur (varsayılan: False) |
| `prompt_extend` | BOOLEAN | Hayır | - | Prompt'un AI yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: True) |
| `watermark` | BOOLEAN | Hayır | - | Sonuca "AI generated" filigranı eklenip eklenmeyeceği (varsayılan: True) |

**Not:** `duration` parametresi yalnızca 5 veya 10 saniye değerlerini kabul eder, çünkü bunlar mevcut sürelerdir. Ses girişi sağlanırken, süresi 3.0 ile 29.0 saniye arasında olmalı ve arka plan gürültüsü veya müzik olmadan net ses içermelidir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Giriş parametrelerine dayalı olarak oluşturulan video |