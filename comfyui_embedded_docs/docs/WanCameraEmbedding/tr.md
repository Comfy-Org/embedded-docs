# WanKameraYerleştirme

WanCameraEmbedding düğümü, kamera hareket parametrelerine dayalı olarak Plücker gömmeleri kullanarak kamera yörüngesi gömmeleri oluşturur. Farklı kamera hareketlerini simüle eden bir dizi kamera pozu oluşturur ve bunları video oluşturma hatlarına uygun gömmeli tensörlere dönüştürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `kamera_pozisyonu` | Simüle edilecek kamera hareketinin türü (varsayılan: "Statik") | COMBO | Evet | "Statik"<br>"Yukarı Kaydır"<br>"Aşağı Kaydır"<br>"Sola Kaydır"<br>"Sağa Kaydır"<br>"Yakınlaştır"<br>"Uzaklaştır"<br>"Saat Yönünün Tersine (SYT)"<br>"Saat Yönünde (SY)" |
| `genişlik` | Çıktının piksel cinsinden genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 ile MAKS_ÇÖZÜNÜRLÜK |
| `yükseklik` | Çıktının piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 ile MAKS_ÇÖZÜNÜRLÜK |
| `uzunluk` | Kamera yörüngesi dizisinin uzunluğu (varsayılan: 81, adım: 4) | INT | Evet | 1 ile MAKS_ÇÖZÜNÜRLÜK |
| `hız` | Kamera hareketinin hızı (varsayılan: 1,0, adım: 0,1) | FLOAT | Hayır | 0,0 ile 10,0 |
| `fx` | Odak uzaklığı x parametresi (varsayılan: 0,5, adım: 0,000000001) | FLOAT | Hayır | 0,0 ile 1,0 |
| `fy` | Odak uzaklığı y parametresi (varsayılan: 0,5, adım: 0,000000001) | FLOAT | Hayır | 0,0 ile 1,0 |
| `cx` | Ana nokta x koordinatı (varsayılan: 0,5, adım: 0,01) | FLOAT | Hayır | 0,0 ile 1,0 |
| `cy` | Ana nokta y koordinatı (varsayılan: 0,5, adım: 0,01) | FLOAT | Hayır | 0,0 ile 1,0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `kamera_yerleştirme` | Yörünge dizisini içeren oluşturulmuş kamera gömme tensörü | TENSOR |
| `genişlik` | İşleme için kullanılan genişlik değeri | INT |
| `yükseklik` | İşleme için kullanılan yükseklik değeri | INT |
| `uzunluk` | İşleme için kullanılan uzunluk değeri | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/tr.md)

---
**Source fingerprint (SHA-256):** `422c4a1fdfb6fd403afac26a609f80cbdbaa87f2c115068de9d7a33c756e71fd`
