> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/tr.md)

Veo3FirstLastFrameNode, Google'ın Veo 3 modelini kullanarak bir video oluşturur. Bir metin istemine dayalı olarak video üretir ve dizinin başlangıcını ve sonunu yönlendirmek için sağlanan bir ilk ve son kareyi kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | Videoyu tanımlayan metin açıklaması (varsayılan: boş dize). |
| `negative_prompt` | STRING | Hayır | Yok | Videoda nelerden kaçınılacağını yönlendirmek için olumsuz metin istemi (varsayılan: boş dize). |
| `resolution` | COMBO | Evet | `"720p"`<br>`"1080p"` | Çıktı videosunun çözünürlüğü. |
| `aspect_ratio` | COMBO | Hayır | `"16:9"`<br>`"9:16"` | Çıktı videosunun en-boy oranı (varsayılan: "16:9"). |
| `duration` | INT | Hayır | 4 - 8 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 8). |
| `seed` | INT | Hayır | 0 - 4294967295 | Video oluşturma için tohum değeri (varsayılan: 0). |
| `first_frame` | IMAGE | Evet | Yok | Video için başlangıç karesi. |
| `last_frame` | IMAGE | Evet | Yok | Video için bitiş karesi. |
| `model` | COMBO | Hayır | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"` | Oluşturma için kullanılacak belirli Veo 3 modeli (varsayılan: "veo-3.1-fast-generate"). |
| `generate_audio` | BOOLEAN | Hayır | Yok | Video için ses oluştur (varsayılan: True). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası. |
