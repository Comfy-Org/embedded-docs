# Hunyuan Video 15 Latent Upscale With Model

Hunyuan Video 15 Latent Upscale With Model düğümü, latent görüntü temsilinin çözünürlüğünü artırır. Önce latent örnekleri seçilen bir enterpolasyon yöntemi kullanarak belirli bir boyuta ölçekler, ardından kaliteyi iyileştirmek için özel bir Hunyuan Video 1.5 upscale modeli kullanarak ölçeklenen sonucu hassaslaştırır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Ölçeklenen örnekleri iyileştirmek için kullanılan Hunyuan Video 1.5 latent upscale modeli. | LATENT_UPSCALE_MODEL | Evet | N/A |
| `samples` | Ölçeklenecek latent görüntü temsili. | LATENT | Evet | N/A |
| `upscale_method` | İlk ölçekleme adımında kullanılan enterpolasyon algoritması (varsayılan: `"bilinear"`). | COMBO | Hayır | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `width` | Ölçeklenen latent için piksel cinsinden hedef genişlik. 0 değeri, genişliğin hedef yüksekliğe ve orijinal en-boy oranına göre otomatik hesaplanmasını sağlar. Son çıktı genişliği 16'nın katı olacaktır (varsayılan: 1280). | INT | Hayır | 0 to 16384 (step 8) |
| `height` | Ölçeklenen latent için piksel cinsinden hedef yükseklik. 0 değeri, yüksekliğin hedef genişliğe ve orijinal en-boy oranına göre otomatik hesaplanmasını sağlar. Son çıktı yüksekliği 16'nın katı olacaktır (varsayılan: 720). | INT | Hayır | 0 to 16384 (step 8) |
| `crop` | Ölçeklenen latentin hedef boyutlara sığacak şekilde nasıl kırpılacağını belirler. | COMBO | Hayır | `"disabled"`<br>`"center"` |

**Boyutlar Hakkında Not:** Hem `width` hem de `height` 0 olarak ayarlanırsa, düğüm girdi `samples` değerini değiştirmeden döndürür. Yalnızca bir boyut 0 olarak ayarlanırsa, diğer boyut orijinal en-boy oranını koruyacak şekilde hesaplanır. Son boyutlar her zaman en az 64 piksel olacak ve 16'ya bölünebilir olacak şekilde ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Ölçeklenmiş ve modelle iyileştirilmiş latent görüntü temsili. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/tr.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`
