# Meshy: Görüntüden Modele

Meshy: Image to Model düğümü, tek bir girdi görüntüsünden 3B model oluşturmak için Meshy API'sini kullanır. Görüntünüzü yükler, bir işleme görevi gönderir ve oluşturulan 3B model dosyalarını (GLB ve FBX) referans için görev kimliğiyle birlikte döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Oluşturma için kullanılacak AI model sürümünü belirtir. | COMBO | Evet | `"latest"` |
| `image` | 3B modele dönüştürülecek girdi görüntüsü. | IMAGE | Evet | - |
| `should_remesh` | `"false"` olarak ayarlandığında, işlenmemiş üçgen mesh döndürür. | DYNAMIC_COMBO | Evet | `"true"`<br>`"false"` |
| `topology` | Yeniden meshlenmiş model için hedef çokgen topolojisi. Bu girdi yalnızca `should_remesh` `"true"` olarak ayarlandığında kullanılabilir. | COMBO | Hayır* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Yeniden meshlenmiş model için hedef çokgen sayısı. Bu girdi yalnızca `should_remesh` `"true"` olarak ayarlandığında kullanılabilir. Varsayılan: 300000. | INT | Hayır* | 100 - 300000 |
| `symmetry_mode` | Oluşturulan 3B modele uygulanan simetriyi kontrol eder. | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | Dokuların oluşturulup oluşturulmayacağını belirler. `"false"` olarak ayarlandığında doku aşaması atlanır ve dokusuz bir mesh döndürülür. | DYNAMIC_COMBO | Evet | `"true"`<br>`"false"` |
| `enable_pbr` | Temel renge ek olarak PBR Haritaları (metallic, roughness, normal) oluşturur. Bu girdi yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. Varsayılan: `False`. | BOOLEAN | Hayır* | - |
| `texture_prompt` | Doku oluşturma sürecini yönlendirmek için bir metin istemi sağlayın. Maksimum 600 karakter. `texture_image` ile aynı anda kullanılamaz. Bu girdi yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. Varsayılan: boş dize. | STRING | Hayır* | - |
| `texture_image` | `texture_image` veya `texture_prompt` öğelerinden yalnızca biri aynı anda kullanılabilir. Bu girdi yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. | IMAGE | Hayır* | - |
| `pose_mode` | Oluşturulan model için poz modunu belirtin. Bu bir gelişmiş parametredir. | COMBO | Evet | `""` (boş)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'dan bağımsız olarak deterministik değildir. Varsayılan: 0. | INT | Evet | 0 - 2147483647 |

**Parametre Kısıtlamaları Notu:**

* `topology` ve `target_polycount` girdileri yalnızca `should_remesh` `"true"` olarak ayarlandığında kullanılabilir.
* `enable_pbr`, `texture_prompt` ve `texture_image` girdileri yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir.
* `should_texture` `"true"` olarak ayarlandığında, `texture_prompt` ve `texture_image` aynı anda kullanılamaz. Her ikisi de sağlanırsa, düğüm bir hata verir.
* `texture_prompt` maksimum 600 karakter uzunluğundadır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model_file` | Oluşturulan GLB modelinin dosya adı. Yalnızca geriye dönük uyumluluk için korunmaktadır. | STRING |
| `meshy_task_id` | Meshy API görevi için benzersiz tanımlayıcıdır; referans veya sorun giderme amacıyla kullanılabilir. | MESHY_TASK_ID |
| `GLB` | GLB dosya biçiminde oluşturulan 3B model. | FILE3DGLB |
| `FBX` | FBX dosya biçiminde oluşturulan 3B model. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `9f7abcb0db3c78715e4ba7370efe294caf186590f7ab62da8568778848fc838c`
