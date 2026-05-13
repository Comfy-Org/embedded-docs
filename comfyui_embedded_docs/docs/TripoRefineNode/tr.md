> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/tr.md)

TripoRefineNode, özellikle v1.4 Tripo modelleri tarafından oluşturulan taslak 3B modelleri iyileştirir. Bir model görev kimliği alır ve Tripo API'si aracılığıyla işleyerek modelin geliştirilmiş bir sürümünü oluşturur. Bu düğüm, yalnızca Tripo v1.4 modelleri tarafından üretilen taslak modellerle çalışmak üzere tasarlanmıştır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model_task_id` | MODEL_TASK_ID | Evet | - | Bir v1.4 Tripo modeli olmalıdır |

**Not:** Bu düğüm yalnızca Tripo v1.4 modelleri tarafından oluşturulan taslak modelleri kabul eder. Diğer sürümlerdeki modellerin kullanılması hatalara neden olabilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model_file` | STRING | İyileştirilmiş modelin dosya yolu veya referansı (yalnızca geriye dönük uyumluluk için) |
| `model task_id` | MODEL_TASK_ID | İyileştirilmiş model işlemi için görev tanımlayıcısı |
| `GLB` | FILE3DGLB | GLB formatında iyileştirilmiş 3B model |

---
**Source fingerprint (SHA-256):** `136093c7cdd7eb33b55e862f4b8c0554de7bde656a7e0139efb63323ad041c32`
