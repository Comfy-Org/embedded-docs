# HiperDöşeme

HyperTile, görüntü üretimi sırasında bellek kullanımını azaltmak için difüzyon modellerinin içindeki dikkat mekanizmasına bir döşeme tekniği uygular. Latent uzayını daha küçük döşemelere böler, her döşeme için dikkati ayrı ayrı işler ve ardından sonuçları yeniden birleştirir. Bu, bellek tükenmeden daha büyük görüntü boyutlarıyla çalışmayı mümkün kılar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | HyperTile optimizasyonunun uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `tile_size` | İşleme için hedef döşeme boyutu (varsayılan: 256). Dahili olarak değer en az 32 olacak şekilde sınırlandırılır ve ardından etkin döşeme boyutunu elde etmek için 8'e bölünür. | INT | Evet | 1 - 2048 |
| `swap_size` | İşleme sırasında döşemelerin verimliliği artırmak için nasıl yeniden düzenlendiğini kontrol eder. Daha büyük değerler döşeme boyutlarında daha fazla çeşitliliğe izin verir (varsayılan: 2) | INT | Evet | 1 - 128 |
| `max_depth` | Döşemenin uygulanacağı maksimum derinlik düzeyi (çözünürlük ölçeği). 0 değeri döşemeyi yalnızca en yüksek çözünürlükte uygular (varsayılan: 0) | INT | Evet | 0 - 10 |
| `scale_depth` | Etkinleştirildiğinde, döşeme boyutu daha derin derinlik düzeylerinde orantılı olarak ölçeklenir. Bu, daha düşük çözünürlüklerde kaliteyi korumaya yardımcı olabilir (varsayılan: False) | BOOLEAN | Evet | True / False |

Not: `tile_size`, `swap_size`, `max_depth` ve `scale_depth` gelişmiş girdiler olarak işaretlenmiştir, bu nedenle yalnızca arayüzde gelişmiş seçenekler etkinleştirildiğinde gösterilirler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | HyperTile optimizasyonu uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/tr.md)

---
**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`
