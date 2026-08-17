# Tripo: Doku modeli

TripoTextureNode, Tripo API'yi kullanarak dokulu 3D modeller oluşturur. Bir model görev kimliği (task ID) alır ve PBR malzemeleri, doku kalitesi ayarları, hizalama yöntemleri ve isteğe bağlı metin yönlendirmesi dahil çeşitli seçeneklerle doku oluşturmayı uygular. Düğüm, doku oluşturma isteğini işlemek için Tripo API ile iletişim kurar ve elde edilen model dosyasını ve görev kimliğini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-----------|-----------|---------|--------|
| `model_task_id` | Doku uygulanacak modelin görev kimliği (task ID) | MODEL_TASK_ID | Evet | - |
| `texture` | Doku oluşturulup oluşturulmayacağı (varsayılan: True) | BOOLEAN | Hayır | - |
| `pbr` | PBR (Fiziksel Tabanlı İşleme) malzemelerinin oluşturulup oluşturulmayacağı (varsayılan: True) | BOOLEAN | Hayır | - |
| `texture_seed` | Doku oluşturma için rastgele tohum (seed) değeri (varsayılan: 42) | INT | Hayır | - |
| `texture_quality` | Doku oluşturma için kalite düzeyi (varsayılan: "standard"). "detailed" seçeneğinin maliyeti 0,20 USD, "standard" seçeneğinin maliyeti ise 0,10 USD'dir. | COMBO | Hayır | "standard"<br>"detailed" |
| `texture_alignment` | Dokuları hizalama yöntemi (varsayılan: "original_image"). "original_image" dokuları orijinal giriş görüntüsüne hizalar, "geometry" ise 3D geometriye hizalar. | COMBO | Hayır | "original_image"<br>"geometry" |
| `texture_prompt` | Doku oluşturma için isteğe bağlı metin yönlendirmesi. Renklerin çıkarılabileceği bir kaynak görüntü taşımayan içe aktarılan modeller (Tripo: Import Model) için pratikte gereklidir. (çok satırlı metin kutusu, varsayılan: boş dize) | STRING | Hayır | - |

*Not: Bu düğüm, sistem tarafından otomatik olarak yönetilen kimlik doğrulama belirteçleri ve API anahtarları gerektirir.*

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|------------|------------|------------|
| `model_file` | Uygulanan dokularla oluşturulan model dosyası (yalnızca geriye dönük uyumluluk için) | STRING |
| `model task_id` | Doku oluşturma sürecini izlemek için görev kimliği (task ID) | MODEL_TASK_ID |
| `GLB` | Uygulanan dokularla GLB formatında oluşturulan 3D model | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/tr.md)

---
**Source fingerprint (SHA-256):** `a0157b7fa2bb94d174ea5893d7389885180876794032a510642586e310ba30d4`
