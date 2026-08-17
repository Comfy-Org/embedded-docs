# RastgeleGürültü

RandomNoise düğümü, bir tohum (seed) değerine dayalı olarak rastgele gürültü desenleri üretir. Çeşitli görüntü işleme ve üretim görevlerinde kullanılabilen yeniden üretilebilir gürültü oluşturur. Aynı tohum değeri her zaman aynı gürültü desenini üretir ve birden fazla çalıştırmada tutarlı sonuçlar elde edilmesini sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `noise_seed` | Rastgele gürültü desenini üretmek için kullanılan tohum değeri (varsayılan: 0). Aynı tohum değeri her zaman aynı gürültü çıktısını üretir. Üretim sonrası kontrol etkinleştirilmiştir; bu sayede tohum değeri her üretimden sonra rastgeleleştirilebilir, sabitlenebilir, artırılabilir veya azaltılabilir. | INT | Evet | 0 ila 18446744073709551615 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `noise` | Sağlanan tohum değerine dayalı olarak üretilen rastgele gürültü deseni. | NOISE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/tr.md)

---
**Source fingerprint (SHA-256):** `b55ff98c636c55f064ede82c6848ffa163d1fd9b0cf6195f4a35603cfbe2bc1e`
