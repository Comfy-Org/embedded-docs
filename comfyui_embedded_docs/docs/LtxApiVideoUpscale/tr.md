# LTX Video Upscale

Yükseltilecek videoyu en-boy oranını, kare hızını ve sesi koruyarak 1080p, 4K veya 8K'ya yükseltir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Yükseltilecek video; kısa kenarı en az 480 piksel olmalı ve her iki yönde de en fazla 7680x4320 olmalıdır. 1080p için 2401 kareye, 4K için 601 kareye ve 8K için 241 kareye kadar. | VIDEO | Evet | - |
| `resolution` | Çıktı boyutu; 1920x1080, 3840x2160 veya 7680x4320 içine sığabilecek en büyük boyut olarak ve dikey videolar için çevrilerek. Varsayılan: `"4k"`. | COMBO | Evet | `"1080p"`<br>`"4k"`<br>`"8k"` |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Hayır | 0 ile 4294967295 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Ses korunarak yükseltilmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoUpscale/tr.md)

---
**Source fingerprint (SHA-256):** `e9b3b760365568ab2f6572c5f4f28758d67c4f5795fc39716ed4f648aafef80e`
