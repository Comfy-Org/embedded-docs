> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/tr.md)

TripoRetargetNode, önceden tanımlanmış animasyonları 3B karakter modellerine hareket verilerini yeniden hedefleyerek uygular. Daha önce işlenmiş bir 3B modeli alır ve bir dizi önceden ayarlanmış animasyondan birini uygulayarak, çıktı olarak animasyonlu bir 3B model dosyası oluşturur. Düğüm, animasyon yeniden hedefleme işlemini gerçekleştirmek için Tripo API'si ile iletişim kurar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | RIG_TASK_ID | Evet | - | Animasyon uygulanacak, daha önce işlenmiş 3B modelin görev kimliği |
| `animation` | STRING | Evet | "preset:idle"<br>"preset:walk"<br>"preset:climb"<br>"preset:jump"<br>"preset:slash"<br>"preset:shoot"<br>"preset:hurt"<br>"preset:fall"<br>"preset:turn" | 3B modele uygulanacak animasyon ön ayarı |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | Hayır | - | Comfy.org API erişimi için kimlik doğrulama belirteci |
| `comfy_api_key` | API_KEY_COMFY_ORG | Hayır | - | Comfy.org servisine erişim için API anahtarı |
| `unique_id` | UNIQUE_ID | Hayır | - | İşlemi takip etmek için benzersiz tanımlayıcı |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_file` | STRING | Oluşturulan animasyonlu 3B model dosyası |
| `retarget task_id` | RETARGET_TASK_ID | Yeniden hedefleme işlemini takip etmek için görev kimliği |