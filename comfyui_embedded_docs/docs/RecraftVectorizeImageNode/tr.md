> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/tr.md)

Girdi görüntüsünden SVG'yi eşzamanlı olarak oluşturur. Bu düğüm, piksel tabanlı görüntüleri vektör grafik formatına dönüştürür; girdi grubundaki her görüntüyü işler ve sonuçları tek bir SVG çıktısında birleştirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | SVG formatına dönüştürülecek girdi görüntüsü |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | Hayır | - | API erişimi için kimlik doğrulama belirteci |
| `comfy_api_key` | API_KEY_COMFY_ORG | Hayır | - | Comfy.org servisleri için API anahtarı |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `SVG` | SVG | İşlenen tüm görüntülerin birleştirilmesiyle oluşturulan vektör grafik çıktısı |