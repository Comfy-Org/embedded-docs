# SigmalarıGürültüAzaltmaBöl

SplitSigmasDenoise düğümü, bir sigma değerleri dizisini, bir gürültü giderme gücü parametresine göre iki parçaya böler. Girdi sigmalarını yüksek ve düşük sigma dizileri olarak ayırır; bölünme noktası, toplam adım sayısının (sigma değeri sayısından bir eksik) `denoise` faktörüyle çarpılmasıyla belirlenir. Bu, gürültü çizelgesini özel işleme için farklı yoğunluk aralıklarına ayırmayı sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `sigmalar` | Gürültü çizelgesini temsil eden girdi sigma değerleri dizisi | SIGMAS | Evet | - |
| `gürültü_azaltma` | Sigma dizisinin nerede bölüneceğini belirleyen gürültü giderme gücü faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (step: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `high_sigmas` | Sigma dizisinin ilk kısmı; bölünme noktasına kadar olan daha yüksek sigma değerlerini içerir | SIGMAS |
| `low_sigmas` | Sigma dizisinin ikinci kısmı; bölünme noktasından itibaren daha düşük sigma değerlerini içerir | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/tr.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`
