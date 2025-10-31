> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImagePadForOutpaint/tr.md)

Bu düğüm, görüntülerin etrafına dolgu ekleyerek dışa boyama süreci için hazırlanması amacıyla tasarlanmıştır. Görüntü boyutlarını, orijinal sınırların ötesinde genişletilmiş görüntü alanlarının oluşturulmasını kolaylaştırmak ve dışa boyama algoritmalarıyla uyumluluğu sağlamak için ayarlar.

## Girdiler

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `görüntü`   | `IMAGE`     | 'image' girdisi, dışa boyama için hazırlanacak ana görüntüdür ve dolgu işlemleri için temel oluşturur. |
| `sol`    | `INT`       | Görüntünün sol tarafına eklenecek dolgu miktarını belirtir ve dışa boyama için genişletilmiş alanı etkiler. |
| `üst`     | `INT`       | Görüntünün üst kısmına eklenecek dolgu miktarını belirler ve dışa boyama için dikey genişlemeyi etkiler. |
| `sağ`   | `INT`       | Görüntünün sağ tarafına eklenecek dolgu miktarını tanımlar ve dışa boyama için yatay genişlemeyi etkiler. |
| `alt`  | `INT`       | Görüntünün alt kısmına eklenecek dolgu miktarını belirtir ve dışa boyama için dikey genişlemeye katkıda bulunur. |
| `yumuşatma` | `INT` | Orijinal görüntü ile eklenen dolgu arasındaki geçişin yumuşaklığını kontrol eder ve dışa boyama için görsel entegrasyonu geliştirir. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `görüntü`   | `IMAGE`     | Çıktı 'image', dışa boyama süreci için hazır olan dolgulu görüntüyü temsil eder. |
| `mask`    | `MASK`      | Çıktı 'mask', orijinal görüntünün ve eklenen dolgunun alanlarını gösterir ve dışa boyama algoritmalarını yönlendirmek için kullanışlıdır. |