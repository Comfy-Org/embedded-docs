> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/tr.md)

SplitSigmasDenoise düğümü, bir gürültü giderme kuvveti parametresine dayanarak bir sigma değerleri dizisini iki parçaya böler. Giriş sigmalarını yüksek ve düşük sigma dizilerine ayırır; burada bölme noktası, toplam adımların gürültü giderme faktörü ile çarpılmasıyla belirlenir. Bu, gürültü programını özel işlemler için farklı yoğunluk aralıklarına ayırmaya olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | SIGMAS | Evet | - | Gürültü programını temsil eden sigma değerlerinin giriş dizisi |
| `denoise` | FLOAT | Evet | 0.0 - 1.0 | Sigma dizisinin nerede bölüneceğini belirleyen gürültü giderme kuvveti faktörü (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `high_sigmas` | SIGMAS | Daha yüksek sigma değerlerini içeren sigma dizisinin ilk bölümü |
| `low_sigmas` | SIGMAS | Daha düşük sigma değerlerini içeren sigma dizisinin ikinci bölümü |