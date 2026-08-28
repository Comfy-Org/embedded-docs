# GizliİşlemKeskinleştirme

LatentOperationSharpen düğümü, Gaussian çekirdeği kullanarak latent temsiller için bir keskinleştirme işlemi oluşturur. Latent verileri normalleştirir, evrişim yoluyla özel bir keskinleştirme çekirdeği uygular ve ardından orijinal parlaklığı geri yükler. Bu, latent uzay temsilindeki ayrıntıları ve kenarları geliştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `keskinleştirme_yarıçapı` | Keskinleştirme çekirdeğinin yarıçapı; keskinleştirme için kullanılan alanın boyutunu kontrol eder (varsayılan: 9) | INT | Evet | 1-31 |
| `sigma` | Keskinleştirme çekirdeğini oluşturmak için kullanılan Gaussian çekirdeğinin standart sapması (varsayılan: 1.0) | FLOAT | Evet | 0.1-10.0 |
| `alfa` | Keskinleştirme yoğunluk faktörü; daha yüksek değerler daha güçlü bir keskinleştirme etkisi üretir (varsayılan: 0.1) | FLOAT | Evet | 0.0-5.0 |

Her üç girdi de gelişmiş parametrelerdir ve varsayılan değerlere sahiptir; bu nedenle düğüm, bu değerleri değiştirmeden kullanılabilir. Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `operation` | Latent verilere uygulanabilen bir keskinleştirme işlemi döndürür | LATENT_OPERATION |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/tr.md)

---
**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`
