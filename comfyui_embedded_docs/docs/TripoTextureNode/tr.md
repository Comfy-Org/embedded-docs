> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/tr.md)

TripoTextureNode, Tripo API'sini kullanarak dokulu 3B modeller oluşturur. Bir model görev kimliği alır ve PBR malzemeleri, doku kalitesi ayarları ve hizalama yöntemleri dahil olmak üzere çeşitli seçeneklerle doku oluşturmayı uygular. Düğüm, doku oluşturma isteğini işlemek için Tripo API'si ile iletişim kurar ve ortaya çıkan model dosyasını ve görev kimliğini döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | Evet | - | Dokuların uygulanacağı modelin görev kimliği |
| `texture` | BOOLEAN | Hayır | - | Dokuların oluşturulup oluşturulmayacağı (varsayılan: True) |
| `pbr` | BOOLEAN | Hayır | - | PBR (Fiziksel Tabanlı Render) malzemelerinin oluşturulup oluşturulmayacağı (varsayılan: True) |
| `texture_seed` | INT | Hayır | - | Doku oluşturma için rastgele tohum değeri (varsayılan: 42) |
| `texture_quality` | COMBO | Hayır | "standard"<br>"detailed" | Doku oluşturma için kalite seviyesi (varsayılan: "standard") |
| `texture_alignment` | COMBO | Hayır | "original_image"<br>"geometry" | Dokuları hizalamak için kullanılan yöntem (varsayılan: "original_image") |

*Not: Bu düğüm, sistem tarafından otomatik olarak yönetilen kimlik doğrulama token'ları ve API anahtarları gerektirir.*

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_file` | STRING | Uygulanan dokulara sahip oluşturulan model dosyası |
| `model task_id` | MODEL_TASK_ID | Doku oluşturma sürecini takip etmek için görev kimliği |