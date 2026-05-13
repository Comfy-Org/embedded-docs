> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageReferenceNode/tr.md)

**ByteDance Görsel Referans Düğümü**, bir metin istemi ve birden dörde kadar referans görsel kullanarak video oluşturur. Görselleri ve istemi, açıklamanızla eşleşen ve referans görsellerinizdeki görsel stili ve içeriği birleştiren bir video oluşturan harici bir API hizmetine gönderir. Düğüm, video çözünürlüğü, en boy oranı, süre ve diğer oluşturma parametreleri için çeşitli kontroller sağlar.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | STRING | Evet | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"` | Video oluşturma için kullanılacak AI modeli (varsayılan: `"seedance-1-0-lite-i2v-250428"`). |
| `prompt` | STRING | Evet | - | Videoyu oluşturmak için kullanılan metin istemi. |
| `images` | IMAGE | Evet | - | Birden dörde kadar görsel. Her görsel 300x300 ile 6000x6000 piksel arasında olmalı ve en boy oranı 0,4 ile 2,5 arasında olmalıdır. |
| `resolution` | STRING | Evet | `"480p"`<br>`"720p"` | Çıktı videosunun çözünürlüğü. |
| `aspect_ratio` | STRING | Evet | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | Çıktı videosunun en boy oranı (varsayılan: `"adaptive"`). |
| `duration` | INT | Evet | 3 - 12 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). |
| `seed` | INT | Hayır | 0 - 2147483647 | Oluşturma için kullanılacak tohum değeri (varsayılan: 0). |
| `watermark` | BOOLEAN | Hayır | - | Videoya "AI tarafından oluşturuldu" filigranı eklenip eklenmeyeceği (varsayılan: False). |

**Not:** İstem metni şu parametre dizelerini içermemelidir: `--resolution`, `--ratio`, `--duration`, `--seed` veya `--watermark`. Bu değerler yalnızca kendilerine ayrılmış giriş widget'ları aracılığıyla kontrol edilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Giriş istemi ve referans görsellerine dayalı olarak oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `d5d1292d6af2fe24dc5c8a10174204546a5a6054ea1f43db44a45ce1017957d6`
