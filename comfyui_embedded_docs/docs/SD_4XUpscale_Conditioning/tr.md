# SD_4X_Büyütme_Koşullandırma

SD_4XUpscale_Conditioning düğümü, difüzyon modellerini kullanarak görüntüleri büyütmek için koşullandırma verilerini hazırlar. Giriş görüntülerini ve koşullandırma verilerini alır, ardından büyütme sürecini yönlendiren değiştirilmiş koşullandırma oluşturmak için ölçekleme ve gürültü artırma uygular. Düğüm, büyütülmüş boyutlar için latent temsillerle birlikte hem pozitif hem de negatif koşullandırma çıktısı verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `images` | Büyütülecek giriş görüntüleri | IMAGE | Evet | - |
| `positive` | İstenen içeriğe doğru üretimi yönlendiren pozitif koşullandırma verileri | CONDITIONING | Evet | - |
| `negative` | İstenmeyen içerikten üretimi uzaklaştıran negatif koşullandırma verileri | CONDITIONING | Evet | - |
| `scale_ratio` | Giriş görüntülerine uygulanan ölçekleme faktörü (varsayılan: 4.0) | FLOAT | Evet | 0.0 - 10.0 |
| `noise_augmentation` | Büyütme işlemi sırasında eklenecek gürültü miktarı (varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 |

Hedef büyütülmüş boyutlar, giriş görüntüsü boyutlarının `scale_ratio` ile çarpılmasıyla hesaplanır. Koşullandırmaya gömülü görüntü ve çıktı latent'i, bu hedef boyutların dörtte biri olarak oluşturulur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Büyütme bilgisi uygulanmış değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Büyütme bilgisi uygulanmış değiştirilmiş negatif koşullandırma | CONDITIONING |
| `latent` | Büyütülmüş boyutlarla eşleşen boş latent temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`
