> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetArea/tr.md)

Bu düğüm, koşullandırma bağlamı içinde belirli alanları ayarlayarak koşullandırma bilgisini değiştirmek için tasarlanmıştır. Koşullandırma öğelerinin hassas uzamsal manipülasyonuna olanak tanıyarak, belirtilen boyutlar ve güce dayalı hedefli ayarlamalar ve iyileştirmeler yapılmasını sağlar.

## Girdiler

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Değiştirilecek koşullandırma verisi. Uzamsal ayarlamaların uygulanması için temel oluşturur. |
| `genişlik`   | `INT`      | Koşullandırma bağlamı içinde ayarlanacak alanın genişliğini belirtir ve ayarın yatay kapsamını etkiler. |
| `yükseklik`  | `INT`      | Ayarlanacak alanın yüksekliğini belirler ve koşullandırma değişikliğinin dikey kapsamını etkiler. |
| `x`       | `INT`      | Ayarlanacak alanın yatay başlangıç noktasıdır ve ayarı koşullandırma bağlamı içinde konumlandırır. |
| `y`       | `INT`      | Alan ayarı için dikey başlangıç noktasıdır ve koşullandırma bağlamı içindeki konumunu belirler. |
| `güç`| `FLOAT`    | Belirtilen alan içindeki koşullandırma değişikliğinin yoğunluğunu tanımlar ve ayarın etkisi üzerinde nüanslı kontrol sağlar. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Belirtilen alan ayarlarını ve düzenlemeleri yansıtan, değiştirilmiş koşullandırma verisi. |