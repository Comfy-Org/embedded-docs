# Tripo: Çok Bakışlıdan Modele

Bu düğüm, bir nesnenin farklı görünümlerini (ön, sol, arka, sağ) gösteren en fazla dört görüntüyü işleyerek Tripo'nun API'sini kullanarak 3B modelleri eşzamanlı olarak üretir. 3B modeli oluşturmak için bir ön görüntü ve en az bir ek görünüm (sol, arka veya sağ) gerektirir. Doku, PBR malzeme, geometri kalitesi ve çıktı biçimi düğümden denetlenebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Nesnenin ön görünüm görüntüsü. | IMAGE | Evet | - |
| `sol_görüntü` | Nesnenin sol görünüm görüntüsü. | IMAGE | Hayır | - |
| `arka_görüntü` | Nesnenin arka görünüm görüntüsü. | IMAGE | Hayır | - |
| `sağ_görüntü` | Nesnenin sağ görünüm görüntüsü. | IMAGE | Hayır | - |
| `model_versiyonu` | Üretim için kullanılacak model sürümü. | COMBO | Hayır | Birden çok seçenek mevcut |
| `yönlendirme` | 3B model için yönelim ayarı (varsayılan: `"default"`). | COMBO | Hayır | Birden çok seçenek mevcut |
| `doku` | Doku haritaları üret. Kapalı olduğunda çıplak geometri döndürür ve pbr yok sayılır. (varsayılan: True) | BOOLEAN | Hayır | - |
| `pbr` | PBR malzeme haritaları (temel renk, metalik, pürüzlülük, normal). Doku gerektirir. (varsayılan: True) | BOOLEAN | Hayır | - |
| `model_tohumu` | Model üretimi için rastgele tohum (varsayılan: 42). | INT | Hayır | 0 ile 2.147.483.647 |
| `doku_tohumu` | Doku üretimi için rastgele tohum (varsayılan: 42). | INT | Hayır | 0 ile 2.147.483.647 |
| `doku_kalitesi` | Doku üretimi için kalite düzeyi (varsayılan: `"standard"`). `"detailed"` = HD dokular, `"extreme"` = 8K Ultra dokular. | COMBO | Hayır | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `doku_hizalama` | Dokuları modele hizalamak için kullanılan yöntem (varsayılan: `"original_image"`). | COMBO | Hayır | `"original_image"`<br>`"geometry"` |
| `yüz_sınırı` | Maksimum yüz sayısı. -1, Tripo'nun uyarlamalı seçim yapmasını sağlar (v3.x standardında yaklaşık 1,4M yüz, `detailed` seçeneğinde 2M). Tripo sessizce sınırlar: quad ağlarda 150.000. (varsayılan: -1) | INT | Hayır | -1 ile 2.000.000 |
| `dörtgen` | Quad ağ çıktısı. Tripo, quad ağları FBX olarak teslim eder; bu nedenle sonuç FBX çıktısına gelir ve GLB çıktısı boş kalır. (varsayılan: False) | BOOLEAN | Hayır | - |
| `geometry_quality` | Geometri üretimi için kalite düzeyi (varsayılan: `"standard"`). | COMBO | Hayır | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Temiz, el yapımı tarzda topolojiye sahip düşük poligonlu ağ (500-20.000 yüz, quad 500-10.000). Basit nesneler için en iyisidir; karmaşık olanlar başarısız olabilir. (varsayılan: False) | BOOLEAN | Hayır | - |
| `auto_size` | Dokulu modelleri metre cinsinden gerçek dünya boyutlarına ölçeklendirin. Tripo, boyutu modelin sahne dönüşümü olarak saklar ve model dönüştürüldüğünde, riglendiğinde veya yeniden hedeflendiğinde bunu sabitler; doku olmadan yok sayılır. (varsayılan: False) | BOOLEAN | Hayır | - |

**Not:** Ön görüntü (`image`) her zaman gereklidir ve `image_left`, `image_back` veya `image_right` görüntülerinden en az biri de sağlanmalıdır. `texture` kapatıldığında `pbr` de otomatik olarak kapanır, çünkü `pbr` doku gerektirir. `smart_low_poly` etkinleştirildiğinde ve `face_limit` -1 olarak bırakılmadığında, `face_limit` üçgen ağlar için 500 ile 20.000 arasında veya quad ağlar için 500 ile 10.000 arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Oluşturulan 3B model için dosya yolu veya tanımlayıcı (yalnızca geriye dönük uyumluluk için). | STRING |
| `model_görev_id` | Model oluşturma sürecini izlemek için görev tanımlayıcısı. | MODEL_TASK_ID |
| GLB | Oluşturulan 3B model dosyası GLB biçiminde. `quad` etkinleştirildiğinde boş olur. | FILE3DGLB |
| FBX | Oluşturulan 3B model dosyası FBX biçiminde. Yalnızca `quad` etkinleştirildiğinde doldurulur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `b66df4cad6167fa27edf1fe21b96cb47af90027b3fbe0a3c9c14101506281ed7`
