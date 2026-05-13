> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/tr.md)

TripoTextureNode, Tripo API'sini kullanarak dokulu 3D modeller oluşturur. Bir model görev kimliği alır ve PBR malzemeleri, doku kalite ayarları ve hizalama yöntemleri gibi çeşitli seçeneklerle doku oluşturma işlemini uygular. Düğüm, doku oluşturma isteğini işlemek için Tripo API'si ile iletişim kurar ve sonuçta ortaya çıkan model dosyası ile görev kimliğini döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_görev_id` | MODEL_TASK_ID | Evet | - | Doku uygulanacak modelin görev kimliği |
| `doku` | BOOLEAN | Hayır | - | Doku oluşturulup oluşturulmayacağı (varsayılan: True) |
| `pbr` | BOOLEAN | Hayır | - | PBR (Fiziksel Tabanlı İşleme) malzemelerinin oluşturulup oluşturulmayacağı (varsayılan: True) |
| `doku_tohumu` | INT | Hayır | - | Doku oluşturma için rastgele tohum değeri (varsayılan: 42) |
| `doku_kalitesi` | COMBO | Hayır | "standard"<br>"detailed" | Doku oluşturma için kalite seviyesi (varsayılan: "standard"). "detailed" seçeneğinin maliyeti 0,20 USD, "standard" seçeneğinin maliyeti ise 0,10 USD'dir. |
| `doku_hizalama` | COMBO | Hayır | "original_image"<br>"geometry" | Dokuları hizalama yöntemi (varsayılan: "original_image"). "original_image" dokuları orijinal giriş görüntüsüne hizalarken, "geometry" onları 3D geometriye hizalar. |

*Not: Bu düğüm, sistem tarafından otomatik olarak yönetilen kimlik doğrulama belirteçleri ve API anahtarları gerektirir.*

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_görev_id` | STRING | Uygulanan dokularla oluşturulan model dosyası (yalnızca geriye dönük uyumluluk için) |
| `GLB` | MODEL_TASK_ID | Doku oluşturma sürecini izlemek için görev kimliği |
| `GLB` | FILE3DGLB | Uygulanan dokularla GLB formatında oluşturulan 3D model |

---
**Source fingerprint (SHA-256):** `6d2a6ff7bbbe9fa91f63c6c7d237799044d2f9aa5afe7b90b99cf9e5a21afc32`
