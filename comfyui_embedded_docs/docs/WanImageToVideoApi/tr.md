> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideoApi/tr.md)

Wan Image to Video düğümü, tek bir giriş görüntüsü ve bir metin isteminden başlayarak video içeriği oluşturur. Başlangıç karesini sağlanan açıklamaya göre genişleterek video dizileri oluşturur ve video kalitesi, süresi ve ses entegrasyonunu kontrol etme seçenekleri sunar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | "wan2.5-i2v-preview"<br>"wan2.5-i2v-preview" | Kullanılacak model (varsayılan: "wan2.5-i2v-preview") |
| `image` | IMAGE | Evet | - | Video oluşturma için ilk kare olarak hizmet veren giriş görüntüsü |
| `prompt` | STRING | Evet | - | Öğeleri ve görsel özellikleri tanımlamak için kullanılan istem, İngilizce/Çince destekler (varsayılan: boş) |
| `negative_prompt` | STRING | Hayır | - | Nelerden kaçınılacağını yönlendirmek için kullanılan olumsuz metin istemi (varsayılan: boş) |
| `resolution` | COMBO | Hayır | "480P"<br>"720P"<br>"1080P" | Video çözünürlük kalitesi (varsayılan: "480P") |
| `duration` | INT | Hayır | 5-10 | Mevcut süreler: 5 ve 10 saniye (varsayılan: 5) |
| `audio` | AUDIO | Hayır | - | Ses, net, yüksek sesli bir konuşma içermeli, fazladan gürültü, arka plan müziği olmamalı |
| `seed` | INT | Hayır | 0-2147483647 | Oluşturma için kullanılacak seed değeri (varsayılan: 0) |
| `generate_audio` | BOOLEAN | Hayır | - | Ses girişi yoksa, otomatik olarak ses oluştur (varsayılan: False) |
| `prompt_extend` | BOOLEAN | Hayır | - | İstemin AI yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: True) |
| `watermark` | BOOLEAN | Hayır | - | Sonuca "AI generated" filigranı eklenip eklenmeyeceği (varsayılan: True) |

**Kısıtlamalar:**

- Video oluşturma için tam olarak bir giriş görüntüsü gereklidir
- Süre parametresi yalnızca 5 veya 10 saniye değerlerini kabul eder
- Ses sağlandığında, süresi 3.0 ile 29.0 saniye arasında olmalıdır

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Giriş görüntüsü ve istemine dayalı olarak oluşturulan video |