# Matematiksel İfade

ComfyMathExpression düğümü, metin olarak yazdığınız bir matematiksel formülü değerlendirir. Formül, `a`, `b`, `c` gibi harf adlarını kullanarak düğümün giriş değerlerine başvurabilir ve genişletilebilir `values` grubu aracılığıyla ihtiyaç duyduğunuz kadar giriş değeri ekleyebilirsiniz. Hesaplama sonucu aynı anda kayan noktalı sayı, tamsayı ve boolean değer olarak döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `expression` | Değerlendirilecek matematiksel formül, metin olarak yazılır (örneğin `a + b`), giriş değerlerinin harf adlarını değişken olarak kullanır. Çok satırlı giriş. (varsayılan: "a + b") | STRING | Evet | N/A |
| `values` | İfade için değişkenleri sağlayan genişletilebilir giriş değerleri grubu. Gruba eklenen her değer otomatik olarak `a` ile başlayan bir sonraki küçük harf adını alır (`a`, `b`, `c`, ...) ve bu ad daha sonra `expression` içinde kullanılabilir. Her öğe bir sayı (INT veya FLOAT) ya da bir boolean (TRUE/FALSE) kabul eder. | FLOAT, INT, BOOLEAN | Evet | 1 ile 26 değer, `a` ile `z` olarak adlandırılır |

### Notlar ve kısıtlamalar

- `expression` boş olamaz veya yalnızca boşluk içeremez.
- İfade, sayısal bir sonuca (INT veya FLOAT) ya da bir boolean sonuca (TRUE/FALSE) değerlendirilmelidir. Boolean sonuçlar TRUE için 1, FALSE için 0 olarak işlenir. Sonuç farklı bir türdeyse, örneğin metin, düğüm bir hata verir.
- Sayısal sonuç sonlu olmalı ve float'a dönüştürülebilmelidir. Çok büyük veya sonlu olmayan sonuçlar hataya neden olur.
- Tüm giriş değerleri kümesi, ifade içinde `values` değişken adı altında (liste olarak) da kullanılabilir, bu nedenle `sum(values)` gibi ifadeler mümkündür.
- İfade içinde aşağıdaki matematik fonksiyonları kullanılabilir: `sum`, `min`, `max`, `abs`, `round`, `pow`, `sqrt`, `ceil`, `floor`, `log`, `log2`, `log10`, `sin`, `cos`, `tan`, `int`, `float`.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `FLOAT` | İfadenin kayan noktalı sayı olarak sonucu. | FLOAT |
| `INT` | İfadenin, ondalık kısmı atılarak tamsayıya dönüştürülmüş sonucu. | INT |
| `BOOL` | Boolean değerine dönüştürülmüş sonuç: sayısal sonuç sıfır değilse TRUE, sıfırsa FALSE. | BOOLEAN |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/tr.md)

---
**Source fingerprint (SHA-256):** `4c77e9834fe7341143352f95ed8808dc81def3361b197c67e33a531bb3696d71`
