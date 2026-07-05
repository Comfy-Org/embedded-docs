# CropByBBoxes

CropByBBoxes düğümü, bir giriş görüntü kümesinden belirli dikdörtgen bölgeleri çıkarır ve yeniden boyutlandırır. Kırpılacak alanı tanımlamak için sağlanan sınırlayıcı kutu koordinatlarını kullanır. Kırpılan bölgeler daha sonra belirtilen bir çıktı boyutuna yeniden boyutlandırılır ve kırpılan alanı esnetme veya orijinal en-boy oranını korumak için dolgu ekleme seçenekleri sunar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Kırpılacak giriş görüntü kümesi. | IMAGE | Evet | - |
| `sınırlayıcı_kutular` | Kırpılacak bölgeleri tanımlayan sınırlayıcı kutuların listesi. Bu girdi zorunludur, yani bağlı olmalıdır. | BOUNDINGBOX | Evet | - |
| `çıktı_genişliği` | Her kırpılan alanın yeniden boyutlandırıldığı genişlik (varsayılan: 512). | INT | Hayır | 64 - 4096 |
| `çıktı_yüksekliği` | Her kırpılan alanın yeniden boyutlandırıldığı yükseklik (varsayılan: 512). | INT | Hayır | 64 - 4096 |
| `dolgu` | Kırpmadan önce sınırlayıcı kutunun her bir kenarına piksel cinsinden eklenen ekstra dolgu (varsayılan: 0). | INT | Hayır | 0 - 1024 |
| `oranı_koru` | Kırpılan alanın çıktı boyutuna sığması için esnetilip esnetilmeyeceği veya en-boy oranını korumak için siyah piksellerle doldurulup doldurulmayacağı (varsayılan: "stretch"). | COMBO | Hayır | `"stretch"`<br>`"pad"` |

**Not:** Düğüm, her seferinde bir görüntü karesini işler. Tek bir kare için birden fazla sınırlayıcı kutu sağlanırsa, tüm sağlanan kutuların birleşimi (tüm kutuları içeren en küçük dikdörtgen) olan tek bir kırpma bölgesi hesaplar. Hesaplanan bir kırpma bölgesi geçersizse (örneğin, sıfır genişlik veya yükseklik), düğüm görüntünün üst-orta kısmından bir yedek kırpma oluşturur.


| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Kırpılan ve yeniden boyutlandırılan tüm bölgeler, tek bir görüntü kümesinde birleştirilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropByBBoxes/tr.md)

---
**Source fingerprint (SHA-256):** `9c0b3078405567911731c42e1873c57c77363e21ef6805769730667c811b0a0b`
