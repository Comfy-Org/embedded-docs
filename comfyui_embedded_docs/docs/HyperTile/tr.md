# HiperDöşeme

HyperTile düğümü, görüntü üretimi sırasında bellek kullanımını optimize etmek için difüzyon modellerindeki dikkat mekanizmasına bir döşeme (tiling) tekniği uygular. Gizli uzayı daha küçük döşemelere böler ve bunları ayrı ayrı işler, ardından sonuçları yeniden birleştirir. Bu, bellek tükenmeden daha büyük görüntü boyutlarıyla çalışmayı sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | HyperTile optimizasyonunun uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `tile_size` | İşleme için hedef döşeme boyutu (varsayılan: 256). Etkin döşeme boyutu, minimum 32 olmak üzere 8'in katına aşağı yuvarlanır. | INT | Hayır | 1 - 2048 |
| `swap_size` | Düğümün görüntüyü nasıl böleceğini rastgele seçerken göz önünde bulundurduğu aday döşeme bölme sayısı. Daha büyük bir değer, bölme işleminde daha fazla çeşitlilik sağlar (varsayılan: 2) | INT | Hayır | 1 - 128 |
| `max_depth` | Döşemenin uygulanacağı maksimum derinlik seviyesi (çözünürlük ölçeği). 0 değeri, döşemeyi yalnızca en yüksek çözünürlükte uygular (varsayılan: 0) | INT | Hayır | 0 - 10 |
| `scale_depth` | Etkinleştirildiğinde, döşeme boyutu daha derin derinlik seviyelerinde orantılı olarak ölçeklenir. Bu, daha düşük çözünürlüklerde kalitenin korunmasına yardımcı olabilir (varsayılan: False) | BOOLEAN | Hayır | True / False |

Not: `scale_depth` yalnızca `max_depth` 0'dan büyük olduğunda etkilidir, çünkü en yüksek çözünürlük seviyesinde (derinlik 0) döşeme boyutu asla ölçeklenmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | HyperTile optimizasyonu uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/tr.md)

---
**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`
