LatentFlip düğümü, gizli temsilleri dikey veya yatay olarak çevirerek manipüle etmek için tasarlanmıştır. Bu işlem, gizli uzayın dönüştürülmesine olanak tanıyarak veri içinde yeni varyasyonlar veya perspektifler ortaya çıkarabilir.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `örnekler` | 'samples' parametresi, çevrilecek gizli temsilleri temsil eder. Çevirme işlemi, 'flip_method' parametresine bağlı olarak bu temsilleri dikey veya yatay olarak değiştirir, böylece gizli uzaydaki veriyi dönüştürür. | `LATENT` |
| `çevirme_yöntemi` | 'flip_method' parametresi, gizli örneklerin hangi eksen boyunca çevrileceğini belirtir. 'x-axis: vertically' (x ekseni: dikey) veya 'y-axis: horizontally' (y ekseni: yatay) değerlerini alabilir, çevirme yönünü ve dolayısıyla gizli temsillere uygulanan dönüşümün doğasını belirler. | COMBO[STRING] |

## Çıkışlar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Çıktı, belirtilen yönteme göre çevrilmiş, girdi gizli temsillerinin değiştirilmiş bir sürümüdür. Bu dönüşüm, gizli uzayda yeni varyasyonlar ortaya çıkarabilir. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFlip/tr.md)
