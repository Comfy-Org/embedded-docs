# Hunyuan Video 15 Latent Upscale With Model

Hunyuan Video 15 Latent Upscale With Model düğümü, bir latent görüntü temsilinin çözünürlüğünü artırır. Önce seçilen bir enterpolasyon yöntemini kullanarak latent örneklerini belirtilen bir boyuta büyütür, ardından kaliteyi artırmak için özelleşmiş bir Hunyuan Video 1.5 büyütme modeli kullanarak büyütülmüş sonucu iyileştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Büyütülen örnekleri iyileştirmek için kullanılan Hunyuan Video 1.5 latent büyütme modeli. | LATENT_UPSCALE_MODEL | Evet | N/A |
| `örnekler` | Büyütülecek latent görüntü temsili. | LATENT | Evet | N/A |
| `büyütme_yöntemi` | İlk büyütme adımında kullanılan enterpolasyon algoritması (varsayılan: `"bilinear"`). | COMBO | Evet | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `genişlik` | Büyütülen latent için hedef genişlik, piksel cinsinden. 0 değeri, hedef yüksekliğe ve özgün en-boy oranına göre genişliği otomatik olarak hesaplar. Nihai çıktı genişliği 16'nın katı olur (varsayılan: 1280). | INT | Evet | 0 ile 16384 (step: 8) |
| `yükseklik` | Büyütülen latent için hedef yükseklik, piksel cinsinden. 0 değeri, hedef genişliğe ve özgün en-boy oranına göre yüksekliği otomatik olarak hesaplar. Nihai çıktı yüksekliği 16'nın katı olur (varsayılan: 720). | INT | Evet | 0 ile 16384 (step: 8) |
| `kırp` | Büyütülen latentin hedef boyutlara sığdırılmak üzere nasıl kırpılacağını belirler. | COMBO | Evet | `"disabled"`<br>`"center"` |

**Boyutlarla İlgili Not:** Eğer hem `width` hem de `height` 0 olarak ayarlanırsa, düğüm girdi `samples` değerini değiştirmeden döndürür. Eğer yalnızca bir boyut 0 olarak ayarlanırsa, diğer boyut özgün en-boy oranını koruyacak şekilde hesaplanır. Her iki değer de en az 64 olacak şekilde sınırlandırılır ve enterpolasyon adımına aktarılan büyütme hedefi `width // 16` x `height // 16` olur; bu nedenle istenen boyutlar etkin biçimde 16'nın katlarına aşağı yuvarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Büyütülmüş ve modelle iyileştirilmiş latent görüntü temsili, CPU üzerinde bir float tensörü olarak döndürülür. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/tr.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`
