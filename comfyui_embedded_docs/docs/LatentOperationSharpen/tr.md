# GizliİşlemKeskinleştirme

LatentOperationSharpen düğümü, bir Gauss çekirdeği kullanarak gizli temsillere keskinleştirme efekti uygular. Gizli verileri normalleştirerek, özel bir keskinleştirme çekirdeği ile evrişim uygulayarak ve ardından orijinal parlaklığı geri yükleyerek çalışır. Bu, gizli uzay temsilindeki ayrıntıları ve kenarları iyileştirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `keskinleştirme_yarıçapı` | Keskinleştirme çekirdeğinin yarıçapı (varsayılan: 9) | INT | Hayır | 1-31 |
| `sigma` | Gauss çekirdeği için standart sapma (varsayılan: 1.0) | FLOAT | Hayır | 0.1-10.0 |
| `alfa` | Keskinleştirme yoğunluk faktörü (varsayılan: 0.1) | FLOAT | Hayır | 0.0-5.0 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `operation` | Gizli verilere uygulanabilecek bir keskinleştirme işlemi döndürür | LATENT_OPERATION |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/tr.md)

---
**Source fingerprint (SHA-256):** `542754746ab462eb27229ab9b949bb66054ab4c87c77cc59d405b35a2cc27bce`
