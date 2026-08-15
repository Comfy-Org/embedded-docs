# Wan 2.7 Video Düzenleme

Wan2VideoEditApi düğümü, metin talimatları, referans görüntüleri veya stil aktarımına dayalı olarak bir videoyu düzenlemek için Wan 2.7 modelini kullanır. Girdi videoyu işler ve çözünürlük, süre ve en-boy oranı gibi belirtilen parametrelere göre yeni bir video oluşturur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video düzenleme için kullanılacak model. | DYNAMIC_COMBO | Evet | `"wan2.7-videoedit"` |
| `video` | Düzenlenecek video. | VIDEO | Evet | - |
| `tohum` | Üretim için kullanılacak tohum değeri. (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 |
| `ses_ayarı` | 'auto': model, isteme göre sesin yeniden oluşturulup oluşturulmayacağına karar verir. 'origin': girdi videodaki orijinal sesi korur. (varsayılan: "auto") | COMBO | Hayır | `"auto"`<br>`"origin"` |
| `filigran` | Sonuca yapay zeka tarafından üretilmiş bir filigran eklenip eklenmeyeceği. (varsayılan: False) | BOOLEAN | Hayır | - |

### wan2.7-videoedit Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Düzenleme talimatları veya stil aktarımı gereksinimleri. (varsayılan: boş dize) | STRING | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720P"`<br>`"1080P"` |
| `ratio` | En-boy oranı. Değiştirilmezse girdi video oranına yaklaşır. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Çıktı süresi saniye cinsinden. 'auto' girdi video süresiyle eşleşir. Belirli bir değer videoyu baştan itibaren kırpar. (varsayılan: "auto") | COMBO | Evet | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Genişletilebilir yuva: Düzenlemeyi yönlendirmek için 0 ile 4 görüntü (`image1`...`image4`) bağlayın. wan2.7-videoedit modeli için sayı sınırı 4'tür. | IMAGE | Hayır | 0 ile 4 öğe |

**Kısıtlamalar:**
*   `prompt` en az 1 karakter içermelidir.
*   `video` girdisinin süresi 2 ile 10 saniye arasında olmalıdır.
*   `reference_images` genişletilebilir yuvası en fazla 4 görüntü kabul eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Model tarafından oluşturulan düzenlenmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `27283273ee56c90903db103a3e9bc17dc4df0914676c9aedd2a115b07937dc10`
