> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/tr.md)

LTXVImgToVideo düğümü, video oluşturma modelleri için bir girdi görüntüsünü video gizil katman temsiline dönüştürür. Tek bir görüntü alır ve VAE kodlayıcıyı kullanarak bunu bir dizi kareye genişletir, ardından video oluşturma sırasında orijinal görüntü içeriğinin ne kadarının korunacağını ve ne kadarının değiştirileceğini belirlemek için güç kontrolü ile koşullandırma uygular.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `pozitif` | CONDITIONING | Evet | - | Video oluşturmayı yönlendirmek için pozitif koşullandırma istemleri |
| `negatif` | CONDITIONING | Evet | - | Videoda belirli öğelerden kaçınmak için negatif koşullandırma istemleri |
| `vae` | VAE | Evet | - | Girdi görüntüsünü gizil katmana kodlamak için kullanılan VAE modeli |
| `görüntü` | IMAGE | Evet | - | Video karelerine dönüştürülecek girdi görüntüsü |
| `genişlik` | INT | Hayır | 64 ile MAKS_ÇÖZÜNÜRLÜK | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 768, adım: 32) |
| `yükseklik` | INT | Hayır | 64 ile MAKS_ÇÖZÜNÜRLÜK | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 512, adım: 32) |
| `uzunluk` | INT | Hayır | 9 ile MAKS_ÇÖZÜNÜRLÜK | Oluşturulan videodaki kare sayısı (varsayılan: 97, adım: 8) |
| `toplu_boyut` | INT | Hayır | 1 ile 4096 | Aynı anda oluşturulacak video sayısı (varsayılan: 1) |
| `güç` | FLOAT | Hayır | 0,0 ile 1,0 | Oluşturulan videonun ilk karesinde orijinal görüntü içeriğinin ne kadarının korunacağını kontrol eder. 1,0 değeri orijinal görüntüyü tamamen korurken, 0,0 maksimum değişikliğe izin verir (varsayılan: 1,0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `negatif` | CONDITIONING | Video kare maskelemesi uygulanmış işlenmiş pozitif koşullandırma |
| `gizli` | CONDITIONING | Video kare maskelemesi uygulanmış işlenmiş negatif koşullandırma |
| `latent` | LATENT | Video oluşturma için kodlanmış kareleri ve gürültü maskesini içeren video gizil katman temsili |

---
**Source fingerprint (SHA-256):** `fbd35623cd71bf917f39108d388986c9604138fbfb9380bdf936deff6d775cb9`
