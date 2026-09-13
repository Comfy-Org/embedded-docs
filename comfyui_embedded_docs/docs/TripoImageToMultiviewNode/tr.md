# Tripo: Görüntüden Çoklu Görünüme

Tripo API kullanarak tek bir girdi görselinden öznenin ön, sol, arka ve sağ görünümlerini oluşturur. Görsel yüklenir, bir çoklu görünüm oluşturma görevi başlatılır ve tamamlanana kadar sorgulanır; elde edilen dört görünüm görev kimliğiyle birlikte döndürülür. Bu, yaklaşık 0,10 USD olarak faturalandırılan ücretli bir görevdir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Tripo'nun ön, sol, arka ve sağ görünümlerini oluşturduğu öznenin kaynak görseli. Bir toplu iş sağlansa bile istek için yalnızca bir görsel kullanılır. | IMAGE | Evet | Tek görsel |

Not: Düğüm, Tripo'nun bulut API'sini çağırır ve oluşturma görevinin tamamlanmasını bekler. Tipik bir görev yaklaşık 25 saniye sürer. Kimlik doğrulama, düğümün gizli girdileri aracılığıyla otomatik olarak yönetilir; bu nedenle iş akışında herhangi bir Tripo API anahtarı sağlanması gerekmez. Düğüm, Tripo yanıtındaki dört görünüm URL'sinin tamamını (`front_view_url`, `left_view_url`, `back_view_url`, `right_view_url`) gerektirir; herhangi bir görünüm eksikse yürütme bir hatayla başarısız olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `multiview task_id` | Tripo tarafından çoklu görünüm görsel oluşturma isteği için döndürülen görev tanımlayıcısı. Tamamlanan göreve başvurmak için kullanılabilir; örneğin görünümleri Tripo: Edit Multiview ile iyileştirirken. | MULTIVIEW_TASK_ID |
| `front` | Öznenin oluşturulan ön görünümü. | IMAGE |
| `left` | Öznenin oluşturulan sol yan görünümü. | IMAGE |
| `back` | Öznenin oluşturulan arka görünümü. | IMAGE |
| `right` | Öznenin oluşturulan sağ yan görünümü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/tr.md)

---
**Source fingerprint (SHA-256):** `7e96d327940f1f09a3e84031c773c1439380f20afae49c79fd4350fcf0aba5da`
