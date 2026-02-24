> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](<https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon> Scaling/tr.md)

Bu düğüm, "Difüzyon Modellerinde Maruz Kalma Yanlılığını Açıklama" araştırma makalesinden Epsilon Ölçeklendirme yöntemini uygular. Örnekleme sürecinde tahmin edilen gürültüyü ölçeklendirerek, oluşturulan görüntülerde kaliteyi artırmaya yardımcı olabilecek maruz kalma yanlılığını azaltmaya çalışır. Bu uygulama, makale tarafından önerilen "tekdüze programı" kullanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Epsilon ölçeklendirme yamasının uygulanacağı model. |
| `scaling_factor` | FLOAT | Hayır | 0.5 - 1.5 | Tahmin edilen gürültünün ölçeklendirileceği faktör. 1.0'dan büyük bir değer gürültüyü azaltırken, 1.0'dan küçük bir değer artırır (varsayılan: 1.005). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Örnekleme sürecine epsilon ölçeklendirme işlevi uygulanmış, girdi modelinin yamalı versiyonu. |
