# BoşLTXVGizliVideo

The EmptyLTXVLatentVideo node creates an empty latent tensor for video generation. It produces a zero-filled latent representation with the specified width, height, length, and batch size, ready to be used as a starting point in LTXV video workflows. The latent stores the video in a compressed form: the spatial dimensions are divided by 32 and the frame count is reduced by a factor of 8.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Gizli videonun piksel cinsinden genişliği (varsayılan: 768, adım: 32) | INT | Evet | 64 ile MAX_RESOLUTION |
| `height` | Gizli videonun piksel cinsinden yüksekliği (varsayılan: 512, adım: 32) | INT | Evet | 64 ile MAX_RESOLUTION |
| `length` | Gizli videodaki kare sayısı (varsayılan: 97, adım: 8) | INT | Evet | 1 ile MAX_RESOLUTION |
| `batch_size` | Bir yığında oluşturulacak gizli video sayısı (varsayılan: 1) | INT | Hayır | 1 ile 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Sıfırlarla doldurulmuş, oluşturulan boş gizli tensör. Gizli katman ayrıca, genişlik ve yüksekliğe uygulanan uzamsal alt örneklemeyi tanımlayan 32 değerinde bir `downscale_ratio_spacial` taşır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/tr.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
