> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscale/tr.md)

LatentUpscale düğümü, görüntülerin gizli temsillerini (latent representations) büyütmek (upscale) için tasarlanmıştır. Gizli görüntülerin çözünürlüğünü artırırken, çıktı görüntüsünün boyutlarını ve büyütme yöntemini ayarlama esnekliği sağlar.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `örnekler` | `LATENT`    | Büyütülecek görüntünün gizli temsili. Bu parametre, büyütme işleminin başlangıç noktasını belirlemek için çok önemlidir. |
| `büyütme_yöntemi` | COMBO[STRING] | Gizli görüntüyü büyütmek için kullanılacak yöntemi belirtir. Farklı yöntemler, büyütülmüş görüntünün kalitesini ve özelliklerini etkileyebilir. |
| `genişlik`   | `INT`       | Büyütülmüş görüntünün istenen genişliği. 0 olarak ayarlanırsa, en-boy oranını korumak için yüksekliğe dayalı olarak hesaplanacaktır. |
| `yükseklik`  | `INT`       | Büyütülmüş görüntünün istenen yüksekliği. 0 olarak ayarlanırsa, en-boy oranını korumak için genişliğe dayalı olarak hesaplanacaktır. |
| `kırp`    | COMBO[STRING] | Büyütülmüş görüntünün nasıl kırpılacağını (crop) belirler; bu, çıktının nihai görünümünü ve boyutlarını etkiler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Daha fazla işlemeye veya oluşturmaya (generation) hazır olan, büyütülmüş gizli görüntü temsili. |