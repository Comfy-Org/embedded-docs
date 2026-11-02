# Tripo: Model İçe Aktar

Bu düğüm, harici bir 3B modeli Tripo'ya aktarır; böylece Texture, Rig ve Convert gibi Tripo son işleme düğümleri onu kullanabilir. Düğüm, dosyayı Tripo'ya yükler ve bu düğümler tarafından kullanılmak üzere içe aktarılan modeli tanımlayan bir görev kimliği döndürür. GLB önerilir çünkü dokular yalnızca dosyaya gömülü olduğunda korunur ve içe aktarılan bir modelin dokulandırılması bir doku istemi gerektirir. Bu düğümün kullanımı ücretsizdir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | İçe aktarılacak 3B model (GLB / FBX / OBJ / STL, en fazla 150 MB). OBJ ve STL dosyaları gömülü doku taşımaz. | FILE3D | Evet | GLB<br>FBX<br>OBJ<br>STL<br>Herhangi bir 3D formatı |

**Not:** Yalnızca GLB, FBX, OBJ ve STL formatları desteklenir. GLTF (.gltf) içe aktarılamaz çünkü harici dosyalara başvurur; bunun yerine tek dosyalık bir GLB dışa aktarın. Model dosyası 150 MB veya daha küçük olmalıdır. GLB önerilir çünkü dokular içe aktarma sırasında yalnızca dosyaya gömülü olduğunda korunur. OBJ ve STL dosyaları gömülü doku taşımaz. İçe aktarılan bir modelin dokulandırılması bir doku istemi gerektirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model task_id` | İçe aktarılan modeli tanımlayan ve Tripo son işleme düğümleriyle kullanılmak üzere bir görev kimliği | MODEL_TASK_ID |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `bf91e964c5705f7377868dd06bbf5d57b41cc3607fc377cd45886d3d6c5ceddc`
