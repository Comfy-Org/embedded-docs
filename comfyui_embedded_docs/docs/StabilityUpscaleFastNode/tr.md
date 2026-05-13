> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleFastNode/tr.md)

Stability API çağrısıyla bir görüntüyü orijinal boyutunun 4 katına hızla yükseltir. Bu düğüm, özellikle düşük kaliteli veya sıkıştırılmış görüntüleri Stability AI'nın hızlı yükseltme hizmetine göndererek yükseltmek için tasarlanmıştır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Yükseltilecek giriş görüntüsü |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Stability AI API'sinden döndürülen yükseltilmiş görüntü |

---
**Source fingerprint (SHA-256):** `0f349c6834807d43173e628abbee91a3a26f587f4bd5453443a9f5754ea8aeeb`
