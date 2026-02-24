> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsInstantVoiceClone/tr.md)

ElevenLabs Instant Voice Clone düğümü, bir kişinin sesine ait 1 ila 8 adet ses kaydını analiz ederek yeni ve benzersiz bir ses modeli oluşturur. Bu örnekleri ElevenLabs API'sine gönderir ve API, metinden sese sentez için kullanılabilecek bir ses klonu oluşturmak üzere bunları işler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `audio_*` | AUDIO | Evet | 1 ila 8 dosya | Ses klonlama için ses kayıtları. 1 ila 8 arasında ses dosyası sağlamanız gerekir. |
| `remove_background_noise` | BOOLEAN | Hayır | True / False | Ses izolasyonu kullanarak ses örneklerinden arka plan gürültüsünü kaldırır. (varsayılan: False) |

**Not:** En az bir ses dosyası sağlamanız gerekir ve en fazla sekiz dosya sağlayabilirsiniz. Düğüm, eklediğiniz ses dosyaları için otomatik olarak giriş yuvaları oluşturacaktır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `voice` | ELEVENLABS_VOICE | Yeni oluşturulan klonlanmış ses modeli için benzersiz tanımlayıcı. Bu çıkış, diğer ElevenLabs metinden sese düğümlerine bağlanabilir. |