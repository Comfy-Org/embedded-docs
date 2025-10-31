> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/tr.md)

TripoRigNode, orijinal model görev kimliğinden riglenmiş bir 3B model oluşturur. Tripo API'sine GLB formatında Tripo spesifikasyonunu kullanarak animasyonlu bir rig oluşturmak için bir istek gönderir, ardından rig oluşturma görevi tamamlanana kadar API'yi yoklar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID | Evet | - | Riglenecek orijinal 3B modelin görev kimliği |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | Hayır | - | Comfy.org API erişimi için kimlik doğrulama belirteci |
| `comfy_api_key` | API_KEY_COMFY_ORG | Hayır | - | Comfy.org servis kimlik doğrulaması için API anahtarı |
| `unique_id` | UNIQUE_ID | Hayır | - | İşlemi takip etmek için benzersiz tanımlayıcı |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_file` | STRING | Oluşturulan riglenmiş 3B model dosyası |
| `rig task_id` | RIG_TASK_ID | Rig oluşturma sürecini takip etmek için görev kimliği |