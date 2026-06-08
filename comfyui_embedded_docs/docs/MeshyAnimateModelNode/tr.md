Bu düğüm, Meshy hizmeti kullanılarak daha önce iskeletlendirilmiş (rig) bir 3D karakter modeline belirli bir animasyon uygular. Önceki bir iskeletlendirme işleminden alınan bir görev kimliğini (task ID) ve kütüphaneden istenen animasyonu seçmek için bir eylem kimliğini (action ID) alır. Düğüm daha sonra isteği işler ve animasyonlu modeli hem GLB hem de FBX dosya formatlarında döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `rig_task_id` | Daha önce tamamlanmış bir Meshy karakter iskeletlendirme işlemine ait benzersiz görev kimliği. | STRING | Evet | Yok |
| `action_id` | Uygulanacak animasyon eyleminin kimlik numarası. Mevcut değerlerin listesi için <https://docs.meshy.ai/en/api/animation-library> adresini ziyaret edin. (varsayılan: 0) | INT | Evet | 0 ile 696 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `GLB` | Animasyonlu model için bir dize tanımlayıcı. Bu çıktı yalnızca geriye dönük uyumluluk için sağlanmıştır. | STRING |
| `FBX` | GLB formatındaki animasyonlu 3D model dosyası. | FILE3DGLB |
| `FBX` | FBX formatındaki animasyonlu 3D model dosyası. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `3b7610b5f6f763dde86a52f9212b3fc98f41e54bda30097fcb8f5f0bd020899e`
