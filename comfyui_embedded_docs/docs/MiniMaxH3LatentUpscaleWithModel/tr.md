# MiniMax H3 Latent Upscale With Model

MiniMax H3 Latent Upscale With Model, MiniMax H3 latentinin video kısmını bir latent ölçek büyütme modeliyle hedef genişlik ve yüksekliğe yeniden boyutlandırır. Ses latenti değiştirilmeden birlikte taşınır; böylece klip sesini korur ve yeniden örnekleme gerekmez. MiniMax H3 örneklemesinden sonra ve klip daha büyük çıkacaksa H3 VAE decode işleminden önce kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Latent ölçek büyütme modeli; genellikle Load Latent Upscale Model ile yüklenir. MiniMax H3 3D konvolüsyonlu latent ölçek büyütücü olmalıdır. | LATENT_UPSCALE_MODEL | Evet | - |
| `samples` | Yeniden boyutlandırılacak MiniMax H3 latenti. İç içe geçmiş bir latent, ses kısmını olduğu gibi korur. | LATENT | Evet | - |
| `width` | Hedef video genişliği (piksel cinsinden). Latent, `width / 16` sütuna yeniden boyutlandırılır; bu nedenle değer 16'nın katına aşağı yuvarlanır. (varsayılan: 2560) | INT | Evet | 32 - 16384 (adım 32) |
| `height` | Hedef video yüksekliği (piksel cinsinden), yine 16'nın katına aşağı yuvarlanır. (varsayılan: 1440) | INT | Evet | 32 - 16384 (adım 32) |

İstenen boyut zaten latentle eşleşiyorsa, girdi latenti değiştirilmeden döndürülür. Yeniden boyutlandırılan latent `noise_mask` taşımaz; bu nedenle kısmen maskelenmiş bir latent maskesini kaybeder. Ağ, 3D konvolüsyonlarını zamansal dilimler halinde çalıştırır; bu da uzun kliplerde bellek kullanımını tek bir dilimin bellek kullanımına yakın tutar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `LATENT` | Yeniden boyutlandırılmış latent; H3 VAE decode için hazırdır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3LatentUpscaleWithModel/tr.md)

---
**Source fingerprint (SHA-256):** `cd659baace5a21620033dd3470b854cccbada01d09545a2f61273b949c3a004b`
