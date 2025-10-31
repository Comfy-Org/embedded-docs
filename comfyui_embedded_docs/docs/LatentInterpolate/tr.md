> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentInterpolate/tr.md)

LatentInterpolate düğümü, belirli bir orana dayalı olarak iki gizli örnek seti arasında enterpolasyon gerçekleştirmek üzere tasarlanmıştır ve her iki setin özelliklerini harmanlayarak yeni, ara bir gizli örnek seti oluşturur.

## Girdiler

| Parametre   | Veri Türü   | Açıklama |
|-------------|-------------|-------------|
| `örnekler1`  | `LATENT`    | Enterpolasyon işlemi için kullanılacak ilk gizli örnek setidir. Enterpolasyon sürecinin başlangıç noktasını oluşturur. |
| `örnekler2`  | `LATENT`    | Enterpolasyon işlemi için kullanılacak ikinci gizli örnek setidir. Enterpolasyon sürecinin bitiş noktasını oluşturur. |
| `oran`     | `FLOAT`     | Enterpole edilmiş çıktıda her örnek setinin ağırlığını belirleyen bir kayan nokta değeridir. 0 oranı ilk setin bir kopyasını üretirken, 1 oranı ikinci setin bir kopyasını üretir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, belirtilen orana dayalı olarak iki girdi seti arasında enterpole edilmiş bir durumu temsil eden yeni bir gizli örnek setidir. |