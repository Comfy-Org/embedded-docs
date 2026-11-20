# Tripo: Smart UV

Tripo: Smart UV, bir modelin UV'lerini yeniden açar ve dokularını, rig'ini ve animasyonunu yeni yerleşime yeniden eşler. Bir modelin özgün UV düzeni kullanılamaz olduğunda, örneğin retopoloji sonrasında veya doku dikişlerinin yeniden yapılması gerektiğinde kullanın. Girdi modeli 80.000 üçgeni aşmamalıdır (bir quad iki üçgen sayılır); bu nedenle daha büyük modelleri önce Tripo: Retopology veya bir `face_limit` ile küçültün.

> **Not:** Tripo, görev kayıtlarını sunucularında 7 gün boyunca tutar (1 Aralık 2026'dan itibaren geçerlidir). Bu süreden daha eski bir görev kimliği artık çözümlenemez; bu nedenle kaydedilmiş bir iş akışını bu süre geçtikten sonra yeniden çalıştırmak bu düğümde başarısız olur. Yeni bir görev kimliği oluşturmak için önceki Tripo düğümünü yeniden çalıştırın veya indirilen modeli **Tripo: Import Model** ile yeniden içe aktarın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | UV'leri yeniden açılacak modelin görev kimliği. Bir Tripo oluşturma düğümünden gelen model görev kimliğini veya bir rig, retarget ya da segment görev kimliğini kabul eder. | MODEL_TASK_ID | Evet | Tripo görev kimliği |
| `bake` | Mevcut dokuları yeni UV düzenine pişirir. Kapalı olduğunda pişirme atlanır ve model renk dokuları olmadan döndürülür (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model task_id` | Tamamlanan UV görevinin görev kimliği. Örneğin Tripo: Texture gibi diğer Tripo düğümlerine aktarılabilir. | MODEL_TASK_ID |
| `GLB` | GLB biçimindeki yeniden UV açılmış model. Kaynak model FBX olduğunda boştur. | FILE_3D_GLB |
| `FBX` | FBX biçimindeki yeniden UV açılmış model. Yalnızca kaynak model FBX olduğunda, örneğin bir quad mesh olduğunda doldurulur. | FILE_3D_FBX |
| `UV atlas` | Modelin görüntü olarak render edilmiş UV düzeni. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartUVNode/tr.md)

---
**Source fingerprint (SHA-256):** `55c9352c7c8129fa7a4f99f803bdc6db112830454e7d9566fa734063cb283532`
