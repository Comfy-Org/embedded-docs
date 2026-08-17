# Videoyu Kaydet

SaveVideo düğümü, girdi olarak aldığı videoyu ComfyUI çıktı dizininize kaydeder. Dosya adı önekini, video biçimini ve codec'i seçmenize olanak tanır ve bir sayaç ekleyerek otomatik olarak benzersiz bir dosya adı oluşturur. Varsayılan olarak düğüm, kaydedilen videoya iş akışı meta verilerini de ekler.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `codec` | Video için kullanılacak codec. `h264` seçildiğinde ek kodlama seçenekleri görüntülenir (varsayılan: "auto"). | DYNAMIC_COMBO | Evet | "auto"<br>"h264" |
| `video` | Kaydedilecek video. | VIDEO | Evet | - |
| `filename_prefix` | Kaydedilecek dosyanın öneki. Düğümlerden değerler dahil etmek için `%date:yyyy-MM-dd%` veya `%Empty Latent Image.width%` gibi biçimlendirme bilgileri içerebilir (varsayılan: "video/ComfyUI"). | STRING | Evet | - |
| `format` | Videonun kaydedileceği biçim. Kaydedilen videonun dosya uzantısını belirler (varsayılan: "auto"). | COMBO | Evet | "auto"<br>"mp4"<br>"webm"<br>"mkv"<br>"gif" |

### h264 Girdileri

Bu girdiler, `codec` değeri `h264` olarak ayarlandığında görüntülenir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `encoding` | H.264 için kodlama modu. Otomatik, uyumlu H.264 akışlarını korur. Yeniden kodlama, özel bir CRF uygular (varsayılan: "auto"). | DYNAMIC_COMBO | Hayır | "auto"<br>"re-encode" |
| `crf` | Daha düşük değerler daha yüksek kalite ve daha büyük dosyalar üretir. Yalnızca `encoding` değeri `re-encode` olarak ayarlandığında kullanılabilir (varsayılan: 23.0). | FLOAT | Evet (yalnızca `encoding` değeri `re-encode` olduğunda) | 0.0 to 51.0 (step: 1.0) |

Not: `filename_prefix` klasörler içeriyorsa, örneğin `video/ComfyUI`, video çıktı dizininin bu alt klasörüne kaydedilir. Dosya adı, öneke eklenen bir sayaçla oluşturulur, örneğin `ComfyUI_00001_.mp4`, böylece mevcut dosyaların üzerine yazılmaz.

Not: Meta veri etkinleştirildiğinde, düğüm iş akışı promptunu ve ek meta verileri kaydedilen videoya gömer. Meta veri, ComfyUI'yi `--disable-metadata` bağımsız değişkeniyle başlatarak devre dışı bırakılabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Kaydedilen video; girdiden doğrudan aktarılır. | VIDEO |
| `ui` | Arayüzde görüntülenmek üzere dosya yolu ve alt klasör bilgilerini içeren kaydedilen video dosyasının önizlemesi. | PREVIEW_VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/tr.md)

---
**Source fingerprint (SHA-256):** `c1fd5ac1043f0811951136b2d09cd59840b0c542079da9ed04c17cca7c02562b`
