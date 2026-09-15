# SeedVR2 Girdisini Ön İşle

Bu düğüm, SeedVR2 modeli için yeniden boyutlandırılmış bir görüntüyü veya videoyu, modelin beklediği şekle dolgu uygulayarak hazırlar. Piksel değerleri 0-1 aralığına sınırlandırılır, yükseklik ve genişlik 16'nın katlarına doldurulur ve kare sayısı, 4n+1 desenine (1, 5, 9, 13, ...) uyana kadar son kare tekrarlanarak doldurulur. İşlem sırasında alfa kanalı çıkarılır; eşlik eden Post-Process SeedVR2 Output düğümü, daha sonra bunu özgün yeniden boyutlandırılmış görüntüden geri yükler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `resized_images` | İşlenecek yeniden boyutlandırılmış görüntü. | IMAGE | Evet | - |

Not: Girdi tek bir kare, bir kare dizisi veya bir video yığını (4-D veya 5-D IMAGE tensörleri) olabilir. 3'ten fazla kanala sahipse alfa kanalı çıkarılır ve yalnızca RGB tutulur. Girdinin kısa kenarı en az 2 piksel olmalıdır. Uzamsal dolgu siyahla (değer 0) doldurulur ve geçerli kare sayıları 4n+1 desenini (1, 5, 9, 13, ...) izler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `images` | VAE kodlaması için doldurulmuş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/tr.md)

---
**Source fingerprint (SHA-256):** `f4fa433d299feba40696f27ff365c59988e5102112f09536724b5db5b09416bb`
