OpenAI API'si için girdi dosyalarını yükler ve biçimlendirir. Bu düğüm, OpenAI Sohbet Düğümü için bağlam girdileri olarak dahil edilmek üzere metin (.txt) ve PDF (.pdf) dosyalarını hazırlar. Dosyalar, yanıt oluşturulurken OpenAI modeli tarafından okunacaktır. Tek bir mesaja birden fazla dosya eklemek için birden çok OpenAI Girdi Dosyaları düğümü birbirine zincirlenebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `dosya` | Model için bağlam olarak eklenecek girdi dosyaları. Şimdilik yalnızca metin (.txt) ve PDF (.pdf) dosyalarını kabul eder. Dosyalar 32MB'tan küçük olmalıdır. | COMBO | Evet | Birden çok seçenek mevcut (girdi dizinindeki 32MB altındaki tüm .txt ve .pdf dosyaları) |
| `OPENAI_GİRDİ_DOSYALARI` | Bu düğümden yüklenen dosyayla birlikte toplu olarak işlenecek isteğe bağlı ek dosya(lar). Tek bir mesajın birden fazla girdi dosyası içerebilmesi için girdi dosyalarının zincirlenmesine olanak tanır. | OPENAI_INPUT_FILES | Hayır | Yok |

**Dosya Kısıtlamaları:**

- Yalnızca .txt ve .pdf dosyaları desteklenir
- Maksimum dosya boyutu: 32MB
- Dosyalar ComfyUI girdi dizininden yüklenir

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `OPENAI_GİRDİ_DOSYALARI` | OpenAI API çağrıları için bağlam olarak kullanılmaya hazır, biçimlendirilmiş girdi dosyaları. | OPENAI_INPUT_FILES |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIInputFiles/tr.md)

---
**Source fingerprint (SHA-256):** `e5e92f6628072da9af787867e38c89dde3db853b7289ef6c607a066cd04c1cc9`
