> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/tr.md)

LTXVSeparateAVLatent düğümü, birleşik bir ses-görüntü gizli temsilini alır ve bunu iki ayrı parçaya ayırır: biri video, diğeri ses için. Giriş gizli temsilinden örnekleri ve varsa gürültü maskelerini ayırarak iki yeni gizli nesne oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `av_latent` | LATENT | Evet | Yok | Ayrıştırılacak birleşik ses-görüntü gizli temsili. |

**Not:** Giriş gizli temsilinin `samples` tensörünün, ilk boyut (toplu iş boyutu) boyunca en az iki öğeye sahip olması beklenir. İlk öğe video gizli temsili için, ikinci öğe ise ses gizli temsili için kullanılır. Bir `noise_mask` (gürültü maskesi) varsa, aynı şekilde ayrıştırılır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `video_latent` | LATENT | Ayrıştırılmış video verilerini içeren gizli temsil. |
| `audio_latent` | LATENT | Ayrıştırılmış ses verilerini içeren gizli temsil. |

---
**Source fingerprint (SHA-256):** `55bce5d768e7fe13f885cc32d34ecdac5cdcbb667b03743004866ea4b6d58d46`
