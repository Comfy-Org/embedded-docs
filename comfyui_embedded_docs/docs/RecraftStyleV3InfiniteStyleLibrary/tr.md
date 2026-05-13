> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/tr.md)

Bu düğüm, önceden var olan bir UUID kullanarak Recraft'ın Sonsuz Stil Kütüphanesi'nden bir stil seçmenizi sağlar. Sağlanan stil tanımlayıcısına göre stil bilgisini alır ve diğer Recraft düğümlerinde kullanılmak üzere döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `style_id` | STRING | Evet | Geçerli herhangi bir UUID | Sonsuz Stil Kütüphanesi'ndeki stilin UUID'si. |

**Not:** `style_id` girişi boş olamaz. Boş bir dize sağlanırsa, düğüm bir istisna oluşturacaktır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | Recraft'ın Sonsuz Stil Kütüphanesi'nden seçilen stil nesnesi |

---
**Source fingerprint (SHA-256):** `37d7d9eff1232cc17912c6fca908dc5b8c404c0b6cf0a36e8fecc837ff2a1eea`
