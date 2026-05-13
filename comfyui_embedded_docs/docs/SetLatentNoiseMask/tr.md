> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetLatentNoiseMask/tr.md)

Bu düğüm, bir dizi gizli örneğe (latent sample) bir gürültü maskesi uygulamak için tasarlanmıştır. Belirtilen maskeyi entegre ederek giriş örneklerini değiştirir ve böylece gürültü özelliklerini değiştirir.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `örnekler` | `LATENT`    | Gürültü maskesinin uygulanacağı gizli örnekler. Bu parametre, değiştirilecek temel içeriğin belirlenmesi için çok önemlidir. |
| `maske`    | `MASK`      | Gizli örneklere uygulanacak maske. Örnekler içindeki gürültü değişikliğinin alanlarını ve yoğunluğunu tanımlar. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Uygulanan gürültü maskesi ile değiştirilmiş gizli örnekler. |