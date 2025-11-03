> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/tr.md)

Tek bir görüntüye dayalı olarak Tripo'nun API'sini kullanarak 3B modelleri eşzamanlı olarak oluşturur. Bu düğüm, bir girdi görüntüsü alır ve onu doku, kalite ve model özellikleri için çeşitli özelleştirme seçenekleriyle bir 3B modele dönüştürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | 3B model oluşturmak için kullanılan girdi görüntüsü |
| `model_version` | COMBO | Hayır | Birden fazla seçenek mevcut | Oluşturma için kullanılacak Tripo modelinin sürümü |
| `style` | COMBO | Hayır | Birden fazla seçenek mevcut | Oluşturulan model için stil ayarı (varsayılan: "None") |
| `texture` | BOOLEAN | Hayır | - | Model için doku oluşturulup oluşturulmayacağı (varsayılan: True) |
| `pbr` | BOOLEAN | Hayır | - | Fiziksel Tabanlı Renderlama kullanılıp kullanılmayacağı (varsayılan: True) |
| `model_seed` | INT | Hayır | - | Model oluşturma için rastgele tohum değeri (varsayılan: 42) |
| `orientation` | COMBO | Hayır | Birden fazla seçenek mevcut | Oluşturulan model için yönlendirme ayarı |
| `texture_seed` | INT | Hayır | - | Doku oluşturma için rastgele tohum değeri (varsayılan: 42) |
| `texture_quality` | COMBO | Hayır | "standard"<br>"detailed" | Doku oluşturma için kalite seviyesi (varsayılan: "standard") |
| `texture_alignment` | COMBO | Hayır | "original_image"<br>"geometry" | Doku eşleme için hizalama yöntemi (varsayılan: "original_image") |
| `face_limit` | INT | Hayır | -1 - 500000 | Oluşturulan modeldeki maksimum yüz sayısı, -1 sınırsız anlamına gelir (varsayılan: -1) |
| `quad` | BOOLEAN | Hayır | - | Üçgenler yerine dörtgen yüzler kullanılıp kullanılmayacağı (varsayılan: False) |

**Not:** `image` parametresi gereklidir ve düğümün çalışması için sağlanmalıdır. Eğer bir görüntü sağlanmazsa, düğüm bir RuntimeError hatası verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_file` | STRING | Oluşturulan 3B model dosyası |
| `model task_id` | MODEL_TASK_ID | Model oluşturma sürecini takip etmek için görev kimliği |