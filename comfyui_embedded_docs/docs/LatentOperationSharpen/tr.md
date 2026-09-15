# GizliİşlemKeskinleştirme

LatentOperationSharpen düğümü, Gauss tabanlı bir çekirdek kullanarak latent temsiller için bir keskinleştirme işlemi oluşturur. Latent verileri normalleştirir, evrişim yoluyla özel bir keskinleştirme çekirdeği uygular ve ardından özgün parlaklığı geri yükler; bu, latent uzay temsilindeki ayrıntıları ve kenarları iyileştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `keskinleştirme_yarıçapı` | Keskinleştirme çekirdeğinin yarıçapı; keskinleştirme için kullanılan alanın boyutunu kontrol eder (varsayılan: 9) | INT | Evet | 1-31 |
| `sigma` | Keskinleştirme çekirdeğini oluşturmak için kullanılan Gauss çekirdeğinin standart sapması (varsayılan: 1.0) | FLOAT | Evet | 0.1-10.0 |
| `alfa` | Keskinleştirme yoğunluk faktörü; daha yüksek değerler daha güçlü bir keskinleştirme etkisi üretir (varsayılan: 0.1) | FLOAT | Evet | 0.0-5.0 |

Üç girdinin tümü gelişmiş parametrelerdir ve varsayılan değerlere sahiptir; bu nedenle düğüm, bunlar değiştirilmeden kullanılabilir. Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `operation` | Latent verilere uygulanabilecek bir keskinleştirme işlemi döndürür | LATENT_OPERATION |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/tr.md)

---
**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`
