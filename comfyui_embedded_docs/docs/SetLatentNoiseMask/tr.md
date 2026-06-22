# Gizli Gürültü Maskesi Ayarla

Bu düğüm, bir dizi gizli örneğe (latent sample) bir gürültü maskesi uygulamak için tasarlanmıştır. Belirtilen maskeyi entegre ederek giriş örneklerini değiştirir ve böylece gürültü özelliklerini değiştirir.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `örnekler` | Gürültü maskesinin uygulanacağı gizli örnekler. Bu parametre, değiştirilecek temel içeriğin belirlenmesi için çok önemlidir. | `LATENT` |
| `maske` | Gizli örneklere uygulanacak maske. Örnekler içindeki gürültü değişikliğinin alanlarını ve yoğunluğunu tanımlar. | `MASK` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Uygulanan gürültü maskesi ile değiştirilmiş gizli örnekler. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetLatentNoiseMask/tr.md)
