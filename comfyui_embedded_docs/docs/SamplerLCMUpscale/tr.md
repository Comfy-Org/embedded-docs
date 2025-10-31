> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/tr.md)

SamplerLCMUpscale düğümü, Gizli Tutarlılık Modeli (LCM) örneklemesini görüntü büyütme yetenekleriyle birleştiren özelleştirilmiş bir örnekleme yöntemi sağlar. Görüntü kalitesini korurken daha yüksek çözünürlüklü çıktılar oluşturmak için kullanışlı olan, çeşitli enterpolasyon yöntemleri kullanarak örnekleme işlemi sırasında görüntüleri büyütmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ölçek_oranı` | FLOAT | Hayır | 0.1 - 20.0 | Büyütme sırasında uygulanacak ölçeklendirme faktörü (varsayılan: 1.0) |
| `ölçek_adımları` | INT | Hayır | -1 - 1000 | Büyütme işlemi için kullanılacak adım sayısı. Otomatik hesaplama için -1 kullanın (varsayılan: -1) |
| `büyütme_yöntemi` | COMBO | Evet | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" | Görüntüyü büyütmek için kullanılan enterpolasyon yöntemi |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Örnekleme işlem hattında kullanılabilecek yapılandırılmış bir örnekleyici nesnesi döndürür |