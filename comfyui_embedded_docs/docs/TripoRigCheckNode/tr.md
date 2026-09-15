# Tripo: Rig Kontrolü

Bu düğüm, tamamlanmış bir Tripo 3D model görevinin kimliğini Tripo API'sine gönderir ve bu modelin riglenip riglenemeyeceğini kontrol eder. Kontrolün tamamlanmasını bekler ve ardından evet/hayır sonucunun yanı sıra Tripo'nun model için önerdiği iskelet türünü döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | Analiz edilecek modelin Tripo görev kimliği. Daha önce oluşturulmuş, içe aktarılmış veya başka bir şekilde bir Tripo görevi aracılığıyla yaratılmış bir modeli tanımlar. | MODEL_TASK_ID | Evet | Yok |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `riggable` | Modelin riglenip riglenemeyeceği. | BOOLEAN |
| `rig_type` | Önerilen iskelet: biped, quadruped, hexapod, octopod, avian, serpentine veya aquatic; model riglenemezse 'others'. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigCheckNode/tr.md)

---
**Source fingerprint (SHA-256):** `3aa0bc194e887804b92ca1f9f2b12997c73e111fb282c5de96e55f664c21545e`
