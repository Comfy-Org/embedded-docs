# RastgeleGürültü

The RandomNoise düğümü, örnekleme sürecinde kullanılmak üzere bir tohum değerine dayalı bir gürültü üreteci oluşturur. Aynı tohum her zaman aynı gürültü desenini üretir; bu da birden fazla çalıştırmada tutarlı ve tekrarlanabilir sonuçlar elde edilmesini sağlar. Örnekleyiciler, latent görüntüleri işlerken üretilen gürültüyü kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `gürültü_tohumu` | Rastgele gürültü desenini oluşturmak için kullanılan tohum değeri (varsayılan: 0). Aynı tohum her zaman aynı gürültü çıktısını üretir. Bu girdi, her üretimden sonra tohumu otomatik olarak güncellemek için bir üretim sonrası kontrol seçeneği içerir. | INT | Evet | 0 ila 18446744073709551615 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `noise` | Sağlanan tohum değerine göre latent örnekler için rastgele gürültü üreten bir gürültü nesnesi. Örnekleme sürecinde örnekleyiciler tarafından kullanılır. | NOISE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/tr.md)

---
**Source fingerprint (SHA-256):** `b55ff98c636c55f064ede82c6848ffa163d1fd9b0cf6195f4a35603cfbe2bc1e`
