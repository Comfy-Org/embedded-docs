> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/tr.md)

LatentOperationSharpen düğümü, Gauss çekirdeği kullanarak gizli temsillere keskinleştirme efekti uygular. Gizli veriyi normalleştirerek, özel bir keskinleştirme çekirdeği ile evrişim uygulayarak ve ardından orijinal parlaklığı geri yükleyerek çalışır. Bu, gizli uzay temsilindeki detayları ve kenarları geliştirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `sharpen_radius` | INT | Hayır | 1-31 | Keskinleştirme çekirdeğinin yarıçapı (varsayılan: 9) |
| `sigma` | FLOAT | Hayır | 0.1-10.0 | Gauss çekirdeği için standart sapma (varsayılan: 1.0) |
| `alpha` | FLOAT | Hayır | 0.0-5.0 | Keskinleştirme yoğunluk faktörü (varsayılan: 0.1) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `operation` | LATENT_OPERATION | Gizli veriye uygulanabilecek bir keskinleştirme işlemi döndürür |