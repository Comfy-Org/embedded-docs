# Anahtar

If/Else Switch düğümü, bir boolean koşula göre iki olası girdi arasında seçim yapar. `switch` etkinleştirildiğinde (true), `on_true` girdisini çıktıya aktarır; devre dışı bırakıldığında (false), `on_false` girdisini aktarır. Girdiler tembel (lazy) yapıdadır; bu nedenle yalnızca seçilen dal değerlendirilir ve diğer girdinin bağlanması gerekmez.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `anahtar` | Çıktıya hangi girdinin aktarılacağını belirleyen bir boolean koşul. Etkinleştirildiğinde (true), `on_true` girdisi seçilir. Devre dışı bırakıldığında (false), `on_false` girdisi seçilir. | BOOLEAN | Evet |  |
| `yanlışta` | `switch` devre dışı bırakıldığında (false) çıktıya aktarılacak veri. Bu girdi yalnızca `switch` false olduğunda istenir. | MATCH_TYPE | Hayır |  |
| `doğruda` | `switch` etkinleştirildiğinde (true) çıktıya aktarılacak veri. Bu girdi yalnızca `switch` true olduğunda istenir. | MATCH_TYPE | Hayır |  |

**Girdi Gereksinimleri Hakkında Not:** `on_false` ve `on_true` girdileri koşullu olarak istenir. Düğüm, `on_true` girdisini yalnızca `switch` true olduğunda ister; `on_false` girdisini ise yalnızca `switch` false olduğunda ister. Her iki girdi de aynı veri türünde olmalıdır ve bu tür çıktı veri türüyle eşleşmelidir. Seçilen girdi bağlı değilse düğüm herhangi bir değer çıktılamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Seçilen veri: `switch` true olduğunda `on_true` değeri veya `switch` false olduğunda `on_false` değeri. | MATCH_TYPE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/tr.md)

---
**Source fingerprint (SHA-256):** `42c442efeda0197d950702c52647233dee1a30216fb07e1ce4bc844784a6c5f2`
