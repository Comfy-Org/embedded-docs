> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/tr.md)

WanCameraEmbedding düğümü, kamera hareket parametrelerine dayalı olarak Plücker gömme yöntemini kullanarak kamera yörünge gömme vektörleri oluşturur. Farklı kamera hareketlerini simüle eden bir kamera poz dizisi oluşturur ve bunları video üretim işlem hatları için uygun gömme tensörlerine dönüştürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `camera_pose` | COMBO | Evet | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" | Simüle edilecek kamera hareket türü (varsayılan: "Static") |
| `width` | INT | Evet | 16'dan MAX_RESOLUTION'a | Çıktının piksel cinsinden genişliği (varsayılan: 832, adım: 16) |
| `height` | INT | Evet | 16'dan MAX_RESOLUTION'a | Çıktının piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) |
| `length` | INT | Evet | 1'den MAX_RESOLUTION'a | Kamera yörünge dizisinin uzunluğu (varsayılan: 81, adım: 4) |
| `speed` | FLOAT | Hayır | 0.0 ile 10.0 arası | Kamera hareketinin hızı (varsayılan: 1.0, adım: 0.1) |
| `fx` | FLOAT | Hayır | 0.0 ile 1.0 arası | Odak uzaklığı x parametresi (varsayılan: 0.5, adım: 0.000000001) |
| `fy` | FLOAT | Hayır | 0.0 ile 1.0 arası | Odak uzaklığı y parametresi (varsayılan: 0.5, adım: 0.000000001) |
| `cx` | FLOAT | Hayır | 0.0 ile 1.0 arası | Ana nokta x koordinatı (varsayılan: 0.5, adım: 0.01) |
| `cy` | FLOAT | Hayır | 0.0 ile 1.0 arası | Ana nokta y koordinatı (varsayılan: 0.5, adım: 0.01) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `camera_embedding` | TENSOR | Yörünge dizisini içeren oluşturulmuş kamera gömme tensörü |
| `width` | INT | İşleme için kullanılan genişlik değeri |
| `height` | INT | İşleme için kullanılan yükseklik değeri |
| `length` | INT | İşleme için kullanılan uzunluk değeri |