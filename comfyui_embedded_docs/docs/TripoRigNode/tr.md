# Tripo: Modeli Rigle

TripoRigNode, orijinal bir model görev kimliğinden (task ID) donanımlı (rigged) bir 3B model oluşturur. Tripo API'sine, Tripo spesifikasyonunu kullanarak GLB formatında animasyonlu bir donanım (rig) oluşturması için bir istek gönderir, ardından donanım oluşturma görevi tamamlanana kadar API'yi sorgular.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `orijinal_model_görev_id` | Donanım eklenecek orijinal 3B modelin görev kimliği | MODEL_TASK_ID | Evet | - |
| `auth_token` | Comfy.org API erişimi için kimlik doğrulama belirteci | AUTH_TOKEN_COMFY_ORG | Hayır | - |
| `comfy_api_key` | Comfy.org hizmet kimlik doğrulaması için API anahtarı | API_KEY_COMFY_ORG | Hayır | - |
| `unique_id` | İşlemi izlemek için benzersiz tanımlayıcı | UNIQUE_ID | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `rig_görev_id` | Oluşturulan donanımlı 3B model dosyası (geriye dönük uyumluluk için korunmuştur) | STRING |
| `GLB` | Donanım oluşturma sürecini izlemek için görev kimliği | RIG_TASK_ID |
| `GLB` | GLB formatında oluşturulan donanımlı 3B model | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/tr.md)

---
**Source fingerprint (SHA-256):** `621a4d08f3b8a349c3afff3dbf888b20d524eb3337685769b7a7badcb28986e4`
