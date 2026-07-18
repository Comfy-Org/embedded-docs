Meshy: Metinden Modele düğümü, bir metin açıklamasından 3B model oluşturmak için Meshy API'sini kullanır. İsteminiz ve ayarlarınızla API'ye bir istek gönderir, ardından oluşturma işleminin tamamlanmasını bekler ve sonuçta ortaya çıkan model dosyalarını indirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak AI model sürümünü belirtir. Şu anda yalnızca "latest" (en son) sürümü mevcuttur. | COMBO | Evet | `"latest"` |
| `prompt` | Oluşturmak istediğiniz 3B modelin metin açıklaması. 1 ile 600 karakter arasında olmalıdır. | STRING | Evet | - |
| `style` | Oluşturulan 3B model için sanatsal stil. | COMBO | Evet | `"realistic"`<br>`"sculpture"` |
| `should_remesh` | Oluşturulan ağın işlenip işlenmeyeceğini kontrol eder. "false" olarak ayarlandığında, düğüm işlenmemiş bir üçgen ağ döndürür. "true" seçildiğinde, topoloji ve çokgen sayısı için ek parametreler görünür hale gelir. | DYNAMIC COMBO | Evet | `"true"`<br>`"false"` |
| `topology` | Yeniden ağ oluşturulan model için hedef çokgen türü. Bu parametre yalnızca `should_remesh` "true" olarak ayarlandığında kullanılabilir ve zorunludur. | COMBO | Hayır* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Yeniden ağ oluşturulan model için hedef çokgen sayısı. Varsayılan değer 300000'dir. Bu parametre yalnızca `should_remesh` "true" olarak ayarlandığında kullanılabilir ve zorunludur. | INT | Hayır* | 100 - 300000 |
| `symmetry_mode` | Oluşturulan modelde simetriyi kontrol eder. | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` |
| `pose_mode` | Oluşturulan model için poz modunu belirtir. Boş bir dize, belirli bir poz istenmediği anlamına gelir. | COMBO | Evet | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Oluşturma için bir tohum değeri. Bunu ayarlamak, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder, ancak tohum değeri ne olursa olsun sonuçlar deterministik değildir. Varsayılan değer 0'dır. | INT | Evet | 0 - 2147483647 |

*Not: `topology` ve `target_polycount` parametreleri koşullu olarak zorunludur. Bunlar yalnızca `should_remesh` parametresi "true" olarak ayarlandığında görünür ve ayarlanmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model_dosyası` | Oluşturulan GLB modelinin dosya adı. Bu çıktı, geriye dönük uyumluluk için sağlanmıştır. | STRING |
| `meshy_görev_id` | Meshy API görevi için benzersiz tanımlayıcı. | MESHY_TASK_ID |
| `GLB` | GLB formatında oluşturulan 3B model dosyası. | FILE3DGLB |
| `FBX` | FBX formatında oluşturulan 3B model dosyası. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `122eee5488a89433bd1f3bf79ccd8e9c51fd23cc1dfb208c39a0628c2ad3d817`
