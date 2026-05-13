> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/tr.md)

**Meshy: Image to Model** düğümü, tek bir giriş görüntüsünden 3B model oluşturmak için Meshy API'sini kullanır. Görüntünüzü yükler, bir işleme görevi gönderir ve oluşturulan 3B model dosyalarını (GLB ve FBX) referans için görev kimliğiyle birlikte döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"latest"` | Oluşturma için kullanılacak yapay zeka modeli sürümünü belirtir. |
| `image` | IMAGE | Evet | - | 3B modele dönüştürülecek giriş görüntüsü. |
| `should_remesh` | DYNAMIC COMBO | Evet | `"true"`<br>`"false"` | Oluşturulan ağın işlenip işlenmeyeceğini belirler. `"false"` olarak ayarlandığında, düğüm işlenmemiş bir üçgen ağ döndürür. |
| `topology` | COMBO | Hayır* | `"triangle"`<br>`"quad"` | Yeniden ağ oluşturulan model için hedef çokgen topolojisi. Bu girdi yalnızca `should_remesh` `"true"` olarak ayarlandığında kullanılabilir. |
| `target_polycount` | INT | Hayır* | 100 - 300000 | Yeniden ağ oluşturulan model için hedef çokgen sayısı. Bu girdi yalnızca `should_remesh` `"true"` olarak ayarlandığında kullanılabilir. Varsayılan değer 300000'dir. |
| `symmetry_mode` | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` | Oluşturulan 3B modele uygulanan simetriyi kontrol eder. |
| `should_texture` | DYNAMIC COMBO | Evet | `"true"`<br>`"false"` | Model için doku oluşturulup oluşturulmayacağını belirler. `"false"` olarak ayarlanması doku aşamasını atlar ve dokusuz bir ağ döndürür. |
| `enable_pbr` | BOOLEAN | Hayır* | - | `should_texture` `"true"` olduğunda, bu seçenek temel renge ek olarak PBR haritaları (metalik, pürüzlülük, normal) oluşturur. Varsayılan değer `False`'dur. |
| `texture_prompt` | STRING | Hayır* | - | Doku oluşturma sürecini yönlendiren bir metin istemi (maksimum 600 karakter). Bu girdi yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. `texture_image` ile aynı anda kullanılamaz. |
| `texture_image` | IMAGE | Hayır* | - | Doku oluşturma sürecini yönlendiren bir görüntü. Bu girdi yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. `texture_prompt` ile aynı anda kullanılamaz. |
| `pose_mode` | COMBO | Evet | `""` (boş)<br>`"A-pose"`<br>`"T-pose"` | Oluşturulan model için poz modunu belirtir. Bu gelişmiş bir parametredir. |
| `seed` | INT | Evet | 0 - 2147483647 | Oluşturma süreci için bir tohum değeri. Tohum değerinden bağımsız olarak sonuçlar deterministik değildir. Varsayılan değer 0'dır. |

**Parametre Kısıtlamaları Hakkında Not:**

* `topology` ve `target_polycount` girdileri yalnızca `should_remesh` `"true"` olarak ayarlandığında kullanılabilir.
* `enable_pbr`, `texture_prompt` ve `texture_image` girdileri yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir.
* `texture_prompt` ve `texture_image` aynı anda kullanılamaz. `should_texture` `"true"` iken her ikisi de sağlanırsa, düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `meshy_task_id` | STRING | Oluşturulan GLB modelinin dosya adı. (Geriye dönük uyumluluk için korunmaktadır). |
| `GLB` | MESHY_TASK_ID | Referans veya sorun giderme amacıyla kullanılabilen Meshy API görevi için benzersiz tanımlayıcı. |
| `FBX` | FILE3DGLB | GLB dosya formatında oluşturulan 3B model. |
| `FBX` | FILE3DFBX | FBX dosya formatında oluşturulan 3B model. |

---
**Source fingerprint (SHA-256):** `134d9250d8b447bbbd2905f827e81b67f491ba355ebb93d4d256324b644100a2`
