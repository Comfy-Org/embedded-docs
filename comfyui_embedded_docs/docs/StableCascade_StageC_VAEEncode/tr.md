# StabilKaskad_AşamaC_VAEKodlama

The StableCascade_StageC_VAEEncode düğümü, Stable Cascade modeli için gizli temsiller üretmek amacıyla bir girdi görüntüsünü bir VAE kodlayıcıdan geçirir. Görüntüyü önce bir sıkıştırma faktörüne ve VAE'nin alt örnekleme oranına göre yeniden boyutlandırır, ardından yeniden boyutlandırılmış görüntüyü kodlar. Düğüm iki gizli tensör çıktısı verir: biri C aşaması için (gerçek kodlanmış sonuç) ve biri B aşaması için (sıfırlarla doldurulmuş bir yer tutucu).

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Gizli uzaya kodlanacak girdi görüntüsü | IMAGE | Evet | - |
| `vae` | Görüntüyü kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `sıkıştırma` | Kodlamadan önce görüntüye uygulanan sıkıştırma faktörü. Görüntü boyutları bu değere bölünür ve ardından VAE'nin alt örnekleme oranıyla çarpılır. Bu gelişmiş bir parametredir. (varsayılan: 42) | INT | Hayır | 4-128 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `aşama_c` | Stable Cascade modelinin C aşaması için kodlanmış gizli temsil | LATENT |
| `aşama_b` | B aşaması için bir yer tutucu gizli temsil. Şu anda girdi görüntüsü boyutundan hesaplanan boyutlara sahip sıfırlarla doldurulmuş bir tensör döndürür. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/tr.md)

---
**Source fingerprint (SHA-256):** `1679aaac77057fcc359e5428906d5227f6c2dde721aabbfb5a32c08738ac376c`
