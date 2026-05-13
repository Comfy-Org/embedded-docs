> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexExtract/tr.md)

RegexExtract düğümü, düzenli ifadeler kullanarak metin içinde desenler arar. İlk eşleşmeyi, tüm eşleşmeleri, eşleşmelerden belirli grupları veya birden çok eşleşme arasındaki tüm grupları bulabilir. Düğüm, büyük/küçük harf duyarlılığı, çok satırlı eşleştirme ve noktanın her şeyle eşleşmesi (dotall) gibi çeşitli regex bayraklarını destekler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `dize` | STRING | Evet | - | Desenlerin aranacağı giriş metni |
| `regex_deseni` | STRING | Evet | - | Aranacak düzenli ifade deseni |
| `mod` | COMBO | Evet | "İlk Eşleşme"<br>"Tüm Eşleşmeler"<br>"İlk Grup"<br>"Tüm Gruplar" | Çıkarma modu, eşleşmelerin hangi bölümlerinin döndürüleceğini belirler (varsayılan: "İlk Eşleşme") |
| `büyük/küçük harf duyarsız` | BOOLEAN | Hayır | - | Eşleştirme sırasında büyük/küçük harf farkının göz ardı edilip edilmeyeceği (varsayılan: True) |
| `çok satırlı` | BOOLEAN | Hayır | - | Dizenin birden çok satır olarak değerlendirilip değerlendirilmeyeceği (varsayılan: False) |
| `nokta her şey` | BOOLEAN | Hayır | - | Nokta (.) karakterinin yeni satırlarla eşleşip eşleşmeyeceği (varsayılan: False) |
| `grup_indeksi` | INT | Hayır | 0-100 | Grup modları kullanılırken çıkarılacak yakalama grubu dizini (varsayılan: 1) |

**Not:** "İlk Grup" veya "Tüm Gruplar" modları kullanılırken, `group_index` parametresi hangi yakalama grubunun çıkarılacağını belirtir. Grup 0 tüm eşleşmeyi temsil ederken, grup 1 ve üzeri regex deseninizdeki numaralandırılmış yakalama gruplarını temsil eder.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `output` | STRING | Seçilen mod ve parametrelere göre çıkarılan metin |

---
**Source fingerprint (SHA-256):** `38e365d21bea966ed65bc78c184766330924fe75392cdb88c6978052037f5d5f`
