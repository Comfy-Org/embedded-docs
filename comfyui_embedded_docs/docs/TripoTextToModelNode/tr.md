> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/tr.md)

Metin açıklamasına dayanarak Tripo'nun API'sini kullanarak 3B modelleri eşzamanlı olarak oluşturur. Bu düğüm, bir metin açıklaması alır ve isteğe bağlı doku ve malzeme özelliklerine sahip bir 3B model oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | 3B model oluşturmak için metin açıklaması (çok satırlı giriş) |
| `negative_prompt` | STRING | Hayır | - | Oluşturulan modelde nelerden kaçınılacağının metin açıklaması (çok satırlı giriş) |
| `model_version` | COMBO | Hayır | Birden fazla seçenek mevcut | Oluşturma için kullanılacak Tripo modelinin sürümü |
| `style` | COMBO | Hayır | Birden fazla seçenek mevcut | Oluşturulan model için stil ayarı (varsayılan: "None") |
| `texture` | BOOLEAN | Hayır | - | Model için doku oluşturulup oluşturulmayacağı (varsayılan: True) |
| `pbr` | BOOLEAN | Hayır | - | PBR (Fiziksel Tabanlı Render) malzemelerinin oluşturulup oluşturulmayacağı (varsayılan: True) |
| `image_seed` | INT | Hayır | - | Görüntü oluşturma için rastgele tohum (varsayılan: 42) |
| `model_seed` | INT | Hayır | - | Model oluşturma için rastgele tohum (varsayılan: 42) |
| `texture_seed` | INT | Hayır | - | Doku oluşturma için rastgele tohum (varsayılan: 42) |
| `texture_quality` | COMBO | Hayır | "standard"<br>"detailed" | Doku oluşturma için kalite seviyesi (varsayılan: "standard") |
| `face_limit` | INT | Hayır | -1 - 500000 | Oluşturulan modeldeki maksimum yüz sayısı, sınırsız için -1 (varsayılan: -1) |
| `quad` | BOOLEAN | Hayır | - | Üçgenler yerine dörtgen tabanlı geometri oluşturulup oluşturulmayacağı (varsayılan: False) |

**Not:** `prompt` parametresi zorunludur ve boş olamaz. Eğer bir prompt sağlanmazsa, düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_file` | STRING | Oluşturulan 3B model dosyası |
| `model task_id` | MODEL_TASK_ID | Model oluşturma süreci için benzersiz görev tanımlayıcısı |