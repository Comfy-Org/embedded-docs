> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/tr.md)

Luma Text to Video ve Luma Image to Video düğümleriyle kullanılmak üzere bir veya daha fazla Kamera Konsepti tutar. Bu düğüm, en fazla dört kamera konsepti seçmenize ve isteğe bağlı olarak bunları mevcut konsept zincirleriyle birleştirmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `concept1` | STRING | Evet | Birden fazla seçenek mevcut<br>"None" seçeneği dahil | Mevcut Luma konseptlerinden ilk kamera konsepti seçimi |
| `concept2` | STRING | Evet | Birden fazla seçenek mevcut<br>"None" seçeneği dahil | Mevcut Luma konseptlerinden ikinci kamera konsepti seçimi |
| `concept3` | STRING | Evet | Birden fazla seçenek mevcut<br>"None" seçeneği dahil | Mevcut Luma konseptlerinden üçüncü kamera konsepti seçimi |
| `concept4` | STRING | Evet | Birden fazla seçenek mevcut<br>"None" seçeneği dahil | Mevcut Luma konseptlerinden dördüncü kamera konsepti seçimi |
| `luma_concepts` | LUMA_CONCEPTS | Hayır | Yok | Burada seçilenlere eklemek için isteğe bağlı Kamera Konseptleri |

**Not:** Dört konsept yuvasının tamamını kullanmak istemiyorsanız, tüm konsept parametreleri (`concept1` ila `concept4`) "None" olarak ayarlanabilir. Düğüm, sağlanan `luma_concepts` değerlerini seçilen konseptlerle birleştirerek kombine bir konsept zinciri oluşturacaktır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `luma_concepts` | LUMA_CONCEPTS | Seçilen tüm konseptleri içeren birleştirilmiş kamera konsepti zinciri |