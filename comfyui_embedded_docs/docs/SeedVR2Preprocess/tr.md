# SeedVR2 Girdisini Ön İşle

Bu düğüm, yeniden boyutlandırılmış bir görüntüyü veya videoyu SeedVR2 modeli için, modelin beklediği şekle dolgulayarak hazırlar. İşlem sırasında alfa kanalını atar; yardımcı Post-Process SeedVR2 Output düğümü, daha sonra orijinal yeniden boyutlandırılmış görüntüden onu geri yükler. Piksel değerleri 0-1 aralığına sıkıştırılır, yükseklik ve genişlik 16'nın katlarına dolgulanır ve kare sayısı, gerektiğinde son kare tekrarlanarak dolgulanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `resized_images` | İşlenecek yeniden boyutlandırılmış görüntü. | IMAGE | Evet | - |

Not: Girdi tek bir kare, bir kare dizisi veya bir video yığını olabilir. 3'ten fazla kanalı varsa, alfa kanalı atılır ve yalnızca RGB korunur. Girdinin kısa kenarı en az 2 piksel olmalıdır. Uzamsal dolgulama siyahla (değer 0) doldurulur ve geçerli kare sayıları 4n+1 düzenini izler (1, 5, 9, 13, ...).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `images` | VAE kodlama için dolgulanmış görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/tr.md)

---
**Source fingerprint (SHA-256):** `f4fa433d299feba40696f27ff365c59988e5102112f09536724b5db5b09416bb`
