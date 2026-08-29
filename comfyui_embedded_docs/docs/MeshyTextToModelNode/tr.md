# Meshy: Metinden Modele

Meshy: Text to Model düğümü, bir metin açıklamasından 3D model oluşturmak için Meshy API'sini kullanır. API'ye isteminiz ve ayarlarınızla bir istek gönderir, ardından oluşturmanın tamamlanmasını bekler ve sonuçta ortaya çıkan model dosyalarını indirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Oluşturma için kullanılacak AI model sürümünü belirtir. | COMBO | Evet | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `prompt` | Oluşturmak istediğiniz 3D modelin metin açıklaması. 1 ile 600 karakter arasında olmalıdır. | STRING | Evet | 1 - 600 karakter |
| `style` | Oluşturulan 3D model için sanatsal stil. | COMBO | Evet | `"realistic"` |
| `should_remesh` | false olarak ayarlandığında işlenmemiş bir üçgen mesh döndürür. "true" seçildiğinde topoloji ve hedef poligon sayısı için ek parametreler görüntülenir. | DYNAMIC_COMBO | Evet | `"true"`<br>`"false"` |
| `topology` | Yeniden meshlenen model için hedef poligon türü. Bu parametre yalnızca `should_remesh` parametresi "true" olarak ayarlandığında kullanılabilir. | COMBO | Hayır* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Yeniden meshlenen model için hedef poligon sayısı. Varsayılan değer 300000'dir. Bu parametre yalnızca `should_remesh` parametresi "true" olarak ayarlandığında kullanılabilir. | INT | Hayır* | 100 - 300000 |
| `symmetry_mode` | Oluşturulan modelde simetriyi kontrol eder. Bu gelişmiş bir parametredir. | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` |
| `pose_mode` | Oluşturulan model için poz modunu belirtir. Boş bir dize, belirli bir poz istenmediği anlamına gelir. Bu gelişmiş bir parametredir. | COMBO | Evet | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan değer 0'dır. | INT | Evet | 0 - 2147483647 |
| `ultra_mode` | Daha ince yüzey detaylarıyla daha yüksek doğruluklu geometri için ek bir iyileştirme geçişi çalıştırır. Varsayılan değer false'tur. | BOOLEAN | Evet | true<br>false |

*Not: `topology` ve `target_polycount` parametreleri koşullu olarak kullanılabilir. Bunlar yalnızca `should_remesh` parametresi "true" olarak ayarlandığında görünür.

`ultra_mode` etkinleştirildiğinde, `model` parametresi `"meshy-7"` veya `"latest"` olarak ayarlanmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Oluşturulan GLB modelinin dosya adı. Bu çıktı, geriye dönük uyumluluk için sağlanmıştır. | STRING |
| `meshy_görev_id` | Meshy API görevi için benzersiz tanımlayıcı. | MESHY_TASK_ID |
| `GLB` | GLB formatında oluşturulan 3D model dosyası. | FILE3DGLB |
| `FBX` | FBX formatında oluşturulan 3D model dosyası. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `131f17bfb788f206e15c1d48c877e822114902fadf073a6f9fb25e8340421122`
