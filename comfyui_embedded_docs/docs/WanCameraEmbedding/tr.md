# WanKameraYerleştirme

WanCameraEmbedding düğümü, kamera hareket parametrelerine dayalı Plücker embedding'lerini kullanarak kamera yörünge embedding'leri üretir. Farklı kamera hareketlerini simüle eden bir dizi kamera pozu oluşturur ve bunları video üretim hatlarına uygun embedding tensörlerine dönüştürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `kamera_pozisyonu` | Simüle edilecek kamera hareketinin türü (varsayılan: "Static") | COMBO | Evet | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" |
| `genişlik` | Çıktının piksel cinsinden genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 ile MAX_RESOLUTION arası |
| `yükseklik` | Çıktının piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 ile MAX_RESOLUTION arası |
| `uzunluk` | Kamera yörünge dizisinin uzunluğu (varsayılan: 81, adım: 4) | INT | Evet | 1 ile MAX_RESOLUTION arası |
| `hız` | Kamera hareketinin hızı (varsayılan: 1.0, adım: 0.1) | FLOAT | Hayır | 0.0 ile 10.0 arası |
| `fx` | Odak uzaklığı x parametresi (varsayılan: 0.5, adım: 0.000000001) | FLOAT | Hayır | 0.0 ile 1.0 arası |
| `fy` | Odak uzaklığı y parametresi (varsayılan: 0.5, adım: 0.000000001) | FLOAT | Hayır | 0.0 ile 1.0 arası |
| `cx` | Asal nokta x koordinatı (varsayılan: 0.5, adım: 0.01) | FLOAT | Hayır | 0.0 ile 1.0 arası |
| `cy` | Asal nokta y koordinatı (varsayılan: 0.5, adım: 0.01) | FLOAT | Hayır | 0.0 ile 1.0 arası |

Not: `fx`, `fy`, `cx` ve `cy` gelişmiş kamera iç parametreleridir. `speed` parametresi, seçilen kamera hareketinin dönüş açısını ve öteleme mesafesini ölçekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `kamera_yerleştirme` | Yörünge dizisini içeren oluşturulmuş kamera embedding tensörü | TENSOR |
| `genişlik` | İşleme için kullanılan genişlik değeri | INT |
| `yükseklik` | İşleme için kullanılan yükseklik değeri | INT |
| `uzunluk` | İşleme için kullanılan uzunluk değeri | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/tr.md)

---
**Source fingerprint (SHA-256):** `1a2f98d83d18033581823dee61b5a3686d560c749c55223f81febca89654a29f`
