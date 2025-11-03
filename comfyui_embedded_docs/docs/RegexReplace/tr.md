> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexReplace/tr.md)

RegexReplace düğümü, metin dizilerinde düzenli ifade desenleri kullanarak metin bulma ve değiştirme işlemleri yapar. Metin desenlerini aramanıza ve bunları yeni metinle değiştirmenize olanak tanır; büyük/küçük harf duyarlılığı, çok satırlı eşleştirme ve değiştirme sayısını sınırlama gibi desen eşleştirme işlemlerinin nasıl çalışacağını kontrol etme seçenekleri sunar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Evet | - | İçinde arama ve değiştirme yapılacak giriş metin dizisi |
| `regex_pattern` | STRING | Evet | - | Giriş dizisi içinde aranacak düzenli ifade deseni |
| `replace` | STRING | Evet | - | Eşleşen desenlerin yerine konulacak değiştirme metni |
| `case_insensitive` | BOOLEAN | Hayır | - | Etkinleştirildiğinde, desen eşleştirmenin büyük/küçük harf farklarını yok saymasını sağlar (varsayılan: True) |
| `multiline` | BOOLEAN | Hayır | - | Etkinleştirildiğinde, ^ ve $ karakterlerinin davranışını, tüm dizinin yalnızca başlangıcı/sonu yerine her satırın başlangıcı/sonunda eşleşecek şekilde değiştirir (varsayılan: False) |
| `dotall` | BOOLEAN | Hayır | - | Etkinleştirildiğinde, nokta (.) karakteri yeni satır karakterleri de dahil olmak üzere herhangi bir karakterle eşleşir. Devre dışı bırakıldığında, noktalar yeni satırlarla eşleşmez (varsayılan: False) |
| `count` | INT | Hayır | 0-100 | Yapılacak maksimum değiştirme sayısı. Tüm oluşumları değiştirmek için 0 olarak ayarlayın (varsayılan). Yalnızca ilk eşleşmeyi değiştirmek için 1, ilk iki eşleşme için 2, vb. olarak ayarlayın (varsayılan: 0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Belirtilen değiştirmelerin uygulandığı değiştirilmiş dizi |