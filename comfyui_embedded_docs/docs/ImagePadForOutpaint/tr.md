Bu düğüm, görüntülerin etrafına dolgu ekleyerek onları dışa boyama (outpainting) işlemine hazırlamak için tasarlanmıştır. Görüntü boyutlarını, dışa boyama algoritmalarıyla uyumluluğu sağlayacak şekilde ayarlar ve orijinal sınırların ötesinde genişletilmiş görüntü alanlarının oluşturulmasını kolaylaştırır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | 'image' girişi, dışa boyama için hazırlanacak ana görüntüdür ve dolgu işlemleri için temel görevi görür. | `IMAGE` |
| `sol` | Görüntünün sol tarafına eklenecek dolgu miktarını belirtir ve dışa boyama için genişletilmiş alanı etkiler. | `INT` |
| `üst` | Görüntünün üst kısmına eklenecek dolgu miktarını belirler ve dışa boyama için dikey genişlemeyi etkiler. | `INT` |
| `sağ` | Görüntünün sağ tarafına eklenecek dolgu miktarını tanımlar ve dışa boyama için yatay genişlemeyi etkiler. | `INT` |
| `alt` | Görüntünün alt kısmına eklenecek dolgu miktarını belirtir ve dışa boyama için dikey genişlemeye katkıda bulunur. | `INT` |
| `yumuşatma` | Orijinal görüntü ile eklenen dolgu arasındaki geçişin yumuşaklığını kontrol eder ve dışa boyama için görsel bütünleşmeyi artırır. | `INT` |

## Çıkışlar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Çıktı 'image' parametresi, dışa boyama işlemine hazır, dolgulanmış görüntüyü temsil eder. | `IMAGE` |
| `mask` | Çıktı 'mask' parametresi, orijinal görüntünün ve eklenen dolgunun alanlarını belirtir ve dışa boyama algoritmalarını yönlendirmek için kullanışlıdır. | `MASK` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImagePadForOutpaint/tr.md)
