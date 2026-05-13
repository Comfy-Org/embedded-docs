> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaTextToVideoNode2_2/tr.md)

Pika Text2Video v2.2 Düğümü, Pika API sürüm 2.2'ye bir metin istemi göndererek video oluşturur. Metin açıklamanızı, Pika'nın yapay zeka video oluşturma hizmetini kullanarak bir videoya dönüştürür. Bu düğüm, en boy oranı, süre ve çözünürlük dahil olmak üzere video oluşturma sürecinin çeşitli yönlerini özelleştirmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | Evet | - | Videoda ne oluşturmak istediğinizi açıklayan ana metin açıklaması |
| `negative_prompt` | STRING | Evet | - | Oluşturulan videoda görünmesini istemediğiniz şeyleri açıklayan metin |
| `seed` | INT | Evet | - | Tekrarlanabilir sonuçlar için oluşturmanın rastgeleliğini kontrol eden bir sayı |
| `resolution` | STRING | Evet | - | Çıktı videosu için çözünürlük ayarı |
| `duration` | INT | Evet | - | Saniye cinsinden videonun uzunluğu |
| `aspect_ratio` | FLOAT | Hayır | 0,4 - 2,5 | En boy oranı (genişlik / yükseklik) (varsayılan: 1,7777777777777777) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `output` | VIDEO | Pika API'sinden döndürülen oluşturulmuş video dosyası |

---
**Source fingerprint (SHA-256):** `b4287519f5d4cc4a1077a58fb13aa99697e3be038a0b382c4b4c9b0e53a0d8a8`
