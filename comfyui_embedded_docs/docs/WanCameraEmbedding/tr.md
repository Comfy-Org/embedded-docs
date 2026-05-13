> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/tr.md)

WanCameraEmbedding düğümü, kamera hareket parametrelerine dayalı olarak Plücker gömmeleri kullanarak kamera yörüngesi gömmeleri oluşturur. Farklı kamera hareketlerini simüle eden bir dizi kamera pozu oluşturur ve bunları video oluşturma hatlarına uygun gömmeli tensörlere dönüştürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `kamera_pozisyonu` | COMBO | Evet | "Statik"<br>"Yukarı Kaydır"<br>"Aşağı Kaydır"<br>"Sola Kaydır"<br>"Sağa Kaydır"<br>"Yakınlaştır"<br>"Uzaklaştır"<br>"Saat Yönünün Tersine (SYT)"<br>"Saat Yönünde (SY)" | Simüle edilecek kamera hareketinin türü (varsayılan: "Statik") |
| `genişlik` | INT | Evet | 16 ile MAKS_ÇÖZÜNÜRLÜK | Çıktının piksel cinsinden genişliği (varsayılan: 832, adım: 16) |
| `yükseklik` | INT | Evet | 16 ile MAKS_ÇÖZÜNÜRLÜK | Çıktının piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) |
| `uzunluk` | INT | Evet | 1 ile MAKS_ÇÖZÜNÜRLÜK | Kamera yörüngesi dizisinin uzunluğu (varsayılan: 81, adım: 4) |
| `hız` | FLOAT | Hayır | 0,0 ile 10,0 | Kamera hareketinin hızı (varsayılan: 1,0, adım: 0,1) |
| `fx` | FLOAT | Hayır | 0,0 ile 1,0 | Odak uzaklığı x parametresi (varsayılan: 0,5, adım: 0,000000001) |
| `fy` | FLOAT | Hayır | 0,0 ile 1,0 | Odak uzaklığı y parametresi (varsayılan: 0,5, adım: 0,000000001) |
| `cx` | FLOAT | Hayır | 0,0 ile 1,0 | Ana nokta x koordinatı (varsayılan: 0,5, adım: 0,01) |
| `cy` | FLOAT | Hayır | 0,0 ile 1,0 | Ana nokta y koordinatı (varsayılan: 0,5, adım: 0,01) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `genişlik` | TENSOR | Yörünge dizisini içeren oluşturulmuş kamera gömme tensörü |
| `yükseklik` | INT | İşleme için kullanılan genişlik değeri |
| `uzunluk` | INT | İşleme için kullanılan yükseklik değeri |
| `uzunluk` | INT | İşleme için kullanılan uzunluk değeri |

---
**Source fingerprint (SHA-256):** `422c4a1fdfb6fd403afac26a609f80cbdbaa87f2c115068de9d7a33c756e71fd`
