# Tripo: Model İçe Aktar

Bu düğüm, Tripo'nun Texture, Rig ve Convert gibi işlem sonrası düğümlerinde kullanabilmeniz için harici bir 3B model dosyasını Tripo sistemine aktarır. Modelinizi yükler ve diğer Tripo düğümlerinin aktarılan modele referans vermek için kullanabileceği bir görev kimliği döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|----------|--------|
| `model_3d` | Aktarılacak 3B model (GLB / FBX / OBJ / STL, en fazla 150 MB). OBJ ve STL dosyaları gömülü doku içermez. | FILE3D | Evet | GLB<br>FBX<br>OBJ<br>STL<br>Herhangi bir 3B biçim |

**Not:** GLB biçimi önerilir çünkü dokular yalnızca dosyaya doğrudan gömüldüklerinde korunur. OBJ ve STL dosyaları gömülü dokuları desteklemez. GLTF (.gltf) biçimi harici dosyalara referans verdiği için desteklenmez; bunun yerine tek dosyalı bir GLB kullanın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `model task_id` | Tripo işlem sonrası düğümleriyle kullanılmak üzere aktarılan modeli tanımlayan bir görev kimliği | MODEL_TASK_ID |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `4fa13a108804f2a52190a85b5b5d58ff18190e9d182b556abada444788012fab`
