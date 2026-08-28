# FishAudioInstantVoiceClone

Bu düğüm, Fish Audio API'sini kullanarak ses kayıtlarınızdan özel bir klonlanmış ses oluşturur. Bir veya daha fazla ses örneği sağlarsınız ve düğüm, metin-konuşma için hemen kullanılabilecek özel bir ses oluşturur. 1 ila 20 kayıt kabul eder; her biri için önerilen uzunluk 10 ila 30 saniyedir ve toplam sınır 270 saniyedir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `files` | Ses klonlama için ses kayıtları. Bu büyütülebilir bir girdidir: ses örneklerini sağlamak için bir veya daha fazla ses öğesi bağlayın (örneğin `audio_1`, `audio_2`, ...). | AUDIO | Evet | 1 ile 20 recordings |
| `enhance_audio_quality` | Eğitimden önce referans ses kalitesini iyileştirin (varsayılan: True). | BOOLEAN | Evet | True<br>False |

**Not:** Tüm referans seslerin birleşik toplam süresi 270 saniyenin altında olmalıdır. Toplam süre 270 saniyeye ulaşır veya aşarsa, düğüm bir hata döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `voice` | Yeni oluşturulan klonlanmış ses; Fish Audio API tarafından döndürülen benzersiz bir ses kimliğiyle tanımlanır. Bu ses, metin-konuşma için kullanılabilir. | FISHAUDIO_VOICE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioInstantVoiceClone/tr.md)

---
**Source fingerprint (SHA-256):** `6c4f011a4611a076b2488152591efeb61c029d6dfae2b079ba74689891c84803`
