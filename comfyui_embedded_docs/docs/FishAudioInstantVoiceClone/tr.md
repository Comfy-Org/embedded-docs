# Fish Audio Anında Ses Klonlama

Bu düğüm, Fish Audio API'sini kullanarak ses kayıtlarınızdan özel bir klonlanmış ses oluşturur. Bir veya daha fazla ses örneği sağlarsınız ve düğüm, metinden sese dönüşüm için hemen kullanılabilecek özel bir ses oluşturur. 1 ila 20 kayıt kabul eder; her biri için önerilen uzunluk 10 ila 30 saniyedir ve toplam sınır 270 saniyedir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `files` | Ses klonlama için ses kayıtları. Bu, genişletilebilir bir girdidir: ses örneklerini sağlamak için bir veya daha fazla ses öğesi (örneğin `audio_1`, `audio_2`, ...) bağlayın. | AUDIO | Evet | 1 ila 20 kayıt |
| `enhance_audio_quality` | Eğitimden önce referans ses kalitesini iyileştirin (varsayılan: True). | BOOLEAN | Evet | True<br>False |

**Not:** Tüm referans seslerin birleşik toplam süresi 270 saniyenin altında olmalıdır. Birleşik süre 270 saniyeye ulaşırsa veya bu süreyi aşarsa, düğüm bir hata döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `voice` | Fish Audio API'si tarafından döndürülen benzersiz bir ses kimliğiyle tanımlanan, yeni oluşturulmuş klonlanmış ses. Bu ses, metinden sese dönüşüm için kullanılabilir. | FISHAUDIO_VOICE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioInstantVoiceClone/tr.md)

---
**Source fingerprint (SHA-256):** `6c4f011a4611a076b2488152591efeb61c029d6dfae2b079ba74689891c84803`
