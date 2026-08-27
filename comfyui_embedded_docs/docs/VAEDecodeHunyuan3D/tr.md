# VAEKodÇözmeHunyuan3D

VAEDecodeHunyuan3D düğümü, latent temsilleri bir VAE kod çözücü kullanarak 3D voxel verilerine dönüştürür. Yapılandırılabilir parçalama ve çözünürlük ayarlarıyla latent örnekleri VAE modeli aracılığıyla işleyerek 3D uygulamaları için uygun hacimsel veriler üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `örnekler` | 3D voxel verilerine kod çözülecek latent temsil | LATENT | Evet | - |
| `vae` | Latent örneklerin kod çözümünde kullanılan VAE modeli | VAE | Evet | - |
| `parça_sayısı` | Bellek yönetimi için işlemin bölüneceği parça sayısı. Gelişmiş parametre (varsayılan: 8000) | INT | Evet | 1000-500000 |
| `sekizli_ağaç_çözünürlüğü` | 3D voxel üretimi için kullanılan octree yapısının çözünürlüğü. Gelişmiş parametre (varsayılan: 256) | INT | Evet | 16-512 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `voxels` | Kod çözülen latent temsilden üretilen 3D voxel verileri | VOXEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/tr.md)

---
**Source fingerprint (SHA-256):** `740e328e9e7817aa1a029c5fadddf5457c91bbb5ac12c7e8af2cd81bee6184a7`
