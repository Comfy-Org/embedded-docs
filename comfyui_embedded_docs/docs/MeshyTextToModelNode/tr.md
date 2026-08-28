# Meshy: Metinden Modele

Meshy: Text to Model düğümü, bir metin açıklamasından 3B model oluşturmak için Meshy API'sini kullanır. İsteminizi ve ayarlarınızı API'ye bir istek olarak gönderir, ardından oluşturmanın tamamlanmasını bekler ve sonuçta oluşan model dosyalarını indirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak AI model sürümünü belirtir. Şu anda yalnızca "latest" sürümü mevcuttur. | COMBO | Evet | `"latest"` |
| `prompt` | Oluşturmak istediğiniz 3B modelin metin açıklaması. 1 ile 600 karakter arasında olmalıdır. | STRING | Evet | - |
| `style` | Oluşturulan 3B model için sanatsal stil. | COMBO | Evet | `"realistic"`<br>`"sculpture"` |
| `should_remesh` | Oluşturulan mesh'in işlenip işlenmediğini kontrol eder. "false" olarak ayarlandığında düğüm, işlenmemiş bir üçgen mesh döndürür. "true" seçildiğinde topoloji ve poligon sayısı için ek parametreler görüntülenir. | DYNAMIC_COMBO | Evet | `"true"`<br>`"false"` |
| `topology` | Yeniden meshlenmiş model için hedef poligon türü. Bu parametre yalnızca `should_remesh` "true" olarak ayarlandığında kullanılabilir. | COMBO | Hayır* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Yeniden meshlenmiş model için hedef poligon sayısı. Varsayılan 300000'dir. Bu parametre yalnızca `should_remesh` "true" olarak ayarlandığında kullanılabilir. | INT | Hayır* | 100 - 300000 |
| `symmetry_mode` | Oluşturulan modelde simetriyi kontrol eder. Bu gelişmiş bir parametredir. | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` |
| `pose_mode` | Oluşturulan model için poze modunu belirtir. Boş bir dize, belirli bir poze istenmediği anlamına gelir. Bu gelişmiş bir parametredir. | COMBO | Evet | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan 0'dır. | INT | Evet | 0 - 2147483647 |

*Not: `topology` ve `target_polycount` parametreleri koşullu olarak kullanılabilir. Bu parametreler yalnızca `should_remesh` parametresi "true" olarak ayarlandığında görünür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Oluşturulan GLB modelinin dosya adı. Bu çıktı, geriye dönük uyumluluk için sağlanmıştır. | STRING |
| `meshy_görev_id` | Meshy API görevi için benzersiz tanımlayıcı. | MESHY_TASK_ID |
| `GLB` | GLB formatında oluşturulan 3B model dosyası. | FILE3DGLB |
| `FBX` | FBX formatında oluşturulan 3B model dosyası. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `1860b2d760aa81d611d4f44114591b4d98ccb85075bd1e06beabf462fb58bd53`
