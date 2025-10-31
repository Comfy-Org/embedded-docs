> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningAverage/tr.md)

`ConditioningAverage` düğümü, iki farklı koşullandırma kümesini (metin istemleri gibi) belirli bir ağırlığa göre harmanlayarak, ikisi arasında yer alan yeni bir koşullandırma vektörü oluşturmak için kullanılır. Ağırlık parametresini ayarlayarak, her bir koşullandırmanın nihai sonuç üzerindeki etkisini esnek bir şekilde kontrol edebilirsiniz. Bu özellikle, istem enterpolasyonu, stil füzyonu ve diğer gelişmiş kullanım senaryoları için uygundur.

Aşağıda gösterildiği gibi, `conditioning_to` parametresinin gücünü ayarlayarak, iki koşullandırma arasında bir sonuç elde edebilirsiniz.

![örnek](./asset/example.webp)

## Girdiler

| Parametre               | Comfy Veri Türü | Açıklama |
|------------------------|---------------|-------------|
| `hedef_koşullandırma`      | `CONDITIONING`| Ağırlıklı ortalamanın ana temeli olarak hizmet eden hedef koşullandırma vektörü. |
| `kaynak_koşullandırma`    | `CONDITIONING`| Belirli bir ağırlığa göre hedefe harmanlanacak olan kaynak koşullandırma vektörü. |
| `hedef_koşullandırma_gücü` | `FLOAT`    | Hedef koşullandırmanın gücü, aralık 0.0-1.0, varsayılan 1.0, adım 0.01. |

## Çıktılar

| Parametre        | Comfy Veri Türü | Açıklama |
|------------------|---------------|-------------|
| `conditioning`   | `CONDITIONING`| Harmanlama sonrasında elde edilen, ağırlıklı ortalamayı yansıtan koşullandırma vektörü. |

## Tipik Kullanım Senaryoları

- **İstem Enterpolasyonu:** İki farklı metin istemi arasında sorunsuz geçiş yaparak, ara stil veya anlambilime sahip içerik oluşturun.
- **Stil Füzyonu:** Farklı sanatsal stilleri veya anlamsal koşulları birleştirerek yeni efektler yaratın.
- **Güç Ayarlama:** Ağırlığı ayarlayarak belirli bir koşullandırmanın sonuç üzerindeki etkisini hassas bir şekilde kontrol edin.
- **Yaratıcı Keşif:** Farklı istemleri karıştırarak çeşitli üretken efektleri keşfedin.