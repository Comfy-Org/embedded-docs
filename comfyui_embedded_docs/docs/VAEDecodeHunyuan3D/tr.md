# VAEKodÇözmeHunyuan3D

VAEDecodeHunyuan3D düğümü, VAE kod çözücü kullanarak latent temsilleri 3D voxel verilerine dönüştürür. Yapılandırılabilir parçalama ve çözünürlük ayarlarıyla latent örnekleri VAE modelinden geçirerek 3D uygulamalar için uygun hacimsel veri üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | 3D voxel verisine dönüştürülecek latent temsil | LATENT | Evet | - |
| `vae` | Latent örnekleri çözmek için kullanılan VAE modeli | VAE | Evet | - |
| `num_chunks` | Bellek yönetimi için işlemin bölüneceği parça sayısı (varsayılan: 8000) | INT | Evet | 1000-500000 |
| `octree_resolution` | 3D voxel üretimi için kullanılan sekizli ağaç yapısının çözünürlüğü (varsayılan: 256) | INT | Evet | 16-512 |

Not: `num_chunks` ve `octree_resolution` gelişmiş parametrelerdir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `voxels` | Çözülen latent temsilden üretilen 3D voxel verisi | VOXEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/tr.md)

---
**Source fingerprint (SHA-256):** `740e328e9e7817aa1a029c5fadddf5457c91bbb5ac12c7e8af2cd81bee6184a7`
