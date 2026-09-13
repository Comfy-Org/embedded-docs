# Recraft Arka Planı Kaldır

Bu düğüm, Recraft API hizmetini kullanarak görüntülerin arka planını kaldırır. Girdi grubundaki her görüntüyü ayrı ayrı işler ve hem saydam arka planlara sahip işlenmiş görüntüleri hem de kaldırılan arka plan alanlarını belirten ilgili alfa maskelerini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Arka plan kaldırma için işlenecek girdi görüntü(ler)i. Gruptaki her görüntü ayrı ayrı işlenir. | IMAGE | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-------------|-------------|-----------|
| `image` | Saydam arka planlara sahip işlenmiş görüntüler (RGBA biçimi) | IMAGE |
| `mask` | Kaldırılan arka plan alanlarını belirten alfa kanalı maskeleri, B,H,W biçiminde | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/tr.md)

---
**Source fingerprint (SHA-256):** `702dfdf2751d5ca33f23e10c0968496887514a21da7a0c42e3636a0ed4e82311`
