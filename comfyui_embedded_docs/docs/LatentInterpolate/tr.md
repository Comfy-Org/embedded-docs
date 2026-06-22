# GizliAraDeğerleme

LatentInterpolate düğümü, iki latent örnek kümesi arasında belirtilen bir orana göre enterpolasyon yaparak, her iki kümenin özelliklerini harmanlayan yeni, ara bir latent örnek kümesi oluşturmak için tasarlanmıştır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `örnekler1` | Enterpolasyon yapılacak ilk latent örnek kümesi. Enterpolasyon işlemi için başlangıç noktası görevi görür. | `LATENT` |
| `örnekler2` | Enterpolasyon yapılacak ikinci latent örnek kümesi. Enterpolasyon işlemi için bitiş noktası görevi görür. | `LATENT` |
| `oran` | Enterpolasyon çıktısında her bir örnek kümesinin ağırlığını belirleyen ondalık sayı değeri. 0 oranı, ilk kümenin bir kopyasını üretirken, 1 oranı ikinci kümenin bir kopyasını üretir. | `FLOAT` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Çıktı, belirtilen orana bağlı olarak iki giriş kümesi arasında enterpolasyon durumunu temsil eden yeni bir latent örnek kümesidir. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentInterpolate/tr.md)
