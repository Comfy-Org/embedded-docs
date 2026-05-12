> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/tr.md)

## Genel Bakış

Bu düğüm, OpenAI'nin GPT Image API'sini kullanarak görseller oluşturur. Birden fazla modeli destekler, düzenleme için giriş görselleri sağlamanıza olanak tanır ve bir görselin hangi bölümlerinin değiştirileceğini belirtmek için maske kullanabilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | GPT Image için metin istemi (varsayılan: ""). |
| `model` | COMBO | Evet | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` | Kullanılacak OpenAI GPT Image modeli. Bir model seçmek, o modele özgü ek parametreleri ortaya çıkarır. |
| `model.size` | COMBO | Evet | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` | Görsel boyutu. Özel genişlik ve yükseklik kullanmak için 'Custom' seçeneğini seçin (varsayılan: "auto"). Yalnızca `gpt-image-2` için kullanılabilir. |
| `model.custom_width` | INT | Hayır | 1024 - 3840 | Yalnızca `size` 'Custom' olduğunda kullanılır. 16'nın katı olmalıdır (varsayılan: 1024). Yalnızca `gpt-image-2` için kullanılabilir. |
| `model.custom_height` | INT | Hayır | 1024 - 3840 | Yalnızca `size` 'Custom' olduğunda kullanılır. 16'nın katı olmalıdır (varsayılan: 1024). Yalnızca `gpt-image-2` için kullanılabilir. |
| `model.background` | COMBO | Evet | `"auto"`<br>`"opaque"` | Görseli arka planlı veya arka plansız döndürür (varsayılan: "auto"). Yalnızca `gpt-image-2` için kullanılabilir. |
| `model.quality` | COMBO | Evet | `"standard"`<br>`"hd"` | Oluşturulan görselin kalitesi. Yalnızca `gpt-image-2` için kullanılabilir. |
| `model.images` | IMAGE | Hayır | Yok | Düzenleme için giriş görselleri. Yalnızca `gpt-image-2` için kullanılabilir. |
| `model.mask` | MASK | Hayır | Yok | Giriş görselinin hangi bölümlerinin düzenleneceğini belirten bir maske. Yalnızca `gpt-image-2` için kullanılabilir. |
| `n` | INT | Evet | 1 - 8 | Oluşturulacak görsel sayısı (varsayılan: 1). |
| `seed` | INT | Evet | 0 - 2147483647 | Tekrarlanabilirlik için tohum değeri (varsayılan: 0). Not: Henüz arka uçta uygulanmamıştır. |

**Parametre Kısıtlamaları ve Sınırlamaları:**

- `gpt-image-2` ile `model.size` "Custom" olarak kullanıldığında, `custom_width` ve `custom_height` değerleri 16'nın katı olmalı, maksimum kenar <= 3840 olmalı, en-boy oranı 3:1'i geçmemeli ve toplam piksel sayısı 655.360 ile 8.294.400 arasında olmalıdır.
- Bir `mask` sağlanırsa, bir giriş görseli (`model.images`) gereklidir. Maske, giriş görseli olmadan kullanılamaz.
- Bir maske, birden fazla giriş görseli ile kullanılamaz.
- Bir maske sağlandığında, maske boyutları giriş görseli boyutlarıyla eşleşmelidir.
- `seed` parametresi şu anda işlevsel değildir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Oluşturulan görsel veya görseller. |