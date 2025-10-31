> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskComposite/tr.md)

Bu düğüm, iki maske girdisini toplama, çıkarma ve mantıksal işlemler gibi çeşitli operasyonlarla birleştirerek yeni, değiştirilmiş bir maske oluşturmada uzmanlaşmıştır. Karmaşık maskeleme efektleri elde etmek için maske verilerinin manipülasyonunu soyut bir şekilde ele alır ve maske tabanlı görüntü düzenleme ve işleme iş akışlarında çok önemli bir bileşen olarak hizmet eder.

## Girdiler

| Parametre    | Veri Türü | Açıklama                                                                                                                                      |
| ------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `destination`| MASK        | Kaynak maskesiyle yapılan işleme bağlı olarak değiştirilecek olan birincil maske. Değişiklikler için temel oluşturarak kompozit işlemde merkezi bir rol oynar. |
| `source`     | MASK        | Hedef maskesiyle birlikte belirtilen işlemi gerçekleştirmek ve nihai çıktı maskesini etkilemek için kullanılacak ikincil maske. |
| `x`          | INT         | Kaynak maskesinin hedef maskesine uygulanacağı yatay ofset. Kompozit sonucun konumlandırmasını etkiler.       |
| `y`          | INT         | Kaynak maskesinin hedef maskesine uygulanacağı dikey ofset. Kompozit sonucun konumlandırmasını etkiler.         |
| `operation`  | COMBO[STRING]| Hedef ve kaynak maskeleri arasında uygulanacak işlem türünü belirtir ('add', 'subtract' veya mantıksal işlemler gibi). Kompozit efektin doğasını belirler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama                                                                 |
| --------- | ------------ | ---------------------------------------------------------------------------- |
| `mask`    | MASK        | Hedef ve kaynak maskeleri arasında belirtilen işlem uygulandıktan sonra elde edilen ve kompozit sonucu temsil eden maske. |