Bu düğüm, Tencent'in Hunyuan3D Pro API'sini kullanarak bir metin açıklamasından 3B model oluşturur. Bir oluşturma görevi oluşturmak için istek gönderir, sonucu yoklar ve nihai model dosyalarını GLB ve OBJ formatlarında indirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Hunyuan3D modelinin sürümü. `3.1` modeli için LowPoly seçeneği kullanılamaz. | COMBO | Evet | `"3.0"`<br>`"3.1"` |
| `istem` | Oluşturulacak 3B modelin metin açıklaması. En fazla 1024 karakter destekler. | STRING | Evet | - |
| `yüz sayısı` | Oluşturulan 3B model için hedef yüz sayısı. Varsayılan: 500000. | INT | Evet | 3000 - 1500000 |
| `oluşturma türü` | Oluşturulacak 3B modelin türü. Mevcut seçenekler ve bunlarla ilişkili parametreler şunlardır:<br>- **Normal**: Standart bir model oluşturur. Bir `pbr` parametresi içerir (varsayılan: `False`).<br>- **LowPoly**: Düşük çokgenli bir model oluşturur. `polygon_type` (`"triangle"` veya `"quadrilateral"`) ve `pbr` (varsayılan: `False`) parametrelerini içerir.<br>- **Geometry**: Yalnızca geometri içeren bir model oluşturur. | DYNAMICCOMBO | Evet | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` |
| `tohum` | Oluşturma için bir tohum değeri. Tohumdan bağımsız olarak sonuçlar deterministik değildir. Yeni bir tohum ayarlamak, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder. Varsayılan: 0. | INT | Hayır | 0 - 2147483647 |

**Not:** `generate_type` parametresi dinamiktir. `"LowPoly"` seçeneğinin seçilmesi, `polygon_type` ve `pbr` için ek girdileri ortaya çıkaracaktır. `"Normal"` seçeneğinin seçilmesi, `pbr` için bir girdi ortaya çıkaracaktır. `"Geometry"` seçeneğinin seçilmesi, herhangi bir ek girdi ortaya çıkarmayacaktır.

**Kısıtlama:** `"LowPoly"` oluşturma türü, `"3.1"` modeliyle kullanılamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `GLB` | Geriye dönük uyumluluk için eski bir çıktı. | STRING |
| `OBJ` | GLB dosya formatında oluşturulan 3B model. | FILE3DGLB |
| `doku_görseli` | OBJ dosya formatında oluşturulan 3B model. | FILE3DOBJ |
| `texture_image` | Varsa, oluşturulan OBJ dosyasından çıkarılan doku görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentTextToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `e35f5165941cc7761639dd72e78141326d37d5e169be9a0e326afcbcdc572b7d`
