# Tripo: Metinden Modele

Bu eski düğüm, Tripo API'si kullanarak bir metin açıklamasından tamamlanmış 3D modeller üretir. Oluşturmanın tamamlanmasını bekler ve ardından model dosyasını, isteğe bağlı olarak dokular ve PBR malzemeleriyle birlikte döndürür. Kullanımdan kaldırılmış olarak işaretlenmiştir ve eski iş akışları için korunmuştur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istek` | Oluşturulacak 3D modelin metin açıklaması (çok satırlı). Bu parametre gereklidir ve boş olamaz. | STRING | Evet | - |
| `olumsuz_istek` | Oluşturulan modelde kaçınılması gerekenlerin metin açıklaması (çok satırlı). En fazla 255 karakter. API'ye yalnızca boş olmadığında gönderilir. | STRING | Hayır | En fazla 255 karakter |
| `model_versiyonu` | Oluşturma için kullanılacak Tripo modelinin sürümü (varsayılan: v3_1_20260211). | COMBO | Hayır | Birden çok seçenek mevcut |
| `stil` | Artık Tripo tarafından desteklenmiyor ve yok sayılıyor. Eski iş akışları için korunmuştur (varsayılan: "None"). | COMBO | Hayır | Birden çok seçenek mevcut |
| `doku` | Doku haritaları oluşturur. Kapalıyken yalnızca geometriyi döndürür ve `pbr` yok sayılır (varsayılan: True). | BOOLEAN | Hayır | true / false |
| `pbr` | PBR malzeme haritaları (temel renk, metalik, pürüzlülük, normal). `texture` gerektirir; `texture` kapalıyken zorunlu olarak kapatılır (varsayılan: True). | BOOLEAN | Hayır | true / false |
| `görüntü_tohumu` | Görüntü oluşturma aşamasında kullanılan tohum (varsayılan: 42). | INT | Hayır | 0 - 2147483647 |
| `model_tohumu` | Model oluşturma aşamasında kullanılan tohum (varsayılan: 42). | INT | Hayır | 0 - 2147483647 |
| `doku_tohumu` | Doku oluşturma aşamasında kullanılan tohum (varsayılan: 42). | INT | Hayır | 0 - 2147483647 |
| `doku_kalitesi` | Oluşturulan dokuların kalitesi. detailed = HD dokular, extreme = 8K Ultra dokular (varsayılan: standard). | COMBO | Hayır | "standard"<br>"detailed"<br>"extreme" |
| `yüz_sınırı` | Maksimum yüz sayısı. -1, Tripo'nun uyarlamalı seçim yapmasını sağlar (v3.x standard için yaklaşık 1,4 milyon yüz, detailed için 2 milyon). Tripo sessizce sınırlar: quad ağlar için 150.000. (varsayılan: -1) | INT | Hayır | -1 - 2000000 |
| `dörtgen` | Quad ağ çıktısı. Tripo quad ağları FBX olarak teslim eder; bu nedenle sonuç FBX çıktısına gelir ve GLB çıktısı boş kalır. (varsayılan: False) | BOOLEAN | Hayır | true / false |
| `geometry_quality` | Oluşturulan geometrinin kalitesi (varsayılan: standard). | COMBO | Hayır | "standard"<br>"detailed" |
| `smart_low_poly` | Temiz, el yapımı tarzı topolojiye sahip düşük poligonlu ağ (500-20.000 yüz, quad 500-10.000). Basit nesneler için en iyisidir; karmaşık olanlar başarısız olabilir. (varsayılan: False) | BOOLEAN | Hayır | true / false |
| `auto_size` | Dokulu modelleri metre cinsinden gerçek dünya boyutlarına ölçekler. Tripo boyutu modelin sahne dönüşümü olarak saklar ve model dönüştürüldüğünde, riglendiğinde veya yeniden hedeflendiğinde bunu kalıcı hale getirir; doku olmadan yok sayılır. (varsayılan: True) | BOOLEAN | Hayır | true / false |

**Notlar:**
- Bu düğüm kullanımdan kaldırılmıştır ve eski düğüm olarak işaretlenmiştir. Eski iş akışlarıyla geriye dönük uyumluluk için korunmuştur.
- `prompt` parametresi zorunludur: boş bir prompt düğümün hata vermesine neden olur.
- `pbr`, `texture` gerektirir. `texture` kapalıyken düğüm `pbr` değerini zorla kapatır ve değerini yok sayar. `auto_size` da `texture` olmadan etkisizdir.
- `smart_low_poly` etkinleştirildiğinde ve `face_limit` -1 dışında bir değere ayarlandığında, yüz sınırı üçgen çıktı için 500 ile 20.000 arasında, `quad` etkinleştirildiğinde ise 500 ile 10.000 arasında olmalıdır; aksi takdirde düğüm hata verir.
- `quad` etkinleştirildiğinde, oluşturulan quad ağ FBX olarak teslim edilir; bu nedenle FBX çıktısı doldurulur ve GLB çıktısı boş kalır.
- `style` parametresi kabul edilir ancak yok sayılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Oluşturulan 3D model dosya adı `<task_id>.<format>` biçiminde; yalnızca geriye dönük uyumluluk için korunmuştur. | STRING |
| `model_görev_id` | Model oluşturma süreci için benzersiz görev tanımlayıcısı. | MODEL_TASK_ID |
| `GLB` | Oluşturulan 3D modelin GLB biçimi. `quad` etkinleştirildiğinde boştur. | FILE3DGLB |
| `FBX` | Oluşturulan 3D modelin FBX biçimi. Yalnızca `quad` etkinleştirildiğinde doldurulur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `c26c8437ea66d08f7f39865fedeaaf4cf8583ca64b368f3b767ea18918dd6c08`
