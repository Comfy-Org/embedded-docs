> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InpaintModelConditioning/tr.md)

InpaintModelConditioning düğümü, inpaint modelleri için koşullandırma sürecini kolaylaştırmak üzere tasarlanmış olup, çeşitli koşullandırma girdilerinin entegrasyonunu ve manipülasyonunu sağlayarak inpaint çıktısını özelleştirmeye olanak tanır. Belirli model kontrol noktalarını yüklemeden stil veya kontrol ağı modelleri uygulamaya, koşullandırma öğelerini kodlamadan birleştirmeye kadar geniş bir işlev yelpazesini kapsar ve böylece inpaint görevlerini özelleştirmek için kapsamlı bir araç görevi görür.

## Girdiler

| Parametre | Comfy türü        | Açıklama |
|-----------|--------------------|-------------|
| `pozitif`| `CONDITIONING`     | Inpaint modeline uygulanacak pozitif koşullandırma bilgisini veya parametrelerini temsil eder. Bu girdi, inpaint işleminin hangi bağlam veya kısıtlamalar altında gerçekleştirileceğini tanımlamak için çok önemli olup, nihai çıktıyı önemli ölçüde etkiler. |
| `negatif`| `CONDITIONING`     | Inpaint modeline uygulanacak negatif koşullandırma bilgisini veya parametrelerini temsil eder. Bu girdi, inpaint sürecinde kaçınılması gereken koşulları veya bağlamları belirtmek için temeldir ve böylece nihai çıktıyı etkiler. |
| `vae`     | `VAE`              | Koşullandırma sürecinde kullanılacak VAE modelini belirtir. Bu girdi, kullanılacak VAE modelinin belirli mimarisini ve parametrelerini belirlemek için çok önemlidir. |
| `pikseller`  | `IMAGE`            | İşlenecek görüntünün piksel verilerini temsil eder. Bu girdi, inpaint görevi için gerekli olan görsel bağlamı sağlamak açısından temeldir. |
| `maske`    | `MASK`             | Görüntüye uygulanacak ve inpaint yapılacak alanları gösteren maskeyi belirtir. Bu girdi, görüntü içinde inpaint gerektiren belirli bölgeleri tanımlamak için çok önemlidir. |

## Çıktılar

| Parametre | Veri Türü      | Açıklama |
|-----------|--------------|-------------|
| `negatif`| `CONDITIONING` | İşlendikten sonra değiştirilmiş pozitif koşullandırma bilgisi, inpaint modeline uygulanmaya hazırdır. Bu çıktı, belirtilen pozitif koşullara göre inpaint sürecini yönlendirmek için temeldir. |
| `gizli`| `CONDITIONING` | İşlendikten sonra değiştirilmiş negatif koşullandırma bilgisi, inpaint modeline uygulanmaya hazırdır. Bu çıktı, belirtilen negatif koşullara göre inpaint sürecini yönlendirmek için temeldir. |
| `latent`  | `LATENT`     | Koşullandırma sürecinden türetilen gizli temsildir. Bu çıktı, işlenmekte olan görüntünün altında yatan özellikleri ve karakteristikleri anlamak için çok önemlidir. |