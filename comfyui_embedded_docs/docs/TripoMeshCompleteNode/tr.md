# TripoMeshCompleteNode

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `segment_task_id` | Bir Tripo mesh segmentasyon görevinin görev kimliği. Bu göreve ait segmentli modelin parçaları tamamlanır. Önceki bir Tripo mesh segmentasyon düğümünün SEGMENT_TASK_ID çıktısına bağlayın. | SEGMENT_TASK_ID | Evet | Tek görev kimliği |
| `part_names` | Tamamlanacak parça adlarının virgülle ayrılmış listesi. Boş bırakılırsa tüm parçalar tamamlanır. Varsayılan: boş dize. Adların etrafındaki fazladan boşluklar kaldırılır ve yinelenen adlar yok sayılır. | STRING | Hayır | Serbest metin veya boş |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Tamamlanan modelin dosya adı. Bu çıktı yalnızca geriye dönük uyumluluk içindir. | STRING |
| `model task_id` | Tamamlanan Tripo mesh tamamlama görevinin görev kimliği. Model görev kimliği bekleyen diğer Tripo düğümleri tarafından girdi olarak kullanılabilir. | MODEL_TASK_ID |
| `GLB` | Onarılmış parçaları içeren, GLB dosyası olarak indirilen tamamlanmış 3D model. | GLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMeshCompleteNode/tr.md)

---
**Source fingerprint (SHA-256):** `aa7173f25f54d9fca9605e246a93fe319cf46c07d8d3aacc214a24a60c92e611`
