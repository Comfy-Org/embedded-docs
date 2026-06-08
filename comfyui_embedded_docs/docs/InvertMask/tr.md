InvertMask düğümü, belirli bir maskenin değerlerini tersine çevirerek maskelenmiş ve maskelenmemiş alanları etkili bir şekilde değiştirmek için tasarlanmıştır. Bu işlem, ilgi odağının ön plan ile arka plan arasında değiştirilmesi gereken görüntü işleme görevlerinde temel bir öneme sahiptir.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `maske` | 'mask' parametresi, tersine çevrilecek giriş maskesini temsil eder. Tersine çevirme işleminde hangi alanların değiştirileceğini belirlemek için kritik öneme sahiptir. | MASK |

## Çıkışlar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `maske` | Çıktı, giriş maskesinin tersine çevrilmiş bir sürümüdür; daha önce maskelenmiş alanlar maskelenmemiş hale gelir ve bunun tersi de geçerlidir. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InvertMask/tr.md)
