# Tripo: Doku modeli

TripoTextureNode, Tripo API'sini kullanarak dokulu 3D modeller oluşturur. Bir model görev kimliği alır ve PBR malzemeleri, doku kalite ayarları ve hizalama yöntemleri gibi çeşitli seçeneklerle doku oluşturma işlemini uygular. Düğüm, doku oluşturma isteğini işlemek için Tripo API'si ile iletişim kurar ve sonuçta ortaya çıkan model dosyası ile görev kimliğini döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model_görev_id` | Doku uygulanacak modelin görev kimliği | MODEL_TASK_ID | Evet | - |
| `doku` | Doku oluşturulup oluşturulmayacağı (varsayılan: True) | BOOLEAN | Hayır | - |
| `pbr` | PBR (Fiziksel Tabanlı İşleme) malzemelerinin oluşturulup oluşturulmayacağı (varsayılan: True) | BOOLEAN | Hayır | - |
| `doku_tohumu` | Doku oluşturma için rastgele tohum değeri (varsayılan: 42) | INT | Hayır | - |
| `doku_kalitesi` | Doku oluşturma için kalite seviyesi (varsayılan: "standard"). "detailed" seçeneğinin maliyeti 0,20 USD, "standard" seçeneğinin maliyeti ise 0,10 USD'dir. | COMBO | Hayır | "standard"<br>"detailed" |
| `doku_hizalama` | Dokuları hizalama yöntemi (varsayılan: "original_image"). "original_image" dokuları orijinal giriş görüntüsüne hizalarken, "geometry" onları 3D geometriye hizalar. | COMBO | Hayır | "original_image"<br>"geometry" |

*Not: Bu düğüm, sistem tarafından otomatik olarak yönetilen kimlik doğrulama belirteçleri ve API anahtarları gerektirir.*

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model_görev_id` | Uygulanan dokularla oluşturulan model dosyası (yalnızca geriye dönük uyumluluk için) | STRING |
| `GLB` | Doku oluşturma sürecini izlemek için görev kimliği | MODEL_TASK_ID |
| `GLB` | Uygulanan dokularla GLB formatında oluşturulan 3D model | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/tr.md)

---
**Source fingerprint (SHA-256):** `6d2a6ff7bbbe9fa91f63c6c7d237799044d2f9aa5afe7b90b99cf9e5a21afc32`
