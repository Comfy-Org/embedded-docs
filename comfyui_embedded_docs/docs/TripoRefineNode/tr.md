> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/tr.md)

TripoRefineNode, özellikle v1.4 Tripo modelleri tarafından oluşturulan taslak 3B modelleri iyileştirir. Bir model görev kimliği alır ve modelin geliştirilmiş bir versiyonunu oluşturmak için Tripo API'sı üzerinden işler. Bu düğüm, yalnızca Tripo v1.4 modelleri tarafından üretilen taslak modellerle çalışmak üzere tasarlanmıştır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | Evet | - | Bir v1.4 Tripo modeli olmalıdır |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | Hayır | - | Comfy.org API'si için kimlik doğrulama jetonu |
| `comfy_api_key` | API_KEY_COMFY_ORG | Hayır | - | Comfy.org hizmetleri için API anahtarı |
| `unique_id` | UNIQUE_ID | Hayır | - | İşlem için benzersiz tanımlayıcı |

**Not:** Bu düğüm yalnızca Tripo v1.4 modelleri tarafından oluşturulan taslak modelleri kabul eder. Diğer sürümlerden modellerin kullanılması hatalara neden olabilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_file` | STRING | İyileştirilmiş modelin dosya yolu veya referansı |
| `model task_id` | MODEL_TASK_ID | İyileştirilmiş model işlemi için görev tanımlayıcısı |