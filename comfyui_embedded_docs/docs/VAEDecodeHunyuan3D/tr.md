# VAEKodÇözmeHunyuan3D

VAEDecodeHunyuan3D düğümü, bir VAE kod çözücü kullanarak gizli temsilleri 3D voxel verilerine dönüştürür. Gizli örnekleri, yapılandırılabilir parçalama ve çözünürlük ayarlarıyla VAE modeli aracılığıyla işleyerek 3D uygulamalar için uygun hacimsel veriler üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `örnekler` | 3D voxel verilerine dönüştürülecek gizli temsil | LATENT | Evet | - |
| `vae` | Gizli örnekleri kod çözmek için kullanılan VAE modeli | VAE | Evet | - |
| `parça_sayısı` | Bellek yönetimi için işlemin bölüneceği parça sayısı (varsayılan: 8000) | INT | Evet | 1000-500000 |
| `sekizli_ağaç_çözünürlüğü` | 3D voxel üretimi için kullanılan sekizli ağaç yapısının çözünürlüğü (varsayılan: 256) | INT | Evet | 16-512 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `voxels` | Kod çözülen gizli temsilden üretilen 3D voxel verileri | VOXEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/tr.md)

---
**Source fingerprint (SHA-256):** `a53ad8e14a2ffca6278866753046d5959f057a4c3fdba5623b37545cee27d557`
