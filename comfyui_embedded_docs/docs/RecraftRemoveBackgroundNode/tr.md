> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/tr.md)

Bu düğüm, Recraft API servisini kullanarak görüntülerden arka planı kaldırır. Girdi grubundaki her görüntüyü işler ve hem şeffaf arka plana sahip işlenmiş görüntüleri hem de kaldırılan arka plan alanlarını gösteren ilgili alfa maskelerini döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Arka plan kaldırma işlemi için işlenecek girdi görüntü(leri) |
| `auth_token` | STRING | Hayır | - | Recraft API erişimi için kimlik doğrulama belirteci |
| `comfy_api_key` | STRING | Hayır | - | Comfy.org servis entegrasyonu için API anahtarı |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Şeffaf arka plana sahip işlenmiş görüntüler |
| `mask` | MASK | Kaldırılan arka plan alanlarını gösteren alfa kanalı maskeleri |