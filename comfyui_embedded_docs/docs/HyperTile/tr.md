# HiperDöşeme

HyperTile düğümü, görüntü oluşturma sırasında bellek kullanımını optimize etmek için difüzyon modellerindeki dikkat mekanizmasına bir döşeme tekniği uygular. Gizli alanı daha küçük döşemelere böler, bunları ayrı ayrı işler ve ardından sonuçları yeniden birleştirir. Bu, bellek yetersizliği sorunu yaşamadan daha büyük görüntü boyutlarıyla çalışmayı sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | HyperTile optimizasyonunun uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `döşeme_boyutu` | İşleme için hedef döşeme boyutu (varsayılan: 256). Etkin döşeme boyutu, 8'in katına yuvarlanır ve minimum 32'dir. | INT | Hayır | 1 - 2048 |
| `değiştirme_boyutu` | Verimliliği artırmak için işleme sırasında döşemelerin nasıl yeniden düzenleneceğini kontrol eder (varsayılan: 2) | INT | Hayır | 1 - 128 |
| `maks_derinlik` | Döşemenin uygulanacağı maksimum derinlik seviyesi (çözünürlük ölçeği). 0 değeri, döşemeyi yalnızca en yüksek çözünürlükte uygular (varsayılan: 0) | INT | Hayır | 0 - 10 |
| `ölçek_derinliği` | Etkinleştirildiğinde, döşeme boyutu daha derin derinlik seviyelerinde orantılı olarak ölçeklenir. Bu, daha düşük çözünürlüklerde kalitenin korunmasına yardımcı olabilir (varsayılan: False) | BOOLEAN | Hayır | True / False |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | HyperTile optimizasyonu uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/tr.md)

---
**Source fingerprint (SHA-256):** `d3c55e6a38abecc8fe612dbb91a3ba26de9bc5cf8a187f01cf4746550f62f40a`
