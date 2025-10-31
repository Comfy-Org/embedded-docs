> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageReferenceNode/tr.md)

ByteDance Image Reference Node, bir metin istemi ve bir ila dört referans görseli kullanarak videolar oluşturur. Görselleri ve istemi, açıklamanızla eşleşen bir video oluştururken referans görsellerinizden görsel stil ve içeriği birleştiren harici bir API servisine gönderir. Düğüm, video çözünürlüğü, en-boy oranı, süre ve diğer oluşturma parametreleri için çeşitli kontroller sağlar.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seedance_1_lite | seedance_1_lite | Model adı |
| `prompt` | STRING | STRING | - | - | Videoyu oluşturmak için kullanılan metin istemi. |
| `images` | IMAGE | IMAGE | - | - | Bir ila dört adet görsel. |
| `resolution` | STRING | COMBO | - | 480p, 720p | Çıktı videosunun çözünürlüğü. |
| `aspect_ratio` | STRING | COMBO | - | adaptive, 16:9, 4:3, 1:1, 3:4, 9:16, 21:9 | Çıktı videosunun en-boy oranı. |
| `duration` | INT | INT | 5 | 3-12 | Çıktı videosunun saniye cinsinden süresi. |
| `seed` | INT | INT | 0 | 0-2147483647 | Oluşturma için kullanılacak seed değeri. |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Videoya "AI generated" (Yapay Zeka ile Oluşturulmuştur) filigranı eklenip eklenmeyeceği. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Girdi istemi ve referans görsellerine dayalı olarak oluşturulan video dosyası. |