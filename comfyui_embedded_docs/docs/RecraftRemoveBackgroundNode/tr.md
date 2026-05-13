> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/tr.md)

Bu düğüm, Recraft API hizmetini kullanarak görüntülerin arka planını kaldırır. Giriş grubundaki her görüntüyü işler ve hem şeffaf arka planlı işlenmiş görüntüleri hem de kaldırılan arka plan alanlarını gösteren karşılık gelen alfa maskelerini döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Arka planı kaldırılacak giriş görüntüsü/görüntüleri |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Şeffaf arka planlı işlenmiş görüntüler |
| `mask` | MASK | Kaldırılan arka plan alanlarını gösteren alfa kanalı maskeleri |

---
**Source fingerprint (SHA-256):** `9e3f1a0471da3afda6b8de26de3b7e78c1070c49ab49e4fc8b6b79bb10ff77de`
