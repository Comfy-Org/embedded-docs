> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetLatentNoiseMask/tr.md)

Bu düğüm, bir dizi gizli örneğe gürültü maskesi uygulamak için tasarlanmıştır. Girdi örneklerini, belirtilen bir maskeyi entegre ederek değiştirir ve böylece onların gürültü karakteristiklerini değiştirir.

## Girdiler

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | Gürültü maskesinin uygulanacağı gizli örnekler. Bu parametre, değiştirilecek temel içeriği belirlemek için çok önemlidir. |
| `mask`    | `MASK`      | Gizli örneklere uygulanacak maske. Örnekler içindeki gürültü değişikliğinin alanlarını ve yoğunluğunu tanımlar. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Uygulanan gürültü maskesi ile değiştirilmiş gizli örnekler. |