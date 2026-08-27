# Recraft Arka Planı Kaldır

Bu düğüm, Recraft API hizmetini kullanarak görsellerden arka planı kaldırır. Giriş grubundaki her görseli işler ve hem şeffaf arka planlı işlenmiş görselleri hem de kaldırılan arka plan alanlarını gösteren ilgili alfa maskelerini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Arka plan kaldırma için işlenecek giriş görseli(ler)i. Gruptaki her görsel ayrı ayrı işlenir. | IMAGE | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Şeffaf arka planlı işlenmiş görseller (RGBA formatı) | IMAGE |
| `mask` | Kaldırılan arka plan alanlarını gösteren alfa kanalı maskeleri, B,H,W formatında | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/tr.md)

---
**Source fingerprint (SHA-256):** `702dfdf2751d5ca33f23e10c0968496887514a21da7a0c42e3636a0ed4e82311`
