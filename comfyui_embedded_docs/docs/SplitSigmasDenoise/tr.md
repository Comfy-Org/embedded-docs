# SigmalarıGürültüAzaltmaBöl

SplitSigmasDenoise düğümü, bir sigma değerleri dizisini gürültü giderme gücü parametresine göre iki parçaya böler. Girdi sigmalarını yüksek ve düşük sigma dizileri olarak ayırır; ayırma noktası, toplam adımların denoise faktörüyle çarpılmasıyla belirlenir. Bu sayede gürültü zamanlaması, özel işlemler için farklı yoğunluk aralıklarına ayrılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `sigmalar` | Gürültü zamanlamasını temsil eden sigma değerlerinden oluşan girdi dizisi | SIGMAS | Evet | - |
| `gürültü_azaltma` | Sigma dizisinin nereden bölüneceğini belirleyen gürültü giderme gücü faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `yüksek_sigma` | Daha yüksek sigma değerleri içeren sigma dizisinin ilk bölümü | SIGMAS |
| `düşük_sigma` | Daha düşük sigma değerleri içeren sigma dizisinin ikinci bölümü | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/tr.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`
