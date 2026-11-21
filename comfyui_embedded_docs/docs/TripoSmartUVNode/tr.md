# Tripo: Smart UV

Tripo: Smart UV, bir modelin UV'lerini yeniden açar ve dokularını, rig ve animasyonunu yeni düzene yeniden eşler. Bir modelin orijinal UV düzeni kullanılamaz olduğunda, örneğin retopoloji sonrasında veya doku dikişlerinin yeniden yapılması gerektiğinde kullanın. Girdi modeli 80.000 üçgeni aşmamalıdır (bir dörtgen iki üçgen sayılır), bu nedenle daha büyük modelleri önce Tripo: Retopology veya bir `face_limit` ile küçültün.

> **Not:** Tripo, görev kayıtlarını sunucularında 7 gün boyunca saklar (1 Aralık 2026 tarihinden itibaren geçerlidir). Bundan daha eski bir görev kimliği artık çözümlenemez, bu nedenle kaydedilmiş bir iş akışını bu süre penceresinden sonra yeniden çalıştırmak bu düğümde başarısız olur. Görevi oluşturan üst Tripo düğümlerini yeniden çalıştırın veya indirilmiş bir modeli **Tripo: Import Model** ile yeniden içe aktarın. Modeli süre penceresi kapanmadan indirin: süresi dolmuş bir varlık görev kaydından kurtarılamaz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | Yeniden UV açımı yapılacak modelin görev kimliği. Bir Tripo oluşturma düğümünden gelen model görev kimliğini veya bir rig, retarget veya segment görev kimliğini kabul eder. | MODEL_TASK_ID | Evet | Tripo görev kimliği |
| `bake` | Mevcut dokuları yeni UV düzenine pişirin. Kapalı olduğunda pişirme atlanır ve model renk dokuları olmadan döndürülür (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model task_id` | Tamamlanan UV görevinin görev kimliği. Örneğin Tripo: Texture gibi diğer Tripo düğümlerine aktarılabilir. | MODEL_TASK_ID |
| `GLB` | GLB biçiminde yeniden UV açımı yapılmış model. Kaynak model FBX olduğunda boştur. | FILE_3D_GLB |
| `FBX` | FBX biçiminde yeniden UV açımı yapılmış model. Yalnızca kaynak model FBX olduğunda doldurulur, örneğin bir dörtgen ağ (quad mesh). | FILE_3D_FBX |
| `UV atlas` | Modelin UV düzeninin görüntü olarak oluşturulmuş hali. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartUVNode/tr.md)

---
**Source fingerprint (SHA-256):** `55c9352c7c8129fa7a4f99f803bdc6db112830454e7d9566fa734063cb283532`
