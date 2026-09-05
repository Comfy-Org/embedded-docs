# TripoImageToMultiviewNode

Tripo API'sini kullanarak, tek bir girdi görüntüsünden nesnenin ön, sol, arka ve sağ görünümlerini üretir. Bu, yaklaşık 0,10 USD olarak faturalandırılan ücretli bir görevdir. Düğüm, görüntüyü yükler, Tripo oluşturma görevinin bitmesini bekler ve ardından dört görünümü çoklu görünüm görev kimliğiyle birlikte döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Nesnenin Tripo'nun ön, sol, arka ve sağ görünümlerini oluşturduğu kaynak görüntü. İstek için tam olarak bir görüntü kullanılır. | IMAGE | Evet | Tek görüntü |

Not: Düğüm, Tripo'nun bulut API'sini çağırır ve oluşturma görevinin bitmesini bekler. Tipik bir görev yaklaşık 25 saniye sürer. Kimlik doğrulama, düğümün gizli girdileri aracılığıyla otomatik olarak işlenir; bu nedenle iş akışında Tripo API anahtarı sağlanmasına gerek yoktur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `multiview task_id` | Tripo tarafından çoklu görünüm görüntü oluşturma isteği için döndürülen görev tanımlayıcısı. Tamamlanan göreve başvurmak için kullanılabilen bir dize tanımlayıcıdır. | MULTIVIEW_TASK_ID |
| `ön` | Nesnenin oluşturulan ön görünümü. | IMAGE |
| `sol` | Nesnenin oluşturulan sol taraf görünümü. | IMAGE |
| `arka` | Nesnenin oluşturulan arka görünümü. | IMAGE |
| `sağ` | Nesnenin oluşturulan sağ taraf görünümü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/tr.md)

---
**Source fingerprint (SHA-256):** `3beca1feeb88aa080330e6867ffd7076bd45b2c52471d1bfacc71f66452211a5`
