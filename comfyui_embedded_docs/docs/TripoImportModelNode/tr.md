# Tripo: Model İçe Aktar

Bu düğüm, harici bir 3B modeli Tripo'ya aktarır ve böylece Texture, Rig ve Convert gibi diğer Tripo işlem sonrası düğümleri bunu kullanabilir. Düğüm modeli yükler ve içe aktarılan modeli tanımlayan bir görev kimliği döndürür. Dokular yalnızca dosyaya gömüldüklerinde korunduğu için GLB önerilir ve içe aktarılan bir modele doku uygulamak bir doku istemi gerektirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|----------|--------|
| `model_3d` | Aktarılacak 3B model (GLB / FBX / OBJ / STL, en fazla 150 MB). OBJ ve STL dosyaları gömülü doku içermez. | FILE3D | Evet | GLB<br>FBX<br>OBJ<br>STL<br>Herhangi bir 3B biçim |

**Not:** Yalnızca GLB, FBX, OBJ ve STL biçimleri desteklenir. GLTF (.gltf) harici dosyalara başvurduğu için içe aktarılamaz; bunun yerine tek dosyalık bir GLB kullanın. Model dosyası 150 MB veya daha küçük olmalıdır. Dokular yalnızca dosyaya gömüldüklerinde içe aktarma sonrasında korunduğu için GLB önerilir. OBJ ve STL dosyaları gömülü dokular taşımaz. İçe aktarılan bir modele doku uygulamak bir doku istemi gerektirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `model task_id` | Tripo işlem sonrası düğümleriyle kullanılmak üzere aktarılan modeli tanımlayan bir görev kimliği | MODEL_TASK_ID |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `4fa13a108804f2a52190a85b5b5d58ff18190e9d182b556abada444788012fab`
