# WanKameraYerleştirme

Bu düğüm, seçtiğiniz kamera yolu için Plücker gömlemelerini kullanarak bir kamera yörüngesi gömme tensörü üretir. Kaydırma, yakınlaştırma veya döndürme gibi hareketleri simüle eden bir kamera pozları dizisi oluşturur ve bunları video üretim işlem hatlarında kullanılabilecek bir gömme tensörüne dönüştürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `kamera_pozisyonu` | Simüle edilecek kamera hareketi türü (varsayılan: "Static") | COMBO | Evet | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" |
| `genişlik` | Çıktının piksel cinsinden genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `yükseklik` | Çıktının piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `uzunluk` | Kamera yörünge dizisinin uzunluğu (varsayılan: 81, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `hız` | Kamera hareketinin hızı (varsayılan: 1.0, adım: 0.1) | FLOAT | Hayır | 0.0 ile 10.0 |
| `fx` | Odak uzaklığı x parametresi (varsayılan: 0.5, adım: 0.000000001) | FLOAT | Hayır | 0.0 ile 1.0 |
| `fy` | Odak uzaklığı y parametresi (varsayılan: 0.5, adım: 0.000000001) | FLOAT | Hayır | 0.0 ile 1.0 |
| `cx` | Ana nokta x koordinatı (varsayılan: 0.5, adım: 0.01) | FLOAT | Hayır | 0.0 ile 1.0 |
| `cy` | Ana nokta y koordinatı (varsayılan: 0.5, adım: 0.01) | FLOAT | Hayır | 0.0 ile 1.0 |

Not: `fx`, `fy`, `cx` ve `cy` gelişmiş kamera içsel parametreleridir. `speed` parametresi, seçilen kamera hareketinin dönüş açısını ve öteleme mesafesini ölçekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `camera_embedding` | Yörünge dizisini içeren üretilmiş kamera gömme tensörü | TENSOR |
| `width` | İşleme için kullanılan genişlik değeri | INT |
| `height` | İşleme için kullanılan yükseklik değeri | INT |
| `length` | İşleme için kullanılan uzunluk değeri | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/tr.md)

---
**Source fingerprint (SHA-256):** `1a2f98d83d18033581823dee61b5a3686d560c749c55223f81febca89654a29f`
