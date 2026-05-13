> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/tr.md)

VAEDecodeHunyuan3D düğümü, bir VAE kod çözücü kullanarak gizli temsilleri 3D voxel verilerine dönüştürür. Gizli örnekleri, yapılandırılabilir parçalama ve çözünürlük ayarlarıyla VAE modeli aracılığıyla işleyerek 3D uygulamalar için uygun hacimsel veriler üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `örnekler` | LATENT | Evet | - | 3D voxel verilerine dönüştürülecek gizli temsil |
| `vae` | VAE | Evet | - | Gizli örnekleri kod çözmek için kullanılan VAE modeli |
| `parça_sayısı` | INT | Evet | 1000-500000 | Bellek yönetimi için işlemin bölüneceği parça sayısı (varsayılan: 8000) |
| `sekizli_ağaç_çözünürlüğü` | INT | Evet | 16-512 | 3D voxel üretimi için kullanılan sekizli ağaç yapısının çözünürlüğü (varsayılan: 256) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `voxels` | VOXEL | Kod çözülen gizli temsilden üretilen 3D voxel verileri |

---
**Source fingerprint (SHA-256):** `a53ad8e14a2ffca6278866753046d5959f057a4c3fdba5623b37545cee27d557`
