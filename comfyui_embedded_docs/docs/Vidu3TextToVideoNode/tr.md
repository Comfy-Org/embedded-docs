# Vidu Q3 Metinden Videoya Üretim

Vidu Q3 Metinden Videoya Üretim düğümü, bir metin açıklamasından video oluşturur. İstemine dayalı video içeriği üretmek için Vidu Q3 Pro veya Q3 Turbo modelini kullanır; videonun uzunluğunu, çözünürlüğünü, en-boy oranını ve ses içerip içermediğini kontrol etmenize olanak tanır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video üretimi için kullanılacak model. Bir model seçmek, en-boy oranı, çözünürlük, süre ve ses için ek yapılandırma parametrelerini ortaya çıkarır. | COMBO | Evet | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `prompt` | Video üretimi için metin açıklaması; en fazla 2000 karakter olabilir. | STRING | Evet | N/A |
| `seed` | Üretimin rastgeleliğini kontrol etmek için kullanılan tohum değeri (varsayılan: 1). | INT | Evet | 0 ila 2147483647 |

### viduq3-pro ve viduq3-turbo Girdileri

Aşağıdaki yapılandırma parametreleri `viduq3-pro` ve `viduq3-turbo` modellerinde ortaktır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model.aspect_ratio` | Çıktı videosunun en-boy oranı. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `model.resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `model.duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 1 ila 16 |
| `model.audio` | Etkinleştirildiğinde, videoyu sesli (diyalog ve ses efektleri dahil) olarak çıkarır (varsayılan: False). | BOOLEAN | Evet | True/False |

**Not:** Bir `model` seçildiğinde `aspect_ratio`, `resolution`, `duration` ve `audio` parametreleri zorunludur; çünkü bunlar model yapılandırmasının parçasıdır. `prompt` boş olmamalı ve 2000 karakteri aşmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `89c23454375a43cdfaf46c9e0e55a8a8166d02ada47ca2e237bd9f73fa4d78db`
