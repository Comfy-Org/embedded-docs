# Koşullandırma (Birleştir)

Bu düğüm, iki koşullandırma girdisini tek bir çıktıda birleştirerek bilgilerini etkili bir şekilde harmanlar. İki koşul, liste birleştirme kullanılarak bir araya getirilir.

## Girişler

| Parametre Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `koşullandırma_1` | Birleştirilecek ilk koşullandırma girdisi. Birleştirme işleminde `koşullandırma_2` ile eşit öneme sahiptir. | `CONDITIONING` |
| `koşullandırma_2` | Birleştirilecek ikinci koşullandırma girdisi. Birleştirme işleminde `koşullandırma_1` ile eşit öneme sahiptir. | `CONDITIONING` |

## Çıktılar

| Parametre Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | `koşullandırma_1` ve `koşullandırma_2`'nin birleştirilmesi sonucu oluşan, harmanlanmış bilgiyi kapsayan çıktı. | `CONDITIONING` |

## Kullanım Senaryoları

Aşağıdaki iki grubu karşılaştırın: sol tarafta ConditioningCombine düğümü kullanılırken, sağ tarafta normal çıktı gösterilmektedir.

![Karşılaştırma](./asset/compare.jpg)

Bu örnekte, `Conditioning Combine` içinde kullanılan iki koşul eşdeğer öneme sahiptir. Bu nedenle, görüntü stili, konu özellikleri vb. için farklı metin kodlamaları kullanabilir ve böylece prompt özelliklerinin daha eksiksiz çıktılanmasını sağlayabilirsiniz. İkinci prompt, birleştirilmiş tam promptu kullanır, ancak anlamsal anlama tamamen farklı koşulları kodlayabilir.

Bu düğümü kullanarak şunları elde edebilirsiniz:

- Temel metin birleştirme: İki `CLIP Text Encode` düğümünün çıktılarını `Conditioning Combine`'ın iki giriş portuna bağlayın
- Karmaşık prompt birleştirme: Pozitif ve negatif promptları birleştirin veya ana açıklamalar ile stil açıklamalarını ayrı ayrı kodlayıp birleştirin
- Koşullu zincir birleştirme: Birden çok `Conditioning Combine` düğümünü seri olarak kullanarak birden çok koşulun aşamalı birleşimini sağlayın

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningCombine/tr.md)
