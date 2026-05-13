> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/tr.md)

LTXVImgToVideo düğümü, video oluşturma modelleri için bir girdi görüntüsünü video gizil katman temsiline dönüştürür. Tek bir görüntü alır ve VAE kodlayıcıyı kullanarak bunu bir dizi kareye genişletir, ardından video oluşturma sırasında orijinal görüntü içeriğinin ne kadarının korunacağını ve ne kadarının değiştirileceğini belirlemek için güç kontrolü ile koşullandırma uygular.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `positive` | CONDITIONING | Evet | - | Video oluşturmayı yönlendirmek için pozitif koşullandırma istemleri |
| `negative` | CONDITIONING | Evet | - | Videoda belirli öğelerden kaçınmak için negatif koşullandırma istemleri |
| `vae` | VAE | Evet | - | Girdi görüntüsünü gizil katmana kodlamak için kullanılan VAE modeli |
| `image` | IMAGE | Evet | - | Video karelerine dönüştürülecek girdi görüntüsü |
| `width` | INT | Hayır | 64 ile MAKS_ÇÖZÜNÜRLÜK | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 768, adım: 32) |
| `height` | INT | Hayır | 64 ile MAKS_ÇÖZÜNÜRLÜK | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 512, adım: 32) |
| `length` | INT | Hayır | 9 ile MAKS_ÇÖZÜNÜRLÜK | Oluşturulan videodaki kare sayısı (varsayılan: 97, adım: 8) |
| `batch_size` | INT | Hayır | 1 ile 4096 | Aynı anda oluşturulacak video sayısı (varsayılan: 1) |
| `strength` | FLOAT | Hayır | 0,0 ile 1,0 | Oluşturulan videonun ilk karesinde orijinal görüntü içeriğinin ne kadarının korunacağını kontrol eder. 1,0 değeri orijinal görüntüyü tamamen korurken, 0,0 maksimum değişikliğe izin verir (varsayılan: 1,0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `positive` | CONDITIONING | Video kare maskelemesi uygulanmış işlenmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Video kare maskelemesi uygulanmış işlenmiş negatif koşullandırma |
| `latent` | LATENT | Video oluşturma için kodlanmış kareleri ve gürültü maskesini içeren video gizil katman temsili |

---
**Source fingerprint (SHA-256):** `fbd35623cd71bf917f39108d388986c9604138fbfb9380bdf936deff6d775cb9`
