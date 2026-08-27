# Hunyuan Video 15 Latent Upscale With Model

Hunyuan Video 15 Latent Upscale With Model düğümü, bir latent görüntü temsilinin çözünürlüğünü artırır. Önce latent örnekleri seçilen bir enterpolasyon yöntemi kullanarak belirtilen boyuta yükseltir, ardından yükseltilmiş sonucu kaliteyi iyileştirmek için özel bir Hunyuan Video 1.5 yükseltme modeli kullanarak hassaslaştırır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Yükseltilmiş örnekleri hassaslaştırmak için kullanılan Hunyuan Video 1.5 latent yükseltme modeli. | LATENT_UPSCALE_MODEL | Evet | N/A |
| `örnekler` | Yükseltilecek latent görüntü temsili. | LATENT | Evet | N/A |
| `büyütme_yöntemi` | İlk yükseltme adımında kullanılan enterpolasyon algoritması (varsayılan: `"bilinear"`). | COMBO | Hayır | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `genişlik` | Yükseltilmiş latent için piksel cinsinden hedef genişlik. 0 değeri, genişliği hedef yüksekliğe ve orijinal en-boy oranına göre otomatik hesaplar. Nihai çıktı genişliği 16'nın katı olacaktır (varsayılan: 1280). | INT | Hayır | 0 ila 16384 (adım: 8) |
| `yükseklik` | Yükseltilmiş latent için piksel cinsinden hedef yükseklik. 0 değeri, yüksekliği hedef genişliğe ve orijinal en-boy oranına göre otomatik hesaplar. Nihai çıktı yüksekliği 16'nın katı olacaktır (varsayılan: 720). | INT | Hayır | 0 ila 16384 (adım: 8) |
| `kırp` | Yükseltilmiş latentin hedef boyutlara sığacak şekilde nasıl kırpılacağını belirler. | COMBO | Hayır | `"disabled"`<br>`"center"` |

**Boyutlar Hakkında Not:** Hem `width` hem de `height` 0 olarak ayarlanırsa, düğüm girdi `samples` değerini değiştirmeden döndürür. Yalnızca bir boyut 0 olarak ayarlanırsa, diğer boyut orijinal en-boy oranını koruyacak şekilde hesaplanır. Nihai boyutlar her zaman en az 64 piksel olacak şekilde ayarlanır ve 16'ya bölünebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Yükseltilmiş ve modelle hassaslaştırılmış latent görüntü temsili. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/tr.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`
