# PikaTextToVideoNode2_2

Pika Text2Video v2.2 Düğümü, Pika API sürüm 2.2'ye bir metin istemi göndererek video oluşturur. Metin açıklamanızı, Pika'nın yapay zeka video oluşturma hizmetini kullanarak bir videoya dönüştürür. Bu düğüm, en boy oranı, süre ve çözünürlük dahil olmak üzere video oluşturma sürecinin çeşitli yönlerini özelleştirmenize olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt_text` | Videoda ne oluşturmak istediğinizi açıklayan ana metin açıklaması | STRING | Evet | - |
| `negative_prompt` | Oluşturulan videoda görünmesini istemediğiniz şeyleri açıklayan metin | STRING | Evet | - |
| `seed` | Tekrarlanabilir sonuçlar için oluşturmanın rastgeleliğini kontrol eden bir sayı | INT | Evet | - |
| `resolution` | Çıktı videosu için çözünürlük ayarı | STRING | Evet | - |
| `duration` | Saniye cinsinden videonun uzunluğu | INT | Evet | - |
| `aspect_ratio` | En boy oranı (genişlik / yükseklik) (varsayılan: 1,7777777777777777) | FLOAT | Hayır | 0,4 - 2,5 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Pika API'sinden döndürülen oluşturulmuş video dosyası | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaTextToVideoNode2_2/tr.md)

---
**Source fingerprint (SHA-256):** `b4287519f5d4cc4a1077a58fb13aa99697e3be038a0b382c4b4c9b0e53a0d8a8`
