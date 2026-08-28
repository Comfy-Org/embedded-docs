# Tripo: Doku modeli

TripoTextureNode, Tripo API kullanarak dokulu 3D modeller üretir. Bir model görev kimliği alır ve PBR malzemeleri, doku kalitesi ayarları ve hizalama yöntemleri dahil çeşitli seçeneklerle doku üretimi uygular. Düğüm, doku üretim isteğini işlemek için Tripo API ile iletişim kurar ve sonuçta ortaya çıkan model dosyasını ve görev kimliğini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_görev_id` | Doku uygulanacak modelin görev kimliği | MODEL_TASK_ID | Evet | - |
| `doku` | Doku üretilip üretilmeyeceği (varsayılan: True) | BOOLEAN | Hayır | - |
| `pbr` | PBR (Fiziksel Tabanlı İşleme) malzemelerinin üretilip üretilmeyeceği (varsayılan: True) | BOOLEAN | Hayır | - |
| `doku_tohumu` | Doku üretimi için rastgele tohum (varsayılan: 42) | INT | Hayır | - |
| `doku_kalitesi` | Doku üretimi için kalite seviyesi (varsayılan: "standard"). "detailed" seçeneği 0,20 USD, "standard" seçeneği ise 0,10 USD tutarındadır. | COMBO | Hayır | "standard"<br>"detailed" |
| `doku_hizalama` | Dokuları hizalama yöntemi (varsayılan: "original_image"). "original_image" dokuları orijinal girdi görüntüsüne hizalar, "geometry" ise 3D geometriye hizalar. | COMBO | Hayır | "original_image"<br>"geometry" |
| `texture_prompt` | Doku oluşturma için isteğe bağlı metin yönlendirmesi. Pratikte, renk çıkarımı yapılacak kaynak görüntü taşımayan içe aktarılmış modeller (Tripo: Modeli İçe Aktar) için gereklidir. (varsayılan: "") | STRING | Hayır | - |

*Not: Bu düğüm, sistem tarafından otomatik olarak yönetilen kimlik doğrulama belirteçleri ve API anahtarları gerektirir.*

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Uygulanan dokularla oluşturulan model dosyası (yalnızca geriye dönük uyumluluk için) | STRING |
| `model_görev_id` | Doku üretim sürecini izlemek için görev kimliği | MODEL_TASK_ID |
| `GLB` | Uygulanan dokularla GLB formatında oluşturulan 3D model | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/tr.md)

---
**Source fingerprint (SHA-256):** `a0157b7fa2bb94d174ea5893d7389885180876794032a510642586e310ba30d4`
