> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoLinearCFGGuidance/tr.md)

VideoLinearCFGGuidance düğümü, bir video modeline doğrusal koşullandırma kılavuz ölçeği uygulayarak, koşullandırılmış ve koşullandırılmamış bileşenlerin etkisini belirli bir aralıkta ayarlar. Bu, üretim süreci üzerinde dinamik kontrol sağlayarak modelin çıktısını istenen koşullandırma seviyesine göre hassas bir şekilde ayarlamaya olanak tanır.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model`   | MODEL     | Model parametresi, doğrusal CFG kılavuzunun uygulanacağı video modelini temsil eder. Kılavuz ölçeği ile değiştirilecek temel modeli tanımlamak için çok önemlidir. |
| `min_cfg` | `FLOAT`     | min_cfg parametresi, uygulanacak minimum koşullandırma kılavuz ölçeğini belirtir ve doğrusal ölçek ayarının başlangıç noktası olarak hizmet eder. Kılavuz ölçeğinin alt sınırını belirlemede ve modelin çıktısını etkilemede kilit rol oynar. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model`   | MODEL     | Çıktı, doğrusal CFG kılavuz ölçeği uygulanmış giriş modelinin değiştirilmiş bir versiyonudur. Bu ayarlanmış model, belirtilen kılavuz ölçeğine dayalı olarak değişen derecelerde koşullandırmaya sahip çıktılar üretebilir. |