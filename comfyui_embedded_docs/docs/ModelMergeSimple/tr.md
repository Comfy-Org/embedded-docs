> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSimple/tr.md)

ModelMergeSimple düğümü, iki modelin parametrelerini belirli bir orana göre harmanlayarak birleştirmek için tasarlanmıştır. Bu düğüm, her iki giriş modelinin güçlü yönlerini veya karakteristik özelliklerini birleştiren melez modellerin oluşturulmasını kolaylaştırır.

`ratio` parametresi, iki model arasındaki harmanlama oranını belirler. Bu değer 1 olduğunda, çıktı modeli %100 `model1` olur ve bu değer 0 olduğunda, çıktı modeli %100 `model2` olur.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model1`  | `MODEL`     | Birleştirilecek ilk model. İkinci modelden alınan yamaların uygulandığı temel model olarak hizmet eder. |
| `model2`  | `MODEL`     | Yamaları, belirtilen orandan etkilenerek ilk modelin üzerine uygulanan ikinci model. |
| `oran`   | `FLOAT`     | Bu değer 1 olduğunda, çıktı modeli %100 `model1` olur ve bu değer 0 olduğunda, çıktı modeli %100 `model2` olur. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model`   | MODEL     | Belirtilen orana göre her iki giriş modelinden unsurlar içeren, ortaya çıkan birleştirilmiş model. |