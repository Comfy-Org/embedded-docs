RegexReplace düğümü, düzenli ifade kalıpları kullanarak metinlerde arama ve değiştirme işlemi yapar. Metin kalıplarını aramanıza ve bunları yeni metinle değiştirmenize olanak tanır. Büyük/küçük harf duyarlılığı, çok satırlı eşleştirme ve değiştirme sayısını sınırlama gibi kalıp eşleştirmeyi kontrol eden seçenekler sunar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `dize` | İçinde arama ve değiştirme yapılacak giriş metin dizesi | STRING | Evet | - |
| `regex_deseni` | Giriş dizesinde aranacak düzenli ifade kalıbı | STRING | Evet | - |
| `değiştir` | Eşleşen kalıpların yerine kullanılacak değiştirme metni | STRING | Evet | - |
| `büyük/küçük harf duyarsız` | Etkinleştirildiğinde, kalıp eşleştirmede büyük/küçük harf farkını yok sayar (varsayılan: True) | BOOLEAN | Hayır | - |
| `çok satırlı` | Etkinleştirildiğinde, ^ ve $ karakterlerinin tüm dizenin başlangıcı/bitişi yerine her satırın başlangıcında/bitişinde eşleşmesini sağlar (varsayılan: False) | BOOLEAN | Hayır | - |
| `nokta her şey` | Etkinleştirildiğinde, nokta (.) karakteri yeni satır karakterleri dahil herhangi bir karakterle eşleşir. Devre dışı bırakıldığında, noktalar yeni satırlarla eşleşmez (varsayılan: False) | BOOLEAN | Hayır | - |
| `sayı` | Yapılacak maksimum değiştirme sayısı. Tüm oluşumları değiştirmek için 0 olarak ayarlayın (varsayılan). Yalnızca ilk eşleşmeyi değiştirmek için 1, ilk iki eşleşme için 2 olarak ayarlayın, vb. (varsayılan: 0) | INT | Hayır | 0-100 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Belirtilen değiştirmelerin uygulandığı değiştirilmiş dize | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexReplace/tr.md)

---
**Source fingerprint (SHA-256):** `4a4d4b317ee23314a4ac26cf3b58a2cc904bfb8111608f88345c1014b801ea00`
