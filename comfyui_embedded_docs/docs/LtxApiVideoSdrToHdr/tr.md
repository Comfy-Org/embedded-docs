# LTX Video SDR to HDR

Bir SDR videosunu, aynı çözünürlükte, HLG transfer fonksiyonuna sahip BT.2020 içinde 10 bit HDR videosuna dönüştürür. Ses korunmaz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Dönüştürülecek SDR video; her iki yönde de en fazla 3840x2160. 1080p'de en fazla 273 kare, 1440p'de 193 kare ve 4K'da 65 kare. | VIDEO | Evet | - |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Hayır | 0 ile 4294967295 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Dönüştürülen 10 bit HDR video, ses olmadan. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoSdrToHdr/tr.md)

---
**Source fingerprint (SHA-256):** `e5c0ef901f504a9477f042b4aef24935f4b85da52ccfaddfc764e9efec490915`
