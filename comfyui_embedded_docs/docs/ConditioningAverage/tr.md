> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningAverage/tr.md)

`ConditioningAverage` düğümü, belirtilen bir ağırlığa göre iki farklı koşullandırma kümesini (metin istemleri gibi) harmanlamak ve ikisi arasında kalan yeni bir koşullandırma vektörü oluşturmak için kullanılır. Ağırlık parametresini ayarlayarak, her bir koşullandırmanın nihai sonuç üzerindeki etkisini esnek bir şekilde kontrol edebilirsiniz. Bu, özellikle istem enterpolasyonu, stil füzyonu ve diğer ileri düzey kullanım durumları için uygundur.

Aşağıda gösterildiği gibi, `conditioning_to` gücünü ayarlayarak iki koşullandırma arasında bir sonuç elde edebilirsiniz.

![example](./asset/example.webp)

## Girişler

| Parametre               | Comfy dtype    | Açıklama |
|------------------------|---------------|-------------|
| `conditioning_to`      | `CONDITIONING`| Ağırlıklı ortalama için ana temel görevi gören hedef koşullandırma vektörü. |
| `conditioning_from`    | `CONDITIONING`| Belirli bir ağırlığa göre hedefe harmanlanacak kaynak koşullandırma vektörü. |
| `conditioning_to_strength` | `FLOAT`    | Hedef koşullandırmanın gücü, aralık 0.0-1.0, varsayılan 1.0, adım 0.01. |

## Çıkışlar

| Parametre        | Comfy dtype    | Açıklama |
|------------------|---------------|-------------|
| `conditioning`   | `CONDITIONING`| Harmanlama sonrasında elde edilen, ağırlıklı ortalamayı yansıtan koşullandırma vektörü. |

## Tipik Kullanım Durumları

- **İstem Enterpolasyonu:** İki farklı metin istemi arasında yumuşak geçiş yaparak ara stilde veya anlamsal içerikte çıktılar üretir.
- **Stil Füzyonu:** Farklı sanatsal stilleri veya anlamsal koşulları birleştirerek yeni efektler oluşturur.
- **Güç Ayarı:** Ağırlığı ayarlayarak belirli bir koşullandırmanın sonuç üzerindeki etkisini hassas bir şekilde kontrol eder.
- **Yaratıcı Keşif:** Farklı istemleri karıştırarak çeşitli üretken efektleri keşfeder.