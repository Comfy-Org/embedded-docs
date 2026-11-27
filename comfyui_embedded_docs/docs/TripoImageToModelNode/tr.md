# Tripo: Görüntüden Modele

Tripo API'sini kullanarak tek bir görsele dayalı olarak 3B modelleri eşzamanlı biçimde oluşturur. Bir giriş görseli sağlayın; düğüm bundan tamamlanmış bir 3B model oluşturur; model sürümü, doku üretimi, ayrıntı düzeyi ve çıktı biçimi için isteğe bağlı kontroller sunar. Bu, görselden modele düğümünün eski sürümüdür; daha eski iş akışları için korunmuştur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | 3B modeli oluşturmak için kullanılan giriş görseli. Bir görsel sağlanmalıdır; aksi takdirde düğüm hata verir. | IMAGE | Evet | - |
| `model_sürümü` | Oluşturma için kullanılacak model sürümü. | COMBO | Hayır | `"v3.1-20260211"`<br>`"v3.0-20250812"` |
| `stil` | Tripo tarafından artık desteklenmiyor ve yok sayılıyor. Daha eski iş akışları için korunmuştur. (varsayılan: `"None"`) | COMBO | Hayır | `"None"`<br>`"realistic"`<br>`"cartoon"`<br>`"sculpture"`<br>`"low_poly"` |
| `doku` | Doku haritaları oluşturur. Kapalı olduğunda yalın geometri döndürür ve `pbr` yok sayılır. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `pbr` | PBR malzeme haritaları (temel renk, metalik, pürüzlülük, normal). `texture` gerektirir. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `model_tohumu` | Model oluşturma için rastgele tohum. (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 |
| `yönlendirme` | Oluşturulan model için yönlendirme ayarı. (varsayılan: `"default"`) | COMBO | Hayır | `"default"`<br>`"front"`<br>`"back"`<br>`"left"`<br>`"right"`<br>`"top"`<br>`"bottom"` |
| `doku_tohumu` | Doku oluşturma için rastgele tohum. (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 |
| `doku_kalitesi` | Doku oluşturma için kalite düzeyi: `detailed` = HD dokular, `extreme` = 8K Ultra dokular. (varsayılan: `"standard"`) | COMBO | Hayır | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `doku_hizalama` | Doku eşleme için hizalama yöntemi. (varsayılan: `"original_image"`) | COMBO | Hayır | `"original_image"`<br>`"geometry"` |
| `yüz_sınırı` | Maksimum yüz sayısı. -1, Tripo'nun uyarlamalı seçim yapmasını sağlar (v3.x standardında yaklaşık 1,4 milyon yüz, ayrıntılıda 2 milyon). Tripo sessizce sınırlar: quad ağlarda 150.000. (varsayılan: -1) | INT | Hayır | -1 ile 2000000 |
| `dörtlü` | Quad ağ çıktısı. Tripo quad ağları FBX olarak teslim eder; bu nedenle sonuç FBX çıktısına gelir ve GLB çıktısı boş kalır. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `geometry_quality` | Geometri oluşturma için kalite düzeyi. (varsayılan: `"standard"`) | COMBO | Hayır | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Temiz, el yapımı tarzda topolojiye sahip düşük poligonlu ağ (500-20.000 yüz, quad 500-10.000). Basit nesneler için en uygunudur; karmaşık olanlar başarısız olabilir. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `auto_size` | Dokulu modelleri metre cinsinden gerçek dünya boyutlarına ölçekler. Tripo boyutu modelin sahne dönüşümü olarak saklar ve model dönüştürüldüğünde, riglendiğinde veya yeniden hedeflendiğinde bunu içine işler; doku olmadan yok sayılır. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |

Not: Bir `image` gereklidir; eksikse düğüm bir RuntimeError fırlatır. `texture` False olduğunda model yalnızca yalın geometri içerir ve `pbr` False olmaya zorlanır. `smart_low_poly` etkinleştirildiğinde, `face_limit` üçgen ağlar için 500 ile 20.000 arasında olmalıdır veya `quad` da etkinleştirildiğinde 500 ile 10.000 arasında olmalıdır; sınır geçersizse düğüm bir ValueError fırlatır. `face_limit` -1 (varsayılan) olarak ayarlandığında API'ye açık bir yüz sınırı gönderilmez ve Tripo'nun uyarlamalı seçim yapmasına izin verilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Oluşturulan 3B model dosyası (yalnızca geriye dönük uyumluluk için). | STRING |
| `model_görev_id` | Model oluşturma sürecini izlemek için görev kimliği. | MODEL_TASK_ID |
| `GLB` | GLB biçiminde oluşturulan 3B model. `quad` etkinleştirildiğinde boştur. | FILE3DGLB |
| `FBX` | FBX biçiminde oluşturulan 3B model. Yalnızca `quad` etkinleştirildiğinde doldurulur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `3b278abfd13329ee58ebab1bfeb47d32d09f4797f3d8628a35a028c3d15a7314`
