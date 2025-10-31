> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFlip/tr.md)

LatentFlip düğümü, gizli temsilleri dikey veya yatay olarak çevirmek için tasarlanmıştır. Bu işlem, gizli uzayda dönüşüm sağlayarak veri içinde yeni varyasyonlar veya perspektifler ortaya çıkarabilir.

## Girdiler

| Parametre     | Veri Tipi    | Açıklama |
|---------------|--------------|-------------|
| `samples`     | `LATENT`     | 'samples' parametresi, çevrilecek gizli temsilleri temsil eder. Çevirme işlemi, bu temsilleri 'flip_method' parametresine bağlı olarak dikey veya yatay olarak değiştirir ve böylece gizli uzaydaki veriyi dönüştürür. |
| `flip_method` | COMBO[STRING] | 'flip_method' parametresi, gizli örneklerin hangi eksen boyunca çevrileceğini belirtir. Bu, 'x-axis: vertically' (dikey) veya 'y-axis: horizontally' (yatay) olabilir ve çevirme yönünü, dolayısıyla gizli temsillere uygulanan dönüşümün doğasını belirler. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, girdi olarak verilen gizli temsillerin belirtilen yönteme göre çevrilmiş halidir. Bu dönüşüm, gizli uzay içinde yeni varyasyonlar oluşturabilir. |