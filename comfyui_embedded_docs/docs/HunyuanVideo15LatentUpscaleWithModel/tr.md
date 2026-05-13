> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/tr.md)

Hunyuan Video 15 Latent Upscale With Model düğümü, bir latent görüntü temsilinin çözünürlüğünü artırır. İlk olarak, seçilen bir enterpolasyon yöntemini kullanarak latent örnekleri belirtilen bir boyuta yükseltir, ardından kaliteyi iyileştirmek için özel bir Hunyuan Video 1.5 yükseltme modeli kullanarak yükseltilmiş sonucu iyileştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | LATENT_UPSCALE_MODEL | Evet | Yok | Yükseltilmiş örnekleri iyileştirmek için kullanılan Hunyuan Video 1.5 latent yükseltme modeli. |
| `samples` | LATENT | Evet | Yok | Yükseltilecek latent görüntü temsili. |
| `upscale_method` | COMBO | Hayır | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` | İlk yükseltme adımında kullanılan enterpolasyon algoritması (varsayılan: `"bilinear"`). |
| `width` | INT | Hayır | 0 ile 16384 | Yükseltilmiş latent için piksel cinsinden hedef genişlik. 0 değeri, hedef yükseklik ve orijinal en-boy oranına göre genişliği otomatik olarak hesaplar. Nihai çıktı genişliği 16'nın katı olacaktır (varsayılan: 1280). |
| `height` | INT | Hayır | 0 ile 16384 | Yükseltilmiş latent için piksel cinsinden hedef yükseklik. 0 değeri, hedef genişlik ve orijinal en-boy oranına göre yüksekliği otomatik olarak hesaplar. Nihai çıktı yüksekliği 16'nın katı olacaktır (varsayılan: 720). |
| `crop` | COMBO | Hayır | `"disabled"`<br>`"center"` | Yükseltilmiş latentin hedef boyutlara sığması için nasıl kırpılacağını belirler. |

**Boyutlar Hakkında Not:** Hem `width` hem de `height` 0 olarak ayarlanırsa, düğüm giriş `samples` değerini değiştirmeden döndürür. Yalnızca bir boyut 0 olarak ayarlanırsa, diğer boyut orijinal en-boy oranını koruyacak şekilde hesaplanır. Nihai boyutlar her zaman en az 64 piksel olacak şekilde ayarlanır ve 16'ya bölünebilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Yükseltilmiş ve model tarafından iyileştirilmiş latent görüntü temsili. |

---
**Source fingerprint (SHA-256):** `1de9e157c1a0433f1b3d5ff4d428a1aa392fd65da5e314e6e818ce66495d5ef4`
