Bu düğüm, koşullandırma bağlamı içinde belirli alanlar ayarlayarak koşullandırma bilgilerini değiştirmek için tasarlanmıştır. Koşullandırma öğelerinin hassas uzamsal manipülasyonuna olanak tanır ve belirtilen boyutlar ile güce dayalı olarak hedefli ayarlamalar ve iyileştirmeler yapılmasını sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Değiştirilecek koşullandırma verisi. Uzamsal ayarlamaların uygulanması için temel görevi görür. | CONDITIONING |
| `genişlik` | Koşullandırma bağlamı içinde ayarlanacak alanın genişliğini belirtir ve ayarlamanın yatay kapsamını etkiler. | `INT` |
| `yükseklik` | Ayarlanacak alanın yüksekliğini belirler ve koşullandırma değişikliğinin dikey kapsamını etkiler. | `INT` |
| `x` | Ayarlanacak alanın yatay başlangıç noktasıdır ve ayarlamayı koşullandırma bağlamı içinde konumlandırır. | `INT` |
| `y` | Alan ayarlaması için dikey başlangıç noktasıdır ve koşullandırma bağlamı içindeki konumunu belirler. | `INT` |
| `güç` | Belirtilen alan içindeki koşullandırma değişikliğinin yoğunluğunu tanımlar ve ayarlamanın etkisi üzerinde incelikli kontrol sağlar. | `FLOAT` |

## Çıkışlar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Belirtilen alan ayarlarını ve düzenlemelerini yansıtan, değiştirilmiş koşullandırma verisi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetArea/tr.md)
