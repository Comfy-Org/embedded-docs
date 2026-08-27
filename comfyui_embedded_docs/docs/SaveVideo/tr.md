# Videoyu Kaydet

Save Video düğümü, girdi videosunu ComfyUI çıktı dizininize kaydeder. Dosya adı ön ekini, kapsayıcı biçimini, video codec'ini ve kalite ile renk uzayı gibi kodlama seçeneklerini seçebilirsiniz. Düğüm, sayaç artışlarıyla dosya adlandırmayı otomatik olarak yönetir ve kaydedilen dosyaya iş akışı meta verilerini gömebilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Kaydedilecek video. | VIDEO | Evet | - |
| `dosyaadı_öneki` | Kaydedilecek dosyanın ön eki. Düğümlerden değerler eklemek için `%date:yyyy-MM-dd%` veya `%Empty Latent Image.width%` gibi biçimlendirme bilgileri içerebilir (varsayılan: "video/ComfyUI"). | STRING | Evet | - |
| `format` | Çıktı kapsayıcısı. Auto, mümkün olduğunda kaynak kapsayıcıyı korur; MP4, MKV ve WebM belirli bir kapsayıcı seçer (varsayılan: "auto"). | DYNAMIC_COMBO | Evet | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"` |
| `codec` | Çıktı video codec'i. Auto, uyumlu bir kaynak akışını korur. H.264 ve AV1 yeniden kodlama SDR, HDR (HLG) ve HDR PQ destekler. Bir format seçildiğinde görünür (varsayılan: "auto"). | DYNAMIC_COMBO | Hayır | `"auto"`<br>`"h264"`<br>`"av1"` |

### H.264 Girdileri

Bu girdiler `codec` `"h264"` olduğunda görünür. Bu codec, `auto`, `mp4` ve `mkv` formatlarıyla kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `encoding` | Otomatik, uyumlu H.264 akışlarını korur. Yeniden kodlama, özel kodlama seçeneklerini uygular. | DYNAMIC_COMBO | Hayır | `"auto"`<br>`"re-encode"` |
| `crf` | Düşük değerler daha yüksek kalite ve daha büyük dosyalar üretir. `encoding` `"re-encode"` olduğunda görünür (varsayılan: 23.0). | FLOAT | Hayır | 0.0 ile 51.0 |
| `color_space` | Auto, görüntülerden oluşturulan videolar için sRGB kullanır ve yüklenen videolarda tanınan renkleri korur. sRGB, SDR BT.709/sRGB yazar. HDR, 10 bit BT.2020/HLG yazar; HDR PQ, BT.2020/PQ yazar. Diğer giriş pikselleri zaten seçili renk uzayını kullanmalıdır. `encoding` `"re-encode"` olduğunda görünür (varsayılan: "auto"). | COMBO | Hayır | `"auto"`<br>`"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

### AV1 Girdileri

Bu girdiler `codec` `"av1"` olduğunda görünür. Bu codec, `auto`, `mp4`, `mkv` ve `webm` formatlarıyla kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `encoding` | Otomatik, uyumlu AV1 akışlarını korur. Yeniden kodlama, özel kodlama seçeneklerini uygular. | DYNAMIC_COMBO | Hayır | `"auto"`<br>`"re-encode"` |
| `crf` | Düşük değerler daha yüksek kalite ve daha büyük dosyalar üretir. `encoding` `"re-encode"` olduğunda görünür (varsayılan: 30.0). | FLOAT | Hayır | 0.0 ile 63.0 |
| `color_space` | Auto, görüntülerden oluşturulan videolar için sRGB kullanır ve yüklenen videolarda tanınan renkleri korur. sRGB, SDR BT.709/sRGB yazar. HDR, 10 bit BT.2020/HLG yazar; HDR PQ, BT.2020/PQ yazar. Diğer giriş pikselleri zaten seçili renk uzayını kullanmalıdır. `encoding` `"re-encode"` olduğunda görünür (varsayılan: "auto"). | COMBO | Hayır | `"auto"`<br>`"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

Not: `webm` formatı yalnızca `auto` ve `av1` codec'lerini destekler. `format` `"auto"` olduğunda, mümkünse kaynak kapsayıcı korunur. `color_space` `"auto"` olduğunda, açık bir renk uzayı uygulanmaz ve renk uzayı otomatik olarak belirlenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Girdi videosu, değiştirilmemiş. | VIDEO |
| `ui` | Kaydedilen video dosyasının, UI'da görüntülenmek üzere dosya yolu ve alt klasör bilgilerini içeren bir önizlemesi. | PREVIEW_VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/tr.md)

---
**Source fingerprint (SHA-256):** `39b168eab2d6798adfec6ace3d4320f26217d893844ba54e62041cfdf0183e6f`
