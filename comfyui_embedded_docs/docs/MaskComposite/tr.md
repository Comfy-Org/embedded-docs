> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskComposite/tr.md)

Bu düğüm, toplama, çıkarma ve mantıksal işlemler gibi çeşitli işlemler aracılığıyla iki maske girdisini birleştirerek yeni, değiştirilmiş bir maske üretme konusunda uzmanlaşmıştır. Karmaşık maskeleme efektleri elde etmek için maske verilerinin manipülasyonunu soyut bir şekilde ele alır ve maske tabanlı görüntü düzenleme ve işleme iş akışlarında önemli bir bileşen olarak hizmet eder.

## Girişler

| Parametre    | Veri Türü | Açıklama                                                                                                                                      |
| ------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `hedef`| MASK        | Kaynak maske ile yapılacak işleme bağlı olarak değiştirilecek olan birincil maske. Bileşik işlemde merkezi bir rol oynar ve değişiklikler için temel görevi görür. |
| `kaynak`     | MASK        | Hedef maske ile birlikte belirtilen işlemi gerçekleştirmek için kullanılacak olan ikincil maske. Nihai çıktı maskesini etkiler. |
| `x`          | INT         | Kaynak maskenin hedef maskeye uygulanacağı yatay konum kayması. Bileşik sonucun konumlandırılmasını etkiler.       |
| `y`          | INT         | Kaynak maskenin hedef maskeye uygulanacağı dikey konum kayması. Bileşik sonucun konumlandırılmasını etkiler.         |
| `işlem`  | COMBO[STRING]| Hedef ve kaynak maskeler arasında uygulanacak işlemin türünü belirtir. 'toplama', 'çıkarma' veya mantıksal işlemler gibi seçenekler, bileşik efektin doğasını belirler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama                                                                 |
| --------- | ------------ | ---------------------------------------------------------------------------- |
| `mask`    | MASK        | Hedef ve kaynak maskeler arasında belirtilen işlem uygulandıktan sonra elde edilen sonuç maskesi. Bileşik sonucu temsil eder. |