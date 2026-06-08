TripoRefineNode, özellikle v1.4 Tripo modelleri tarafından oluşturulan taslak 3B modelleri iyileştirir. Bir model görev kimliği alır ve Tripo API'si aracılığıyla işleyerek modelin geliştirilmiş bir sürümünü oluşturur. Bu düğüm, yalnızca Tripo v1.4 modelleri tarafından üretilen taslak modellerle çalışmak üzere tasarlanmıştır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model_görev_id` | Bir v1.4 Tripo modeli olmalıdır | MODEL_TASK_ID | Evet | - |

**Not:** Bu düğüm yalnızca Tripo v1.4 modelleri tarafından oluşturulan taslak modelleri kabul eder. Diğer sürümlerdeki modellerin kullanılması hatalara neden olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model_görev_id` | İyileştirilmiş modelin dosya yolu veya referansı (yalnızca geriye dönük uyumluluk için) | STRING |
| `GLB` | İyileştirilmiş model işlemi için görev tanımlayıcısı | MODEL_TASK_ID |
| `GLB` | GLB formatında iyileştirilmiş 3B model | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/tr.md)

---
**Source fingerprint (SHA-256):** `136093c7cdd7eb33b55e862f4b8c0554de7bde656a7e0139efb63323ad041c32`
