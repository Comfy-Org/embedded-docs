> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleFastNode/tr.md)

Görüntüleri Stability API çağrısı ile hızlı bir şekilde orijinal boyutunun 4 katına kadar büyütür. Bu düğüm, özellikle düşük kaliteli veya sıkıştırılmış görüntüleri Stability AI'nın hızlı büyütme servisine göndererek yeniden boyutlandırmak için tasarlanmıştır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Büyütülecek giriş görüntüsü |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Stability AI API'sinden dönen büyütülmüş görüntü |