# Tripo: Modeli Rigle

Bu düğüm, mevcut bir Tripo 3D modelini alır ve onun iskeletli bir sürümünü oluşturur; yani model, canlandırılabilmesi için bir iskelete kavuşur. İskeletlendirilecek modelin görev kimliğini sağlarsınız, rig sürümünü, iskelet türünü, kemik adlandırma stilini ve çıktı dosyası biçimini seçersiniz; düğüm işi Tripo'ya gönderir, tamamlanana kadar bekler ve ardından indirilen sonucu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `orijinal_model_görev_id` | İskeletlendirilecek özgün 3D modelin görev kimliği. Bu genellikle daha önceki bir Tripo model oluşturma düğümü tarafından üretilen kimliktir. | MODEL_TASK_ID | Evet | - |
| `model_version` | Kullanılacak rig model sürümü. v1.0: yalnızca insansı (iki ayaklı) karakterler, 90+ animasyon ön ayarı. v2.5: insansı olmayan canlılar (dört ayaklı, altı ayaklı, sekiz ayaklı, kuşsu, yılansı, sucul). Varsayılan: `v1.0-20240301`. | COMBO | Hayır | "v1.0-20240301"<br>"v2.5-20260210" |
| `rig_type` | İskelet türü. "auto", önce Tripo'nun ücretsiz rig kontrolünü çalıştırır ve önerilen türü kullanır. Varsayılan: "auto". | COMBO | Hayır | "auto"<br>"biped"<br>"quadruped"<br>"hexapod"<br>"octopod"<br>"avian"<br>"serpentine"<br>"aquatic" |
| `spec` | Kemik adlandırma: Tripo yerel veya Mixamo uyumlu. Tripo, animasyon ön ayarlarını mixamo spec ile oluşturulmuş bir v1.0 rig üzerine yeniden hedefleyemez; Tripo: Retarget rigged model için tripo kullanın. Varsayılan: "tripo". | COMBO | Hayır | "tripo"<br>"mixamo" |
| `out_format` | Çıktı dosyası biçimi; sonuç, eşleşen çıktıya gelir. Varsayılan: "glb". | COMBO | Hayır | "glb"<br>"fbx" |

**Not:** v1.0 model sürümü (`v1.0-20240301`) yalnızca iki ayaklı iskeletleri destekler. Bu sürümle iki ayaklı olmayan bir `rig_type` kullanılırsa düğüm hata verir ve bunun yerine `v2.5-20260210` kullanmanızı söyler.

**Not:** `rig_type` "auto" olduğunda, Tripo önce modelin iskeletlendirilip iskeletlendirilemeyeceğini kontrol eder ve önerilen iskelet türünü seçer. Tripo modelin iskeletlendirilemeyeceğini bildirirse düğüm hata verir.

**Not:** Düğüm, Tripo'nun bir GLB veya FBX dosyası döndürmesini bekler. Tripo başka bir dosya türü döndürürse düğüm hata verir.

**Not:** Yalnızca `out_format` ile eşleşen çıktı doldurulur: `out_format` "glb" olduğunda `GLB`, "fbx" olduğunda `FBX`. Diğer 3D çıktısı boştur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Oluşturulan iskeletli model dosyası adı (görev kimliği artı biçim uzantısı). Yalnızca geriye dönük uyumluluk için tutulur. | STRING |
| `rig task_id` | Rig oluşturma sürecini izlemek için görev kimliği. | RIG_TASK_ID |
| `GLB` | İskeletli modelin GLB 3D dosyası olarak hâli. `out_format` "glb" olduğunda doldurulur. | FILE3DGLB |
| `FBX` | İskeletli modelin FBX 3D dosyası olarak hâli. `out_format` "fbx" olduğunda doldurulur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/tr.md)

---
**Source fingerprint (SHA-256):** `b9c1b6d27b6278bcee4fc22e11c11e65cd22ea92cab3fc6c74f84d3deb2024d6`
