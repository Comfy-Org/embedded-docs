# Meshy: Metinden Modele

Meshy: Text to Model düğümü, bir metin açıklamasından 3B model oluşturmak için Meshy API'sini kullanır. API'ye isteminiz ve ayarlarınızla bir istek gönderir, ardından oluşturmanın tamamlanmasını bekler ve ortaya çıkan model dosyalarını indirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Oluşturma için kullanılacak yapay zeka model sürümünü belirtir. | COMBO | Evet | `"meshy-7.1"`<br>`"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `prompt` | Oluşturmak istediğiniz 3B modelin metin açıklaması. 1 ile 600 karakter arasında olmalıdır. Varsayılan değer boş bir dizedir. | STRING | Evet | 1 - 600 karakter |
| `style` | Oluşturulan 3B model için sanatsal stil. | COMBO | Evet | `"realistic"` |
| `should_remesh` | false olarak ayarlandığında, işlenmemiş bir üçgen ağ döndürür. "true" seçildiğinde topoloji ve hedef poligon sayısı için ek parametreler görünür. | DYNAMIC_COMBO | Evet | `"true"`<br>`"false"` |
| `topology` | Yeniden ağ oluşturulmuş model için hedef poligon türü. Bu parametre yalnızca `should_remesh` "true" olarak ayarlandığında kullanılabilir. | COMBO | Hayır* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Yeniden ağ oluşturulmuş model için hedef poligon sayısı. Varsayılan değer 300000'dir. Bu parametre yalnızca `should_remesh` "true" olarak ayarlandığında kullanılabilir. | INT | Hayır* | 100 - 300000 |
| `symmetry_mode` | Oluşturulan modelde simetriyi kontrol eder. Bu gelişmiş bir parametredir. Seçenekler `"auto"`, `"on"` ve `"off"` şeklindedir. | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` |
| `pose_mode` | Oluşturulan model için poz modunu belirtin. Boş bir dize, belirli bir poz istenmediği anlamına gelir. Bu gelişmiş bir parametredir. | COMBO | Evet | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan değer 0'dır. | INT | Evet | 0 - 2147483647 |
| `ultra_mode` | Daha ince yüzey ayrıntısıyla daha yüksek sadakatli geometri için ek bir iyileştirme geçişi çalıştırır. Varsayılan değer false'tur. | BOOLEAN | Evet | true<br>false |
| `ultra_resolution` | Ultra geçişinin çözünürlüğü: `"2k"` bunu 2048³'te, `"4k"` ise en ince yüzey ayrıntısı için 4096³'te çalıştırır. `"4k"` için `"meshy-7.1"` veya `"latest"` modeli gerekir. Yalnızca `ultra_mode` etkinleştirildiğinde kullanılır (varsayılan: `"2k"`). | COMBO | Hayır | `"2k"`<br>`"4k"` |

*Not: `topology` ve `target_polycount` parametreleri koşullu olarak kullanılabilir. Yalnızca `should_remesh` parametresi "true" olarak ayarlandığında görünürler.

`ultra_mode` etkinleştirildiğinde, `model` parametresi `"meshy-7.1"`, `"meshy-7"` veya `"latest"` olarak ayarlanmalıdır; başka bir model seçilirse hata verilir. `"meshy-7"` ile ultra geçiş her zaman 2048³'te çalışır ve `"4k"` ultra çözünürlüğü `"meshy-7.1"` veya `"latest"` gerektirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Oluşturulan GLB modelinin dosya adı. Bu çıktı geriye dönük uyumluluk için sağlanmıştır. | STRING |
| `meshy_task_id` | Meshy API görevi için benzersiz tanımlayıcı. | MESHY_TASK_ID |
| `GLB` | GLB biçiminde oluşturulan 3B model dosyası. | FILE3DGLB |
| `FBX` | FBX biçiminde oluşturulan 3B model dosyası. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `a02a5ae28bcae343c628d11ba3efa952b61b8bdf867669f58f1beb0f7c9e49f9`
