# OpenAI GPT Görüntü 2

## Genel Bakış

Bu düğüm, OpenAI'nin GPT Image API'sini kullanarak görseller oluşturur. Birden fazla modeli destekler, düzenleme için giriş görselleri sağlamanıza olanak tanır ve bir görselin hangi bölümlerinin değiştirileceğini belirtmek için maske kullanabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | GPT Image için metin istemi (varsayılan: ""). | STRING | Evet | Yok |
| `model` | Kullanılacak OpenAI GPT Image modeli. Bir model seçmek, o modele özgü ek parametreleri ortaya çıkarır. | COMBO | Evet | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `model.size` | Görsel boyutu. Özel genişlik ve yükseklik kullanmak için 'Custom' seçeneğini seçin (varsayılan: "auto"). Yalnızca `gpt-image-2` için kullanılabilir. | COMBO | Evet | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Yalnızca `size` 'Custom' olduğunda kullanılır. 16'nın katı olmalıdır (varsayılan: 1024). Yalnızca `gpt-image-2` için kullanılabilir. | INT | Hayır | 1024 - 3840 |
| `model.custom_height` | Yalnızca `size` 'Custom' olduğunda kullanılır. 16'nın katı olmalıdır (varsayılan: 1024). Yalnızca `gpt-image-2` için kullanılabilir. | INT | Hayır | 1024 - 3840 |
| `model.background` | Görseli arka planlı veya arka plansız döndürür (varsayılan: "auto"). Yalnızca `gpt-image-2` için kullanılabilir. | COMBO | Evet | `"auto"`<br>`"opaque"` |
| `model.quality` | Oluşturulan görselin kalitesi. Yalnızca `gpt-image-2` için kullanılabilir. | COMBO | Evet | `"standard"`<br>`"hd"` |
| `model.images` | Düzenleme için giriş görselleri. Yalnızca `gpt-image-2` için kullanılabilir. | IMAGE | Hayır | Yok |
| `model.mask` | Giriş görselinin hangi bölümlerinin düzenleneceğini belirten bir maske. Yalnızca `gpt-image-2` için kullanılabilir. | MASK | Hayır | Yok |
| `n` | Kaç adet görsel oluşturulacağı (varsayılan: 1). | INT | Evet | 1 - 8 |
| `tohum` | Tekrarlanabilirlik için tohum değeri (varsayılan: 0). Not: Henüz arka uçta uygulanmamıştır. | INT | Evet | 0 - 2147483647 |

**Parametre Kısıtlamaları ve Sınırlamaları:**

- `gpt-image-2` kullanılırken `model.size` değeri "Custom" olduğunda, `custom_width` ve `custom_height` değerleri 16'nın katı olmalı, maksimum kenar <= 3840 olmalı, en-boy oranı 3:1'i geçmemeli ve toplam piksel sayısı 655.360 ile 8.294.400 arasında olmalıdır.
- Bir `mask` sağlanmışsa, bir giriş görseli (`model.images`) gereklidir. Giriş görseli olmadan maske kullanılamaz.
- Birden fazla giriş görseli ile maske kullanılamaz.
- Maske sağlandığında, maske boyutları giriş görseli boyutlarıyla eşleşmelidir.
- `seed` parametresi şu anda işlevsel değildir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Oluşturulan görsel veya görseller. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `a757208cf6cc151594599b35b0ef73f2caf7274189e948799211c0714a6a8f89`
