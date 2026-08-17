# SigmalarıGürültüAzaltmaBöl

SplitSigmasDenoise düğümü, bir sigma değerleri dizisini, gürültü giderme (denoising) gücü parametresine göre iki parçaya böler. Girdi sigmalarını yüksek ve düşük sigma dizileri olarak ayırır; bölünme noktası, toplam adım sayısının denoise faktörüyle çarpılmasıyla belirlenir. Bu, gürültü programının farklı yoğunluk aralıklarına ayrılmasına ve özel işleme tabi tutulmasına olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `sigmas` | Gürültü programını temsil eden sigma değerleri girdi dizisi | SIGMAS | Evet | - |
| `denoise` | Sigma dizisinin nereden bölüneceğini belirleyen gürültü giderme gücü faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

Not: Toplam adım sayısı, sigma değerlerinin sayısının 1 eksiğidir. İki çıktı dizisi, bölünme noktasında bir sigma değerini paylaşır. `denoise` = 0.0 olduğunda `high_sigmas` boştur; `denoise` = 1.0 olduğunda `high_sigmas` yalnızca ilk sigma değerini içerir ve `low_sigmas` dizinin tamamını içerir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `high_sigmas` | Sigma dizisinin daha yüksek sigma değerlerini içeren ilk bölümü | SIGMAS |
| `low_sigmas` | Sigma dizisinin daha düşük sigma değerlerini içeren ikinci bölümü | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/tr.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`
