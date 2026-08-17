# Recraft Arka Planı Kaldır

Bu düğüm, Recraft API hizmetini kullanarak görüntülerden arka planı kaldırır. Giriş kümesindeki her görüntüyü işler ve hem şeffaf arka planlı işlenmiş görüntüleri hem de kaldırılan arka plan alanlarını gösteren karşılık gelen alfa maskelerini döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Arka plan kaldırma için işlenecek giriş görüntüsü(leri) | IMAGE | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `image` | Şeffaf arka planlı işlenmiş görüntüler | IMAGE |
| `mask` | Kaldırılan arka plan alanlarını gösteren alfa kanalı maskeleri | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/tr.md)

---
**Source fingerprint (SHA-256):** `702dfdf2751d5ca33f23e10c0968496887514a21da7a0c42e3636a0ed4e82311`
