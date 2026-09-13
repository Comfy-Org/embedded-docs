# Wan 2.7 Video Düzenleme

Wan 2.7 Video Edit düğümü, bir videoyu metin talimatları, referans görüntüler veya stil aktarımı kullanarak düzenler. Girdi videosunu (ve varsa referans görüntülerini) Wan 2.7 video düzenleme hizmetine gönderir ve seçilen çözünürlük, en boy oranı ve süre ayarlarına göre yeni oluşturulmuş bir video döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video düzenleme için kullanılacak model. Her seçenek kendi alt parametre kümesini sunar. | DYNAMIC_COMBO | Evet | `"wan2.7-videoedit"` |
| `video` | Düzenlenecek video. | VIDEO | Evet | - |
| `tohum` | Oluşturma için kullanılacak tohum. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 |
| `ses_ayarı` | 'auto': modelin isteme göre sesi yeniden oluşturup oluşturmayacağına karar verir. 'origin': girdi videosundaki özgün sesi korur. (varsayılan: "auto") | COMBO | Evet | `"auto"`<br>`"origin"` |
| `filigran` | Sonuca yapay zekâ tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği. (varsayılan: False) | BOOLEAN | Evet | - |

### wan2.7-videoedit Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Düzenleme talimatları veya stil aktarımı gereksinimleri. (varsayılan: boş dize) | STRING | Evet | - |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720P"`<br>`"1080P"` |
| `ratio` | En boy oranı. Değiştirilmezse, girdi videosunun oranına yaklaşır. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Çıktı süresi saniye cinsinden. 'auto', girdi videosunun süresiyle eşleşir. Belirli bir değer, videonun başından itibaren kısaltır. (varsayılan: "auto") | COMBO | Evet | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Büyütülebilir yuva: düzenlemeye rehberlik etmek için 0 ile 4 arasında görüntü (`image1`...`image4`) bağlayın. Sayı sınırı wan2.7-videoedit modeli için 4'tür. | IMAGE | Hayır | 0 ile 4 items |

**Kısıtlamalar:**
*   `audio_setting` ve `watermark` gelişmiş seçeneklerdir.
*   `prompt` en az 1 karakter içermelidir.
*   Girdi `video` süresi 2 ile 10 saniye arasında olmalıdır.
*   `reference_images` büyütülebilir yuvası en fazla 4 görüntü kabul eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Model tarafından oluşturulan düzenlenmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `27283273ee56c90903db103a3e9bc17dc4df0914676c9aedd2a115b07937dc10`
