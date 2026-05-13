> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/tr.md)

## Genel Bakış

HappyHorse modelini kullanarak bir videoyu metin talimatları veya referans görsellerle düzenleyin. Çıktı süresi 3-15 saniye arasındadır ve giriş videosuyla eşleşir; 15 saniyeden uzun girişler kısaltılır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | DICT | Evet | Aşağıya bakın | Model seçimi, istem, çözünürlük, en-boy oranı ve isteğe bağlı referans görsellerini içeren model yapılandırması. |
| `video` | VIDEO | Evet | - | Düzenlenecek video. |
| `tohum` | INT | Evet | 0 ile 2147483647 arası | Üretim için kullanılacak tohum değeri (varsayılan: 0). |
| `filigran` | BOOLEAN | Hayır | True / False | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: False). |

### `model` Parametre Detayları

`model` parametresi aşağıdaki alanları içeren bir sözlüktür:

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

---
**Source fingerprint (SHA-256):** `af6747efbea1c65e4909d35dad009cbc2ffaad787d0f2031581c227deb9bf53c`
