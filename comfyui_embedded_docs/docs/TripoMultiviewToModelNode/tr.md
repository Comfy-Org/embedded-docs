> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/tr.md)

Bu düğüm, bir nesnenin farklı görünümlerini gösteren en fazla dört görüntüyü işleyerek Tripo'nun API'sini kullanarak 3B modelleri senkronize bir şekilde oluşturur. Doku ve malzeme seçenekleriyle eksiksiz bir 3B model oluşturmak için bir ön görüntü ve en az bir ek görünüm (sol, arka veya sağ) gerektirir.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Nesnenin ön görünüm görüntüsü (gerekli) |
| `image_left` | IMAGE | Hayır | - | Nesnenin sol görünüm görüntüsü |
| `image_back` | IMAGE | Hayır | - | Nesnenin arka görünüm görüntüsü |
| `image_right` | IMAGE | Hayır | - | Nesnenin sağ görünüm görüntüsü |
| `model_version` | COMBO | Hayır | Birden fazla seçenek mevcut | Oluşturma için kullanılacak Tripo model versiyonu |
| `orientation` | COMBO | Hayır | Birden fazla seçenek mevcut | 3B model için yönlendirme ayarı |
| `texture` | BOOLEAN | Hayır | - | Model için doku oluşturulup oluşturulmayacağı (varsayılan: True) |
| `pbr` | BOOLEAN | Hayır | - | PBR (Fiziksel Tabanlı Render) malzemeleri oluşturulup oluşturulmayacağı (varsayılan: True) |
| `model_seed` | INT | Hayır | - | Model oluşturma için rastgele tohum değeri (varsayılan: 42) |
| `texture_seed` | INT | Hayır | - | Doku oluşturma için rastgele tohum değeri (varsayılan: 42) |
| `texture_quality` | COMBO | Hayır | "standard"<br>"detailed" | Doku oluşturma için kalite seviyesi (varsayılan: "standard") |
| `texture_alignment` | COMBO | Hayır | "original_image"<br>"geometry" | Dokuları modele hizalamak için kullanılan yöntem (varsayılan: "original_image") |
| `face_limit` | INT | Hayır | -1 - 500000 | Oluşturulan modeldeki maksimum yüz sayısı, -1 sınırsız anlamına gelir (varsayılan: -1) |
| `quad` | BOOLEAN | Hayır | - | Üçgenler yerine dörtgen tabanlı geometri oluşturulup oluşturulmayacağı (varsayılan: False) |

**Not:** Ön görüntü (`image`) her zaman gereklidir. Çoklu görünüm işleme için en az bir ek görünüm görüntüsü (`image_left`, `image_back` veya `image_right`) sağlanmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_file` | STRING | Oluşturulan 3B model için dosya yolu veya tanımlayıcı |
| `model task_id` | MODEL_TASK_ID | Model oluşturma sürecini takip etmek için görev tanımlayıcısı |