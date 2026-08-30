# Videoyu Kaydet

Save Video düğümü, girdi videosunu ComfyUI çıktı dizininize kaydeder. Dosya adı önekini, kapsayıcı biçimini, video codec'ini ve kalite gibi kodlama seçeneklerini seçebilirsiniz. Düğüm, bir sayaç kullanarak otomatik olarak benzersiz bir dosya adı oluşturur ve kaydedilen dosyaya iş akışı meta verilerini gömebilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Kaydedilecek video. | VIDEO | Evet | - |
| `dosyaadı_öneki` | Kaydedilecek dosyanın öneki. Bu, düğümlerden değer eklemek için `%date:yyyy-MM-dd%` veya `%Empty Latent Image.width%` gibi biçimlendirme bilgileri içerebilir (varsayılan: `video/ComfyUI`). | STRING | Evet | - |
| `format` | Çıktı kapsayıcısı. Auto, Auto/H.264 için MP4 ve AV1 için WebM kullanır. MP4, MKV ve WebM belirli bir kapsayıcı seçer. Bir biçim seçmek ayrıca hangi codec seçeneklerinin kullanılabilir olduğunu da belirler (varsayılan: `auto`). | DYNAMIC_COMBO | Evet | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"` |
| `codec` | Çıktı video codec'i. Auto, uyumlu bir kaynak akışı korur. H.264 ve AV1 yeniden kodlaması SDR, HDR (HLG) ve HDR PQ destekler. Bir biçim seçildikten sonra görünür (varsayılan: `auto`). | DYNAMIC_COMBO | Hayır | `"auto"`<br>`"h264"`<br>`"av1"` |

### H.264 Girdileri

Bu girdiler, `codec` `"h264"` olduğunda görünür ve `auto`, `mp4` ve `mkv` biçimleriyle kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `encoding` | Automatic, uyumlu H.264 akışlarını korur. Re-encode, özel kodlama seçeneklerini uygular. | DYNAMIC_COMBO | Hayır | `"auto"`<br>`"re-encode"` |
| `crf` | Daha düşük değerler daha yüksek kalite ve daha büyük dosyalar üretir. `encoding` `"re-encode"` olduğunda görünür (varsayılan: 23.0). | FLOAT | Hayır | 0.0 - 51.0 |

### AV1 Girdileri

Bu girdiler, `codec` `"av1"` olduğunda görünür ve `auto`, `mp4`, `mkv` ve `webm` biçimleriyle kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `encoding` | Automatic, uyumlu AV1 akışlarını korur. Re-encode, özel kodlama seçeneklerini uygular. | DYNAMIC_COMBO | Hayır | `"auto"`<br>`"re-encode"` |
| `crf` | Daha düşük değerler daha yüksek kalite ve daha büyük dosyalar üretir. `encoding` `"re-encode"` olduğunda görünür (varsayılan: 30.0). | FLOAT | Hayır | 0.0 - 63.0 |

Not: `format` `"auto"` olduğunda, kaydedilen kapsayıcı otomatik olarak seçilir: `av1` WebM üretirken, `auto` ve `h264` MP4 üretir. `webm` biçimi yalnızca `auto` ve `av1` codec'lerine izin verir. `codec` `"auto"` olduğunda, kaynak video akışı yeniden kodlanmak yerine korunur. Kaydedilen dosya, mevcut dosyaların üzerine yazılmasını önlemek için bir sayaç soneki kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Değiştirilmemiş girdi videosu. | VIDEO |
| `ui` | Kaydedilen video dosyasının, UI'da görüntülenmek üzere dosya yolu ve alt klasör bilgilerini içeren bir önizlemesi. | PREVIEW_VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/tr.md)

---
**Source fingerprint (SHA-256):** `8078f692b5c366447a1b08f351637baff901e489f2389e7a26c945661f75c37a`
