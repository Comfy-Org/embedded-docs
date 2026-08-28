# HiperDöşeme

HyperTile düğümü, görüntü üretimi sırasında bellek kullanımını optimize etmek için difüzyon modellerindeki dikkat mekanizmasına bir döşeme (tile) tekniği uygular. Gizli uzayı daha küçük döşemelere böler ve bunları ayrı ayrı işler, ardından sonuçları yeniden birleştirir. Bu sayede bellek tükenmesi yaşanmadan daha büyük görüntü boyutlarıyla çalışmayı sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | HyperTile optimizasyonunun uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `döşeme_boyutu` | İşleme için hedef döşeme boyutu (varsayılan: 256). Dahili olarak değer, minimum 32 olacak şekilde sınırlandırılır ve ardından etkin döşeme boyutunu elde etmek için 8'e bölünür. | INT | Evet | 1 - 2048 |
| `değiştirme_boyutu` | İşlem sırasında döşemelerin verimliliği artırmak için nasıl yeniden düzenleneceğini kontrol eder. Daha büyük değerler, döşeme boyutlarında daha fazla çeşitlilik sağlar (varsayılan: 2) | INT | Evet | 1 - 128 |
| `maks_derinlik` | Döşemenin uygulanacağı maksimum derinlik seviyesi (çözünürlük ölçeği). 0 değeri, döşemeyi yalnızca en yüksek çözünürlükte uygular (varsayılan: 0) | INT | Evet | 0 - 10 |
| `ölçek_derinliği` | Etkinleştirildiğinde, daha derin seviyelerde döşeme boyutu orantılı olarak ölçeklenir. Bu, daha düşük çözünürlüklerde kalitenin korunmasına yardımcı olabilir (varsayılan: False) | BOOLEAN | Evet | True / False |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | HyperTile optimizasyonu uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/tr.md)

---
**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`
