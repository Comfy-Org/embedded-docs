> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/tr.md)

## Genel Bakış

HappyHorse modelini kullanarak metin talimatları veya referans görselleriyle video düzenleyin. Çıktı süresi, giriş videosuyla eşleşir (3-15 saniye) ve 15 saniyeden uzun girişler otomatik olarak kısaltılır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | DICT | Evet | Aşağıya bakın | Model seçimi, istem, çözünürlük, en-boy oranı ve isteğe bağlı referans görsellerini içeren model yapılandırması. |
| `video` | VIDEO | Evet | - | Düzenlenecek video. |
| `seed` | INT | Evet | 0 ile 2147483647 arası | Üretim için kullanılacak tohum değeri (varsayılan: 0). |
| `watermark` | BOOLEAN | Hayır | True / False | Sonuca yapay zeka tarafından oluşturulmuş filigran eklenip eklenmeyeceği (varsayılan: False). |

### `model` Parametre Detayları

`model` parametresi, aşağıdaki alanları içeren bir sözlüktür:

| Alan | Veri Türü | Zorunlu | Aralık | Açıklama |
|-------|-----------|----------|-------|-------------|
| `model` | STRING | Evet | `"happyhorse-1.0-video-edit"` | Kullanılacak HappyHorse video düzenleme modeli. |
| `prompt` | STRING | Evet | - | Düzenleme talimatları veya stil aktarımı gereksinimleri. En az 1 karakter uzunluğunda olmalıdır. |
| `resolution` | STRING | Evet | `"720P"`<br>`"1080P"` | Çıktı çözünürlüğü. |
| `ratio` | STRING | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | En-boy oranı. Değiştirilmezse, giriş videosunun oranına yaklaşır. |
| `reference_images` | DICT | Hayır | 0 ile 5 görsel arası | Düzenlemeyi yönlendirmek için isteğe bağlı referans görselleri (image1, image2, image3, image4, image5). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Düzenlenmiş video çıktısı. |