# StabilKaskad_AşamaC_VAEKodlama

StableCascade_StageC_VAEEncode düğümü, Stable Cascade modeli için latent temsiller üretmek üzere bir girdi görüntüsünü bir VAE kodlayıcıdan geçirir. Önce görüntüyü bir sıkıştırma faktörüne ve VAE'nin küçültme oranına göre yeniden boyutlandırır, ardından yeniden boyutlandırılmış görüntüyü kodlar. Düğüm iki latent tensörü çıkarır: biri C aşaması için (gerçek kodlanmış sonuç) ve biri B aşaması için (sıfırlarla doldurulmuş bir yer tutucu).

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Latent uzaya kodlanacak girdi görüntüsü | IMAGE | Evet | - |
| `vae` | Görüntüyü kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `compression` | Kodlamadan önce görüntüye uygulanan sıkıştırma faktörü. Görüntü boyutları bu değere bölünür, ardından VAE'nin küçültme oranıyla çarpılır. (varsayılan: 42) | INT | Hayır | 4-128 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `stage_c` | Stable Cascade modelinin C aşaması için kodlanmış latent temsil | LATENT |
| `stage_b` | B aşaması için bir yer tutucu latent temsil. Şu anda girdi görüntüsü boyutundan hesaplanan boyutlara sahip sıfırlarla doldurulmuş bir tensör döndürür. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/tr.md)

---
**Source fingerprint (SHA-256):** `1679aaac77057fcc359e5428906d5227f6c2dde721aabbfb5a32c08738ac376c`
