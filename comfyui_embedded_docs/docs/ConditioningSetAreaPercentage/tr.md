> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentage/tr.md)

ConditioningSetAreaPercentage düğümü, koşullandırma elemanlarının etki alanını yüzde değerlerine göre ayarlamada uzmanlaşmıştır. Koşullandırma etkisinin yoğunluğunu modüle eden bir güç parametresinin yanı sıra, alanın boyutlarını ve konumunu toplam görüntü boyutunun yüzdeleri olarak belirlemeye olanak tanır.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Değiştirilecek koşullandırma elemanlarını temsil eder; alan ve güç ayarlamalarının uygulanması için temel oluşturur. |
| `width`   | `FLOAT`     | Alanın genişliğini, toplam görüntü genişliğinin bir yüzdesi olarak belirler; koşullandırmanın görüntüyü yatay olarak ne kadar etkilediğini belirler. |
| `height`  | `FLOAT`     | Alanın yüksekliğini, toplam görüntü yüksekliğinin bir yüzdesi olarak belirler; koşullandırmanın dikey etki kapsamını etkiler. |
| `x`       | `FLOAT`     | Alanın yatay başlangıç noktasını, toplam görüntü genişliğinin bir yüzdesi olarak belirterek koşullandırma etkisinin konumlandırılmasını sağlar. |
| `y`       | `FLOAT`     | Alanın dikey başlangıç noktasını, toplam görüntü yüksekliğinin bir yüzdesi olarak belirterek koşullandırma etkisinin konumlandırılmasını sağlar. |
| `strength`| `FLOAT`     | Belirtilen alan içindeki koşullandırma etkisinin yoğunluğunu kontrol eder; etkisinin ince ayar yapılmasına olanak tanır. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Güncellenmiş alan ve güç parametreleriyle değiştirilmiş koşullandırma elemanlarını döndürür; daha fazla işleme veya uygulama için hazırdır. |