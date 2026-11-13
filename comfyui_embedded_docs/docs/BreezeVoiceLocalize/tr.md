# Breeze Voice Localize

Başka bir dili ana dili gibi konuşan bir sesin kopyasını oluşturur; yabancı bir dili özgün aksanıyla okumak yerine. Kopya hesabınıza kaydedilir ve bir ses önizlemesiyle birlikte döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `voice` | Kopyalanacak Breeze sesi. | BREEZE_VOICE | Evet | - |
| `language` | Yeni sesin konuştuğu dil. Varsayılan: `"English"`. | COMBO | Evet | Birden çok seçenek mevcut |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Hayır | 0 ile 2147483647 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `voice` | Sesin, orijinal ses ve dile göre adlandırılmış yerelleştirilmiş kopyası. | BREEZE_VOICE |
| `preview` | Yerelleştirilmiş sesin ses önizlemesi. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceLocalize/tr.md)

---
**Source fingerprint (SHA-256):** `a997fbc3426669f6e5725c455f49f3e16d5e14806ea3fac26657459f63e99db1`
