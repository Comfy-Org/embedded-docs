Stability API çağrısıyla bir görüntüyü orijinal boyutunun 4 katına hızla yükseltir. Bu düğüm, özellikle düşük kaliteli veya sıkıştırılmış görüntüleri Stability AI'nın hızlı yükseltme hizmetine göndererek yükseltmek için tasarlanmıştır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Yükseltilecek giriş görüntüsü | IMAGE | Evet | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Stability AI API'sinden döndürülen yükseltilmiş görüntü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleFastNode/tr.md)

---
**Source fingerprint (SHA-256):** `0f349c6834807d43173e628abbee91a3a26f587f4bd5453443a9f5754ea8aeeb`
