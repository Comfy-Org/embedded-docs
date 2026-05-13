> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/tr.md)

LatentOperationSharpen düğümü, bir Gauss çekirdeği kullanarak gizli temsillere keskinleştirme efekti uygular. Gizli verileri normalleştirerek, özel bir keskinleştirme çekirdeği ile evrişim uygulayarak ve ardından orijinal parlaklığı geri yükleyerek çalışır. Bu, gizli uzay temsilindeki ayrıntıları ve kenarları iyileştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `keskinleştirme_yarıçapı` | INT | Hayır | 1-31 | Keskinleştirme çekirdeğinin yarıçapı (varsayılan: 9) |
| `sigma` | FLOAT | Hayır | 0.1-10.0 | Gauss çekirdeği için standart sapma (varsayılan: 1.0) |
| `alfa` | FLOAT | Hayır | 0.0-5.0 | Keskinleştirme yoğunluk faktörü (varsayılan: 0.1) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `operation` | LATENT_OPERATION | Gizli verilere uygulanabilecek bir keskinleştirme işlemi döndürür |

---
**Source fingerprint (SHA-256):** `542754746ab462eb27229ab9b949bb66054ab4c87c77cc59d405b35a2cc27bce`
