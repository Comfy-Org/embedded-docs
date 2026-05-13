> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/tr.md)

ComfyMathExpression düğümü, bir dizi girdi değeri kullanarak matematiksel bir formülü değerlendirir. Değişken adları (örneğin `a`, `b`, `c`) kullanarak bir ifade yazabilirsiniz ve düğüm sonucu hesaplar. Hesaplamanız için gerektiği kadar girdi değerini dinamik olarak eklemeyi destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ifade` | STRING | Evet | Yok | Değerlendirilecek matematiksel formül. Girdi değerlerine karşılık gelen değişken adlarını kullanabilirsiniz (varsayılan: "a + b"). |
| `değerler` | FLOAT, INT, BOOLEAN | Hayır | Yok | Dinamik olarak eklenebilen bir dizi sayısal veya boolean girdi. Her girdiye, ifadede değişken olarak kullanılmak üzere alfabeden bir harf (a, b, c, ...) atanır. |

**Parametre Kısıtlamaları:**
*   `expression` parametresi boş olamaz veya yalnızca boşluk karakterlerinden oluşamaz.
*   İfade, sonlu bir sayısal sonuç (INT veya FLOAT) vermelidir. Boolean veya diğer sayısal olmayan sonuçlar hataya neden olur.
*   `values` parametresi için girdi değerleri sayı (INT veya FLOAT) veya boolean değer (TRUE/FALSE) olabilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `FLOAT` | FLOAT | Matematiksel ifadenin kayan noktalı sayı olarak sonucu. |
| `BOOL` | INT | Matematiksel ifadenin tam sayı olarak sonucu. |
| `BOOL` | BOOLEAN | Matematiksel ifadenin boolean değer olarak sonucu. |

---
**Source fingerprint (SHA-256):** `962f82684d9dc58a67a57e6738d6d2ed457d7f30288cedb21fd46b5c655c1708`
