# Breeze Voice Clone

Tek bir konuşmacının kaydından bir Breeze sesi oluşturur. Ses, hesabınıza kaydedilir ve nasıl duyulduğuna dair bir ses önizlemesiyle birlikte bir ses tanıtıcısı olarak döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `audio` | Tek konuşmacının kaydı, en az 3 saniye uzunluğunda. Yalnızca ilk 60 saniye kullanılır. | AUDIO | Evet | - |
| `remove_background_noise` | Klonlamadan önce kaydı temizler. Varsayılan: false. | BOOLEAN | Hayır | true<br>false |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Hayır | 0 ile 2147483647 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `voice` | Breeze Text to Speech için yeni Breeze sesi. | BREEZE_VOICE |
| `preview` | Klonlanan sesin ses önizlemesi. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceClone/tr.md)

---
**Source fingerprint (SHA-256):** `3c2e461a8e1a38bfa494a687f5b77a375e9e81c77964493181d7c622a682c56f`
