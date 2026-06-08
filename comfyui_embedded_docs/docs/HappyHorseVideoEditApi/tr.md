## Genel Bakış

HappyHorse modelini kullanarak bir videoyu metin talimatları veya referans görsellerle düzenleyin. Çıktı süresi 3-15 saniye arasındadır ve giriş videosuyla eşleşir; 15 saniyeden uzun girişler kısaltılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Model seçimi, istem, çözünürlük, en-boy oranı ve isteğe bağlı referans görsellerini içeren model yapılandırması. | DICT | Evet | Aşağıya bakın |
| `video` | Düzenlenecek video. | VIDEO | Evet | - |
| `tohum` | Üretim için kullanılacak tohum değeri (varsayılan: 0). | INT | Evet | 0 ile 2147483647 arası |
| `filigran` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: False). | BOOLEAN | Hayır | True / False |

### `model` Parametre Detayları

`model` parametresi aşağıdaki alanları içeren bir sözlüktür:

| Alan | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak HappyHorse video düzenleme modeli. | STRING | Evet | `"happyhorse-1.0-video-edit"` |
| `prompt` | Düzenleme talimatları veya stil aktarımı gereksinimleri. En az 1 karakter uzunluğunda olmalıdır. | STRING | Evet | - |
| `resolution` | Çıktı çözünürlüğü. | STRING | Evet | `"720P"`<br>`"1080P"` |
| `ratio` | En-boy oranı. Değiştirilmezse, giriş videosunun oranına yaklaşır. | STRING | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `reference_images` | Düzenlemeyi yönlendirmek için isteğe bağlı referans görselleri (image1, image2, image3, image4, image5). | DICT | Hayır | 0 ile 5 görsel arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Düzenlenmiş video çıktısı. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `af6747efbea1c65e4909d35dad009cbc2ffaad787d0f2031581c227deb9bf53c`
