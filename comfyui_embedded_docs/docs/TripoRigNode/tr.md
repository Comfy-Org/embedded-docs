> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/tr.md)

TripoRigNode, orijinal bir model görev kimliğinden (task ID) donanımlı (rigged) bir 3B model oluşturur. Tripo API'sine, Tripo spesifikasyonunu kullanarak GLB formatında animasyonlu bir donanım (rig) oluşturması için bir istek gönderir, ardından donanım oluşturma görevi tamamlanana kadar API'yi sorgular.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID | Evet | - | Donanım eklenecek orijinal 3B modelin görev kimliği |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | Hayır | - | Comfy.org API erişimi için kimlik doğrulama belirteci |
| `comfy_api_key` | API_KEY_COMFY_ORG | Hayır | - | Comfy.org hizmet kimlik doğrulaması için API anahtarı |
| `unique_id` | UNIQUE_ID | Hayır | - | İşlemi izlemek için benzersiz tanımlayıcı |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_file` | STRING | Oluşturulan donanımlı 3B model dosyası (geriye dönük uyumluluk için korunmuştur) |
| `rig task_id` | RIG_TASK_ID | Donanım oluşturma sürecini izlemek için görev kimliği |
| `GLB` | FILE3DGLB | GLB formatında oluşturulan donanımlı 3B model |

---
**Source fingerprint (SHA-256):** `621a4d08f3b8a349c3afff3dbf888b20d524eb3337685769b7a7badcb28986e4`
