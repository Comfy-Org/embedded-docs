# Meshy: Görüntüden Modele

**Meshy: Image to Model** düğümü, tek bir giriş görüntüsünden 3B model oluşturmak için Meshy API'sini kullanır. Görüntünüzü yükler, bir işleme görevi gönderir ve oluşturulan 3B model dosyalarını (GLB ve FBX) referans için görev kimliğiyle birlikte döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Oluşturma için kullanılacak yapay zeka modeli sürümünü belirtir. | COMBO | Evet | `"latest"` |
| `image` | 3B modele dönüştürülecek giriş görüntüsü. | IMAGE | Evet | - |
| `should_remesh` | Oluşturulan ağın işlenip işlenmeyeceğini belirler. `"false"` olarak ayarlandığında, düğüm işlenmemiş bir üçgen ağ döndürür. | DYNAMIC COMBO | Evet | `"true"`<br>`"false"` |
| `topology` | Yeniden ağ oluşturulan model için hedef çokgen topolojisi. Bu girdi yalnızca `should_remesh` `"true"` olarak ayarlandığında kullanılabilir. | COMBO | Hayır* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Yeniden ağ oluşturulan model için hedef çokgen sayısı. Bu girdi yalnızca `should_remesh` `"true"` olarak ayarlandığında kullanılabilir. Varsayılan değer 300000'dir. | INT | Hayır* | 100 - 300000 |
| `symmetry_mode` | Oluşturulan 3B modele uygulanan simetriyi kontrol eder. | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | Model için doku oluşturulup oluşturulmayacağını belirler. `"false"` olarak ayarlanması doku aşamasını atlar ve dokusuz bir ağ döndürür. | DYNAMIC COMBO | Evet | `"true"`<br>`"false"` |
| `enable_pbr` | `should_texture` `"true"` olduğunda, bu seçenek temel renge ek olarak PBR haritaları (metalik, pürüzlülük, normal) oluşturur. Varsayılan değer `False`'dur. | BOOLEAN | Hayır* | - |
| `texture_prompt` | Doku oluşturma sürecini yönlendiren bir metin istemi (maksimum 600 karakter). Bu girdi yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. `texture_image` ile aynı anda kullanılamaz. | STRING | Hayır* | - |
| `texture_image` | Doku oluşturma sürecini yönlendiren bir görüntü. Bu girdi yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. `texture_prompt` ile aynı anda kullanılamaz. | IMAGE | Hayır* | - |
| `pose_mode` | Oluşturulan model için poz modunu belirtir. Bu gelişmiş bir parametredir. | COMBO | Evet | `""` (boş)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Oluşturma süreci için bir tohum değeri. Tohum değerinden bağımsız olarak sonuçlar deterministik değildir. Varsayılan değer 0'dır. | INT | Evet | 0 - 2147483647 |

**Parametre Kısıtlamaları Hakkında Not:**

* `topology` ve `target_polycount` girdileri yalnızca `should_remesh` `"true"` olarak ayarlandığında kullanılabilir.
* `enable_pbr`, `texture_prompt` ve `texture_image` girdileri yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir.
* `texture_prompt` ve `texture_image` aynı anda kullanılamaz. `should_texture` `"true"` iken her ikisi de sağlanırsa, düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `meshy_task_id` | Oluşturulan GLB modelinin dosya adı. (Geriye dönük uyumluluk için korunmaktadır). | STRING |
| `GLB` | Referans veya sorun giderme amacıyla kullanılabilen Meshy API görevi için benzersiz tanımlayıcı. | MESHY_TASK_ID |
| `FBX` | GLB dosya formatında oluşturulan 3B model. | FILE3DGLB |
| `FBX` | FBX dosya formatında oluşturulan 3B model. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `134d9250d8b447bbbd2905f827e81b67f491ba355ebb93d4d256324b644100a2`
