> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/tr.md)

Wan2VideoEditApi düğümü, metin talimatlarına, referans görüntülere veya stil aktarımına dayalı olarak bir videoyu düzenlemek için Wan 2.7 modelini kullanır. Giriş videosunu işler ve çözünürlük, süre ve en boy oranı gibi belirtilen parametrelere göre yeni bir video oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"wan2.7-videoedit"` | Video düzenleme için kullanılacak model. |
| `model.prompt` | STRING | Evet | - | Düzenleme talimatları veya stil aktarımı gereksinimleri. (varsayılan: boş dize) |
| `model.resolution` | COMBO | Evet | `"720P"`<br>`"1080P"` | Çıktı videosunun çözünürlüğü. |
| `model.ratio` | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | Çıktı videosunun en boy oranı. Değiştirilmezse, giriş videosunun oranına yaklaşır. |
| `model.duration` | COMBO | Evet | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` | Saniye cinsinden çıktı süresi. 'auto', giriş videosunun süresiyle eşleşir. Belirli bir değer, videonun başlangıcından itibaren kırpar. (varsayılan: "auto") |
| `model.reference_images` | IMAGE | Hayır | - | Düzenlemeyi yönlendirmek için en fazla 4 referans görüntüden oluşan bir liste. |
| `video` | VIDEO | Evet | - | Düzenlenecek video. |
| `tohum` | INT | Hayır | 0 ile 2147483647 arası | Üretim için kullanılacak tohum değeri. (varsayılan: 0) |
| `ses_ayarı` | COMBO | Hayır | `"auto"`<br>`"origin"` | 'auto': model, istem temelinde sesi yeniden oluşturup oluşturmayacağına karar verir. 'origin': giriş videosundaki orijinal sesi korur. (varsayılan: "auto") |
| `filigran` | BOOLEAN | Hayır | - | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği. (varsayılan: False) |

**Kısıtlamalar:**
*   `model.prompt` en az 1 karakter uzunluğunda olmalıdır.
*   Giriş `video` süresi 2 ile 10 saniye arasında olmalıdır.
*   `model.reference_images` girişi en fazla 4 görüntü kabul edebilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Model tarafından oluşturulan düzenlenmiş video. |

---
**Source fingerprint (SHA-256):** `d2dd65d743358c6a357e75076774e93c52c39893fbb376da2f4395446f440a20`
