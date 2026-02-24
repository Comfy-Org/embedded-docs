> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/tr.md)

Hunyuan Video 15 Latent Upscale With Model düğümü, bir gizli (latent) görüntü temsilinin çözünürlüğünü artırır. Önce gizli örnekleri seçilen bir enterpolasyon yöntemi kullanarak belirtilen bir boyuta yükseltir, ardından kaliteyi iyileştirmek için özel bir Hunyuan Video 1.5 yükseltme modeli kullanarak yükseltilmiş sonucu işler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | LATENT_UPSCALE_MODEL | Evet | Yok | Yükseltilmiş örnekleri iyileştirmek için kullanılan Hunyuan Video 1.5 gizli yükseltme modeli. |
| `samples` | LATENT | Evet | Yok | Yükseltilecek gizli görüntü temsili. |
| `upscale_method` | COMBO | Hayır | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` | İlk yükseltme adımında kullanılan enterpolasyon algoritması (varsayılan: `"bilinear"`). |
| `width` | INT | Hayır | 0 - 16384 | Yükseltilmiş gizli görüntü için hedef genişlik (piksel cinsinden). 0 değeri, hedef yüksekliğe ve orijinal en-boy oranına göre genişliği otomatik olarak hesaplayacaktır. Nihai çıktı genişliği 16'nın katı olacaktır (varsayılan: 1280). |
| `height` | INT | Hayır | 0 - 16384 | Yükseltilmiş gizli görüntü için hedef yükseklik (piksel cinsinden). 0 değeri, hedef genişliğe ve orijinal en-boy oranına göre yüksekliği otomatik olarak hesaplayacaktır. Nihai çıktı yüksekliği 16'nın katı olacaktır (varsayılan: 720). |
| `crop` | COMBO | Hayır | `"disabled"`<br>`"center"` | Yükseltilmiş gizli görüntünün hedef boyutlara sığdırılmak üzere nasıl kırpılacağını belirler. |

**Boyutlar Hakkında Not:** Hem `width` hem de `height` 0 olarak ayarlanırsa, düğüm girdi `samples` değerini değiştirmeden döndürür. Yalnızca bir boyut 0 olarak ayarlanırsa, diğer boyut orijinal en-boy oranını koruyacak şekilde hesaplanır. Nihai boyutlar her zaman en az 64 piksel olacak ve 16'ya bölünebilir olacak şekilde ayarlanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Yükseltilmiş ve model tarafından işlenmiş gizli görüntü temsili. |
