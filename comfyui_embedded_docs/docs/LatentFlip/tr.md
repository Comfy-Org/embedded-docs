> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFlip/tr.md)

LatentFlip düğümü, gizli temsilleri dikey veya yatay olarak çevirerek manipüle etmek için tasarlanmıştır. Bu işlem, gizli uzayın dönüştürülmesine olanak tanıyarak veri içinde yeni varyasyonlar veya perspektifler ortaya çıkarabilir.

## Girişler

| Parametre      | Veri Türü      | Açıklama |
|----------------|----------------|-------------|
| `örnekler`      | `LATENT`       | 'samples' parametresi, çevrilecek gizli temsilleri temsil eder. Çevirme işlemi, 'flip_method' parametresine bağlı olarak bu temsilleri dikey veya yatay olarak değiştirir, böylece gizli uzaydaki veriyi dönüştürür. |
| `çevirme_yöntemi`  | COMBO[STRING]  | 'flip_method' parametresi, gizli örneklerin hangi eksen boyunca çevrileceğini belirtir. 'x-axis: vertically' (x ekseni: dikey) veya 'y-axis: horizontally' (y ekseni: yatay) değerlerini alabilir, çevirme yönünü ve dolayısıyla gizli temsillere uygulanan dönüşümün doğasını belirler. |

## Çıkışlar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, belirtilen yönteme göre çevrilmiş, girdi gizli temsillerinin değiştirilmiş bir sürümüdür. Bu dönüşüm, gizli uzayda yeni varyasyonlar ortaya çıkarabilir. |