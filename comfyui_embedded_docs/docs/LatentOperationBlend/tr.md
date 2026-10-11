# Latent Operation Blend

Bu düğüm, bir latent'i bir referans latent'e doğru harmanlayan bir latent işlemi oluşturur ve bu işlemi Latent Apply Operation veya Latent Apply Operation CFG gibi düğümlere takılabilecek şekilde döndürür. Referans farklı bir uzamsal boyuta sahip olduğunda, hedef latent'e en yakın komşu enterpolasyonuyla yeniden boyutlandırılır ve daha küçük bir gruba sahip referans, hedef grup boyutuyla eşleşmesi için tekrarlanır. 0 `strength` değeri, latent'i değiştirmeden bırakır. Bu düğüm deneysel olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `reference` | Kendisine doğru harmanlanacak latent. Örnekleri, işlenen latentin cihazına ve dtype'ına dönüştürülür; ardından onunla eşleşmesi için yeniden boyutlandırılır ve tekrarlanır. | LATENT | Evet | - |
| `strength` | Referansa doğru ne kadar harmanlanacağı: 0, latent'i değiştirmeden bırakır; 1, yeniden boyutlandırılmış referans latent ile eşleşir (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 arası (adım 0.0001) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `operation` | Latent örneklerine uygulanabilecek bir harmanlama işlemi. | LATENT_OPERATION |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationBlend/tr.md)

---
**Source fingerprint (SHA-256):** `5890089afddf83ddd4edd992606509b118aac9ef13eb89589f73fa75e0b9dd5a`
