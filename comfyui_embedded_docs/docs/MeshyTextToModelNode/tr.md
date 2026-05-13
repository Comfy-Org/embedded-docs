> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/tr.md)

Meshy: Metinden Modele düğümü, bir metin açıklamasından 3B model oluşturmak için Meshy API'sini kullanır. İsteminiz ve ayarlarınızla API'ye bir istek gönderir, ardından oluşturma işleminin tamamlanmasını bekler ve sonuçta ortaya çıkan model dosyalarını indirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"latest"` | Kullanılacak AI model sürümünü belirtir. Şu anda yalnızca "latest" (en son) sürümü mevcuttur. |
| `prompt` | STRING | Evet | - | Oluşturmak istediğiniz 3B modelin metin açıklaması. 1 ile 600 karakter arasında olmalıdır. |
| `style` | COMBO | Evet | `"realistic"`<br>`"sculpture"` | Oluşturulan 3B model için sanatsal stil. |
| `should_remesh` | DYNAMIC COMBO | Evet | `"true"`<br>`"false"` | Oluşturulan ağın işlenip işlenmeyeceğini kontrol eder. "false" olarak ayarlandığında, düğüm işlenmemiş bir üçgen ağ döndürür. "true" seçildiğinde, topoloji ve çokgen sayısı için ek parametreler görünür hale gelir. |
| `topology` | COMBO | Hayır* | `"triangle"`<br>`"quad"` | Yeniden ağ oluşturulan model için hedef çokgen türü. Bu parametre yalnızca `should_remesh` "true" olarak ayarlandığında kullanılabilir ve zorunludur. |
| `target_polycount` | INT | Hayır* | 100 - 300000 | Yeniden ağ oluşturulan model için hedef çokgen sayısı. Varsayılan değer 300000'dir. Bu parametre yalnızca `should_remesh` "true" olarak ayarlandığında kullanılabilir ve zorunludur. |
| `symmetry_mode` | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` | Oluşturulan modelde simetriyi kontrol eder. |
| `pose_mode` | COMBO | Evet | `""`<br>`"A-pose"`<br>`"T-pose"` | Oluşturulan model için poz modunu belirtir. Boş bir dize, belirli bir poz istenmediği anlamına gelir. |
| `seed` | INT | Evet | 0 - 2147483647 | Oluşturma için bir tohum değeri. Bunu ayarlamak, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder, ancak tohum değeri ne olursa olsun sonuçlar deterministik değildir. Varsayılan değer 0'dır. |

*Not: `topology` ve `target_polycount` parametreleri koşullu olarak zorunludur. Bunlar yalnızca `should_remesh` parametresi "true" olarak ayarlandığında görünür ve ayarlanmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `meshy_görev_id` | STRING | Oluşturulan GLB modelinin dosya adı. Bu çıktı, geriye dönük uyumluluk için sağlanmıştır. |
| `GLB` | MESHY_TASK_ID | Meshy API görevi için benzersiz tanımlayıcı. |
| `FBX` | FILE3DGLB | GLB formatında oluşturulan 3B model dosyası. |
| `FBX` | FILE3DFBX | FBX formatında oluşturulan 3B model dosyası. |

---
**Source fingerprint (SHA-256):** `122eee5488a89433bd1f3bf79ccd8e9c51fd23cc1dfb208c39a0628c2ad3d817`
