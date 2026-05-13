> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/tr.md)

SplitSigmasDenoise düğümü, bir sigma değerleri dizisini gürültü giderme gücü parametresine göre iki parçaya böler. Giriş sigmalarını yüksek ve düşük sigma dizilerine ayırır; bölünme noktası, toplam adım sayısının gürültü giderme faktörü ile çarpılmasıyla belirlenir. Bu, gürültü programının özel işleme için farklı yoğunluk aralıklarına ayrılmasını sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `sigmas` | SIGMAS | Evet | - | Gürültü programını temsil eden giriş sigma değerleri dizisi |
| `denoise` | FLOAT | Evet | 0.0 - 1.0 | Sigma dizisinin nereden bölüneceğini belirleyen gürültü giderme gücü faktörü (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `high_sigmas` | SIGMAS | Daha yüksek sigma değerlerini içeren sigma dizisinin ilk kısmı |
| `low_sigmas` | SIGMAS | Daha düşük sigma değerlerini içeren sigma dizisinin ikinci kısmı |

---
**Source fingerprint (SHA-256):** `fda53efe2fcaed9244376b7360d8b0b76ce7395d594de4c2ecc48a8f243d7ca6`
