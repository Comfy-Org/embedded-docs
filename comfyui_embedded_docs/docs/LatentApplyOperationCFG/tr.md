# GizliİşlemUygulaCFG

The LatentApplyOperationCFG düğümü, bir modelin örnekleme sürecinin sınıflandırıcıdan bağımsız yönlendirme (CFG) adımında latent bir işlem uygular. CFG'den önce üretilen koşullandırma çıktılarını yakalar, bağlı işlemi latent değerlere uygular ve bu değiştirilmiş örnekleme davranışına sahip modeli döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | CFG işleminin uygulanacağı model | MODEL | Evet | - |
| `işlem` | CFG örnekleme sürecinde uygulanacak latent işlemi | LATENT_OPERATION | Evet | - |
| `start_percent` | İşlemin uygulanmaya başladığı gürültü giderme çizelgesi oranı; 0, çizelgenin başlangıcıdır (varsayılan: 0.0) | FLOAT | Hayır | 0.0 ila 1.0 (adım 0.001) |
| `end_percent` | İşlemin uygulanmayı bıraktığı gürültü giderme çizelgesi oranı; 1, çizelgenin sonudur (varsayılan: 1.0) | FLOAT | Hayır | 0.0 ila 1.0 (adım 0.001) |

Not: Bu düğüm deneysel olarak işaretlenmiştir. İşlem, CFG örnekleme sürecinde modelin koşullandırma çıktılarına uygulanır. İki koşullandırma çıktısı mevcut olduğunda, işlem birinci ve ikinci çıktı arasındaki farka uygulanır ve ikinci çıktı sonuca geri eklenir. Yalnızca bir koşullandırma çıktısı mevcut olduğunda, işlem doğrudan ona uygulanır. İşlem yalnızca gürültü giderme çizelgesinin `start_percent` ile `end_percent` noktaları arasında çalışır, bu nedenle çizelgenin bir bölümüyle sınırlandırılabilir; bu aralığın dışında koşullandırma çıktıları değiştirilmeden döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Örnekleme sürecine CFG işlemi uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/tr.md)

---
**Source fingerprint (SHA-256):** `6a5f59f02eaec38334c63d871e48e89aa983a5ac2ca10801161cdc9e13cacdf2`
