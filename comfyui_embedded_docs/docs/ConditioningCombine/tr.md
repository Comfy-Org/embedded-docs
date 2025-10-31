> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningCombine/tr.md)

Bu düğüm, iki koşullandırma girdisini tek bir çıktıda birleştirerek bilgilerini etkili bir şekilde birleştirir. İki koşul, liste birleştirme kullanılarak birleştirilir.

## Girdiler

| Parametre Adı        | Veri Türü          | Açıklama |
|----------------------|--------------------|-------------|
| `conditioning_1`     | `CONDITIONING`     | Birleştirilecek ilk koşullandırma girdisi. Birleştirme işleminde `conditioning_2` ile eşit öneme sahiptir. |
| `conditioning_2`     | `CONDITIONING`     | Birleştirilecek ikinci koşullandırma girdisi. Birleştirme işleminde `conditioning_1` ile eşit öneme sahiptir. |

## Çıktılar

| Parametre Adı        | Veri Türü          | Açıklama |
|----------------------|--------------------|-------------|
| `conditioning`       | `CONDITIONING`     | `conditioning_1` ve `conditioning_2`'nin birleştirilmesi sonucu, birleştirilmiş bilgiyi kapsayan çıktı. |

## Kullanım Senaryoları

Aşağıdaki iki grubu karşılaştırın: sol taraf ConditioningCombine düğümünü kullanırken, sağ taraf normal çıktıyı göstermektedir.

![Karşılaştırma](./asset/compare.jpg)

Bu örnekte, `Conditioning Combine` içinde kullanılan iki koşul eşdeğer öneme sahiptir. Bu nedenle, görüntü stili, konu özellikleri vb. için farklı metin kodlamaları kullanabilir, böylece prompt özelliklerinin daha eksiksiz çıktılanmasını sağlayabilirsiniz. İkinci prompt, birleştirilmiş tam prompt'u kullanır, ancak anlamsal anlama tamamen farklı koşullar kodlayabilir.

Bu düğümü kullanarak şunları başarabilirsiniz:

- Temel metin birleştirme: İki `CLIP Text Encode` düğümünün çıktılarını `Conditioning Combine`'un iki giriş portuna bağlayın
- Karmaşık prompt birleştirme: Olumlu ve olumsuz prompt'ları birleştirin veya ana açıklamaları ve stil açıklamalarını ayrı ayrı kodladıktan sonra birleştirin
- Koşullu zincir birleştirme: Birden fazla `Conditioning Combine` düğümü, birden fazla koşulun kademeli olarak birleştirilmesini sağlamak için seri olarak kullanılabilir