# Tripo P1: Metinden Modele

Tripo P1 metinden 3B'ye. Bu düğüm, Tripo P1 API'sini kullanarak bir metin açıklamasından 3B model oluşturur. Kararlı topolojiye sahip düşük poligonlu, oyun için hazır mesh'ler oluşturmak üzere optimize edilmiştir ve bu da onu gerçek zamanlı uygulamalar için uygun hale getirir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `çıktı_modu` | Oluşturulan modelin yalnızca geometri mi yoksa renk/PBR dokularını da mı içereceğini kontrol eder. `"Geometry only"` doku içermeyen bir mesh döndürür. `"Textured"` renk/PBR haritaları ekler ve aşağıdaki doku seçeneklerini gösterir. | DYNAMIC_COMBO | Evet | `"Geometry only"`<br>`"Textured"` |
| `istem` | Oluşturmak istediğiniz 3B modelin metin açıklaması. En fazla 1024 karakter. Gereklidir ve boş olamaz. | STRING | Evet | Up to 1024 characters |
| `negatif_istem` | Oluşturulan modelde istemediğiniz şeylerin metin açıklaması. En fazla 255 karakter. Varsayılan: ayarlanmamış. | STRING | Hayır | Up to 255 characters |
| `görüntü_tohumu` | Rastgeleliği kontrol etmek için kullanılan bir tohum değeri. Varsayılan: 42. | INT | Hayır | 0 ile 2147483647 |
| `yüz_sınırı` | Hedef yüz sayısı, 48-20000. -1, Tripo'nun uyarlamalı olarak seçmesini sağlar. Varsayılan: -1. | INT | Hayır | -1 ile 20000 |
| `model_tohumu` | Rastgeleliği kontrol etmek için kullanılan bir tohum değeri. Varsayılan: 42. | INT | Hayır | 0 ile 2147483647 |
| `otomatik_boyut` | Çıktıyı gerçek dünya metrelerine yaklaşık olacak şekilde ölçeklendirir. Varsayılan: False. | BOOLEAN | Hayır | True / False |
| `uv_dışa_aktar` | Oluşturma sırasında UV açılımı yapar. Daha hızlı yalnızca geometri çalışmaları için kapatın. Varsayılan: True. | BOOLEAN | Hayır | True / False |
| `geometriyi_sıkıştır` | meshopt geometri sıkıştırması uygular (EXT_meshopt_compression). Daha küçük dosyalar, ancak ComfyUI'nin 3B önizlemesi bunları görüntüleyemez; düzenlemeden önce sıkıştırmayı açın. Varsayılan: False. | BOOLEAN | Hayır | True / False |

### Yalnızca Geometri Girdileri

`output_mode` `"Geometry only"` olarak ayarlandığında kullanılabilir ek girdi yoktur. Bu modda dokuyla ilgili parametreler Tripo'ya gönderilmez.

### Dokulu Girdiler

Bu girdiler yalnızca `output_mode` `"Textured"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `pbr` | PBR haritalarını içerir. Açık olduğunda temel doku da zorunlu olarak açılır. Varsayılan: True. | BOOLEAN | Evet | True / False |
| `texture_quality` | Doku kalitesi ön ayarı. detailed = HD dokular, extreme = 8K Ultra dokular. Varsayılan: "standard". | COMBO | Evet | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_seed` | Doku oluşturma için bir tohum değeri; rastgeleliği kontrol etmek için kullanılır. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Oluşturulan model dosyası adı; yalnızca geriye dönük uyumluluk için tutulur. | STRING |
| `model task_id` | Model oluşturma isteği için benzersiz görev kimliği. | MODEL_TASK_ID |
| `GLB` | GLB biçiminde oluşturulan 3B model. | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `53a5573384294612b912558436e82f3481717d2ba3d50b73f1e40c3065aff2a0`
