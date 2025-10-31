> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/tr.md)

Bu düğüm, önceden var olan bir UUID kullanarak Recraft'ın Sonsuz Stil Kütüphanesi'nden bir stil seçmenize olanak tanır. Sağlanan stil tanımlayıcısına dayanarak stil bilgilerini alır ve diğer Recraft düğümlerinde kullanılmak üzere döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `stil_kimliği` | STRING | Evet | Geçerli herhangi bir UUID | Sonsuz Stil Kütüphanesi'nden stil UUID'si. |

**Not:** `style_id` girdisi boş olamaz. Boş bir dize sağlanırsa, düğüm bir istisna oluşturacaktır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | Recraft'ın Sonsuz Stil Kütüphanesi'nden seçilen stil nesnesi |