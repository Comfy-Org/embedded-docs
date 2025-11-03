> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InvertMask/tr.md)

InvertMask düğümü, belirli bir maskenin değerlerini tersine çevirmek için tasarlanmıştır, böylece maskelenmiş ve maskelenmemiş alanlar etkili bir şekilde değiştirilir. Bu işlem, odaklanılan ilgi alanının ön plan ve arka plan arasında değiştirilmesi gereken görüntü işleme görevlerinde temel bir işlemdir.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `maske`    | MASK      | 'mask' parametresi, tersine çevrilecek girdi maskesini temsil eder. Tersine çevirme işleminde hangi alanların değiştirileceğini belirlemek için kritik öneme sahiptir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `maske`    | MASK      | Çıktı, girdi maskesinin tersine çevrilmiş halidir; önceden maskelenmiş alanlar maskesiz hale gelir ve bunun tersi de geçerlidir. |