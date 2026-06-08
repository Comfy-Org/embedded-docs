ConditioningSetAreaPercentage düğümü, koşullandırma öğelerinin etki alanını yüzde değerlerine göre ayarlama konusunda uzmanlaşmıştır. Alanın boyutlarını ve konumunu toplam görüntü boyutunun yüzdesi olarak belirtmeye olanak tanır; ayrıca koşullandırma etkisinin yoğunluğunu ayarlamak için bir güç parametresi içerir.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Değiştirilecek koşullandırma öğelerini temsil eder; alan ve güç ayarlamalarının uygulanması için temel görevi görür. | CONDITIONING |
| `genişlik` | Alanın genişliğini toplam görüntü genişliğinin yüzdesi olarak belirtir; koşullandırmanın görüntüyü yatay olarak ne kadar etkileyeceğini belirler. | `FLOAT` |
| `yükseklik` | Alanın yüksekliğini toplam görüntü yüksekliğinin yüzdesi olarak belirler; koşullandırma etkisinin dikey kapsamını etkiler. | `FLOAT` |
| `x` | Alanın yatay başlangıç noktasını toplam görüntü genişliğinin yüzdesi olarak belirtir; koşullandırma etkisini konumlandırır. | `FLOAT` |
| `y` | Alanın dikey başlangıç noktasını toplam görüntü yüksekliğinin yüzdesi olarak belirtir; koşullandırma etkisini konumlandırır. | `FLOAT` |
| `güç` | Belirtilen alan içindeki koşullandırma etkisinin yoğunluğunu kontrol eder; etkisinin ince ayarının yapılmasına olanak tanır. | `FLOAT` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Güncellenmiş alan ve güç parametreleriyle değiştirilmiş koşullandırma öğelerini döndürür; daha fazla işleme veya uygulamaya hazırdır. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentage/tr.md)
