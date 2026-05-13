> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentage/tr.md)

ConditioningSetAreaPercentage düğümü, koşullandırma öğelerinin etki alanını yüzde değerlerine göre ayarlama konusunda uzmanlaşmıştır. Alanın boyutlarını ve konumunu toplam görüntü boyutunun yüzdesi olarak belirtmeye olanak tanır; ayrıca koşullandırma etkisinin yoğunluğunu ayarlamak için bir güç parametresi içerir.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Değiştirilecek koşullandırma öğelerini temsil eder; alan ve güç ayarlamalarının uygulanması için temel görevi görür. |
| `genişlik`   | `FLOAT`     | Alanın genişliğini toplam görüntü genişliğinin yüzdesi olarak belirtir; koşullandırmanın görüntüyü yatay olarak ne kadar etkileyeceğini belirler. |
| `yükseklik`  | `FLOAT`     | Alanın yüksekliğini toplam görüntü yüksekliğinin yüzdesi olarak belirler; koşullandırma etkisinin dikey kapsamını etkiler. |
| `x`       | `FLOAT`     | Alanın yatay başlangıç noktasını toplam görüntü genişliğinin yüzdesi olarak belirtir; koşullandırma etkisini konumlandırır. |
| `y`       | `FLOAT`     | Alanın dikey başlangıç noktasını toplam görüntü yüksekliğinin yüzdesi olarak belirtir; koşullandırma etkisini konumlandırır. |
| `güç`| `FLOAT`     | Belirtilen alan içindeki koşullandırma etkisinin yoğunluğunu kontrol eder; etkisinin ince ayarının yapılmasına olanak tanır. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Güncellenmiş alan ve güç parametreleriyle değiştirilmiş koşullandırma öğelerini döndürür; daha fazla işleme veya uygulamaya hazırdır. |