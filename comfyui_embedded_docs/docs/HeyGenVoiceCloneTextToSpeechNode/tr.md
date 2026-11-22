# HeyGen Voice 1.0 Instant Clone Text to Speech

HeyGen Voice 1.0 ile tek bir konuşmacının kaydından ses klonlayın ve metni o sesle konuşun. Düğüm kaydı yükler, konuşmayı sentezler ve ses olarak döndürür; böylece tek bir düğüm ses örneğinden tamamlanmış konuşmaya gider.

`model` seçimi, ona özgü parametreleri ortaya çıkarır: `audio`, `text`, `language`, `expressiveness_boost`, `recording_language`, `similarity`, `remove_background_noise` ve `seed`.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. `heygen-voice-1-turbo` daha hızlıdır ve daha az maliyetlidir (varsayılan: `"heygen-voice-1"`). | DYNAMIC_COMBO | Evet | `"heygen-voice-1"`<br>`"heygen-voice-1-turbo"` |
| `audio` | Klonlanacak tek bir konuşmacının kaydı. En az 10 saniye net konuşma kullanın; yalnızca ilk 3 dakika kullanılır. | AUDIO | Evet | - |
| `text` | Konuşulacak metin, en fazla 5000 karakter. Yaklaşık 12 dakikadan uzun konuşmalar başarısız olur, bu nedenle çok uzun Çince veya Japonca metinleri bölün (varsayılan: boş). | STRING | Evet | 1 ile 5000 karakter arası |
| `language` | Metnin dili. Sırpça veya Malayca gibi otomatik algılamanın karıştırabileceği yakından ilişkili diller için ayarlayın (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>Çoklu dil ön ayarları |
| `expressiveness_boost` | Daha yüksek değerler daha ifade edici; daha düşük değerler orijinal sese daha yakın kalır (varsayılan: 0.5). | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.05) |
| `recording_language` | Kayıtta konuşulan dil, klonu o dile daraltır (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>Çoklu dil ön ayarları |
| `similarity` | Sesin kayda ne kadar yakından uyduğu (varsayılan: `"max"`). | COMBO | Evet | `"medium"`<br>`"high"`<br>`"extra_high"`<br>`"max"` |
| `remove_background_noise` | Klonlamadan önce kayıttaki arka plan gürültüsünü temizleyin (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |
| `seed` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

`text` en az bir karakter içermelidir ve `audio` gereklidir: birden çok konuşmacının kaydı veya klonlamak için çok gürültülü olan bir kayıt kötü ses verir. Örnekteki dil açık değilse `recording_language` ayarlayın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `AUDIO` | Klonlanmış seste konuşulan metin. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceCloneTextToSpeechNode/tr.md)

---
**Source fingerprint (SHA-256):** `ea18e2abce687e106ed0b37eb7afd723fbe72a3b4d58124a143c00b66d2fe7c9`
