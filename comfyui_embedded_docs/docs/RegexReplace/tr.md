> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexReplace/tr.md)

RegexReplace düğümü, düzenli ifade kalıpları kullanarak metinlerde arama ve değiştirme işlemi yapar. Metin kalıplarını aramanıza ve bunları yeni metinle değiştirmenize olanak tanır. Büyük/küçük harf duyarlılığı, çok satırlı eşleştirme ve değiştirme sayısını sınırlama gibi kalıp eşleştirmeyi kontrol eden seçenekler sunar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `string` | STRING | Evet | - | İçinde arama ve değiştirme yapılacak giriş metin dizesi |
| `regex_pattern` | STRING | Evet | - | Giriş dizesinde aranacak düzenli ifade kalıbı |
| `replace` | STRING | Evet | - | Eşleşen kalıpların yerine kullanılacak değiştirme metni |
| `case_insensitive` | BOOLEAN | Hayır | - | Etkinleştirildiğinde, kalıp eşleştirmede büyük/küçük harf farkını yok sayar (varsayılan: True) |
| `multiline` | BOOLEAN | Hayır | - | Etkinleştirildiğinde, ^ ve $ karakterlerinin tüm dizenin başlangıcı/bitişi yerine her satırın başlangıcında/bitişinde eşleşmesini sağlar (varsayılan: False) |
| `dotall` | BOOLEAN | Hayır | - | Etkinleştirildiğinde, nokta (.) karakteri yeni satır karakterleri dahil herhangi bir karakterle eşleşir. Devre dışı bırakıldığında, noktalar yeni satırlarla eşleşmez (varsayılan: False) |
| `count` | INT | Hayır | 0-100 | Yapılacak maksimum değiştirme sayısı. Tüm oluşumları değiştirmek için 0 olarak ayarlayın (varsayılan). Yalnızca ilk eşleşmeyi değiştirmek için 1, ilk iki eşleşme için 2 olarak ayarlayın, vb. (varsayılan: 0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | STRING | Belirtilen değiştirmelerin uygulandığı değiştirilmiş dize |

---
**Source fingerprint (SHA-256):** `4a4d4b317ee23314a4ac26cf3b58a2cc904bfb8111608f88345c1014b801ea00`
