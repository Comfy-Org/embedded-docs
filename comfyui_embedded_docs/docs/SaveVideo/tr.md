# Videoyu Kaydet

Save Video düğümü, giriş videosunu ComfyUI çıktı dizininize kaydeder. Dosya adı ön ekini, kapsayıcı biçimini, video kodeğini ve kalite gibi kodlama seçeneklerini seçebilirsiniz. Düğüm, bir sayaç kullanarak otomatik olarak benzersiz bir dosya adı oluşturur ve kaydedilen dosyaya iş akışı meta verilerini gömebilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Kaydedilecek video. | VIDEO | Evet | - |
| `dosyaadı_öneki` | Kaydedilecek dosyanın ön eki. Düğümlerden gelen değerleri dahil etmek için `%date:yyyy-MM-dd%` veya `%Empty Latent Image.width%` gibi biçimlendirme bilgileri içerebilir (varsayılan: `video/ComfyUI`). | STRING | Evet | - |
| `format` | Çıktı kapsayıcısı. Otomatik, Otomatik/H.264 için MP4 ve AV1 için WebM kullanır. MP4, MKV ve WebM belirli bir kapsayıcı seçer. Bir biçim seçmek, hangi kodek seçeneklerinin kullanılabilir olduğunu da belirler (varsayılan: `auto`). | DYNAMIC_COMBO | Evet | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"` |
| `codec` | Çıktı video kodeği. Otomatik, uyumlu bir kaynak akışını korur. H.264 ve AV1 yeniden kodlama SDR, HDR (HLG) ve HDR PQ'yu destekler. Bu seçici, seçilen biçimin altında iç içe yer alır (varsayılan: `auto`). | DYNAMIC_COMBO | Hayır | `"auto"`<br>`"h264"`<br>`"av1"` (`webm` biçiminde kullanılamaz) |

### H.264 Girdileri

Bu girdiler, `codec` `"h264"` olduğunda görünür ve `auto`, `mp4` ve `mkv` biçimlerinde kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `encoding` | Otomatik, uyumlu H.264 akışlarını korur. Yeniden kodla, özel kodlama seçeneklerini uygular. | DYNAMIC_COMBO | Hayır | `"auto"`<br>`"re-encode"` |
| `crf` | Düşük değerler daha yüksek kalite ve daha büyük dosyalar üretir. `encoding` `"re-encode"` olduğunda görünür (varsayılan: 23.0). | FLOAT | Hayır | 0.0 - 51.0 |

### AV1 Girdileri

Bu girdiler, `codec` `"av1"` olduğunda görünür ve `auto`, `mp4`, `mkv` ve `webm` biçimlerinde kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `encoding` | Otomatik, uyumlu AV1 akışlarını korur. Yeniden kodla, özel kodlama seçeneklerini uygular. | DYNAMIC_COMBO | Hayır | `"auto"`<br>`"re-encode"` |
| `crf` | Düşük değerler daha yüksek kalite ve daha büyük dosyalar üretir. `encoding` `"re-encode"` olduğunda görünür (varsayılan: 30.0). | FLOAT | Hayır | 0.0 - 63.0 |

Not: `format` `"auto"` olduğunda, kaydedilen kapsayıcı otomatik olarak seçilir: `av1` WebM üretirken `auto` ve `h264` MP4 üretir. `webm` biçimi yalnızca `auto` ve `av1` kodeklerine izin verir. `codec` `"auto"` olduğunda, kaynak video akışı yeniden kodlanmak yerine korunur. Kaydedilen dosya, mevcut dosyaların üzerine yazılmasını önlemek için bir sayaç son eki kullanır. Dosya uzantısı, çözümlenen kapsayıcı tarafından belirlenir. Başlangıçta meta veri kaydetme devre dışı bırakılmadıkça, iş akışı meta verileri (istem ve ek düğüm bilgileri) kaydedilen dosyaya gömülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Giriş videosu, değiştirilmeden. | VIDEO |
| `ui` | Kaydedilen video dosyasının önizlemesi; kullanıcı arayüzünde görüntülemek için dosya yolu ve alt klasör bilgilerini içerir. | PREVIEW_VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/tr.md)

---
**Source fingerprint (SHA-256):** `8078f692b5c366447a1b08f351637baff901e489f2389e7a26c945661f75c37a`
