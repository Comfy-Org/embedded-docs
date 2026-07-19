# SigmalarıGürültüAzaltmaBöl

SplitSigmasDenoise düğümü, bir sigma değerleri dizisini gürültü giderme gücü parametresine göre iki parçaya böler. Giriş sigmalarını yüksek ve düşük sigma dizilerine ayırır; bölünme noktası, toplam adım sayısının gürültü giderme faktörü ile çarpılmasıyla belirlenir. Bu, gürültü programının özel işleme için farklı yoğunluk aralıklarına ayrılmasını sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `sigmalar` | Gürültü programını temsil eden giriş sigma değerleri dizisi | SIGMAS | Evet | - |
| `gürültü_azaltma` | Sigma dizisinin nereden bölüneceğini belirleyen gürültü giderme gücü faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `high_sigmas` | Daha yüksek sigma değerlerini içeren sigma dizisinin ilk kısmı | SIGMAS |
| `low_sigmas` | Daha düşük sigma değerlerini içeren sigma dizisinin ikinci kısmı | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/tr.md)

---
**Source fingerprint (SHA-256):** `fda53efe2fcaed9244376b7360d8b0b76ce7395d594de4c2ecc48a8f243d7ca6`
