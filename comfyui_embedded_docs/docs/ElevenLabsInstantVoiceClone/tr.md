ElevenLabs Anlık Ses Klonlama düğümü, bir kişinin sesine ait 1 ila 8 ses kaydını analiz ederek yeni ve benzersiz bir ses modeli oluşturur. Bu örnekleri ElevenLabs API'sine gönderir; API, bunları işleyerek metin-konuşma sentezinde kullanılabilecek bir ses klonu oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `audio_*` | Ses klonlama için ses kayıtları. 1 ile 8 arasında ses dosyası sağlamanız gerekir. | AUDIO | Evet | 1 ila 8 dosya |
| `arka_plan_gürültüsünü_kaldır` | Ses izolasyonu kullanarak ses örneklerindeki arka plan gürültüsünü kaldırır. (varsayılan: False) | BOOLEAN | Hayır | True / False |

**Not:** En az bir ses dosyası sağlamanız gerekir ve en fazla sekiz dosya sağlayabilirsiniz. Düğüm, eklediğiniz ses dosyaları için otomatik olarak giriş yuvaları oluşturacaktır.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `voice` | Yeni oluşturulan klonlanmış ses modeli için benzersiz tanımlayıcı. Bu çıkış, diğer ElevenLabs metin-konuşma düğümlerine bağlanabilir. | ELEVENLABS_VOICE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsInstantVoiceClone/tr.md)

---
**Source fingerprint (SHA-256):** `297598e183df3ccddabc75d6903c5c69f10648adeea430e546f9c5f6df49bdb2`
