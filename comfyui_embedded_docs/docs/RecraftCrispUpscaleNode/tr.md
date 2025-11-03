> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCrispUpscaleNode/tr.md)

Görüntüyü senkron olarak büyütür. Verilen bir raster görüntüyü 'crisp upscale' aracını kullanarak geliştirir, görüntü çözünürlüğünü artırır ve görüntüyü daha keskin ve temiz hale getirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | - | Büyütülecek giriş görüntüsü |
| `auth_token` | STRING | Hayır | - | Recraft API için kimlik doğrulama token'ı |
| `comfy_api_key` | STRING | Hayır | - | Comfy.org servisleri için API anahtarı |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `görüntü` | IMAGE | Geliştirilmiş çözünürlük ve netliğe sahip büyütülmüş görüntü |