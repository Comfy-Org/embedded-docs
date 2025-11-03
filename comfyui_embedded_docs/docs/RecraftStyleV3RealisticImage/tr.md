> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/tr.md)

Bu düğüm, Recraft API'si ile kullanılmak üzere gerçekçi bir görüntü stili yapılandırması oluşturur. Gerçekçi görüntü stilini seçmenize ve çıktı görünümünü özelleştirmek için çeşitli alt stil seçenekleri arasından seçim yapmanıza olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `alt_stil` | STRING | Evet | Birden fazla seçenek mevcut | Gerçekçi görüntü stiline uygulanacak belirli alt stil. "None" olarak ayarlanırsa, hiçbir alt stil uygulanmaz. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | Gerçekçi görüntü stilini ve seçilen alt stil ayarlarını içeren bir Recraft stili yapılandırma nesnesi döndürür. |