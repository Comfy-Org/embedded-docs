BetaSamplingScheduler düğümü, beta zamanlama algoritmasını kullanarak örnekleme süreci için bir dizi gürültü seviyesi (sigma) oluşturur. Bir model ve yapılandırma parametreleri alarak, görüntü oluşturma sırasında gürültü giderme sürecini kontrol eden özelleştirilmiş bir gürültü zamanlaması oluşturur. Bu zamanlayıcı, alfa ve beta parametreleri aracılığıyla gürültü azaltma yörüngesinin ince ayarını yapmaya olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme için kullanılan ve model örnekleme nesnesini sağlayan model | MODEL | Evet | - |
| `adımlar` | Sigma değerlerinin oluşturulacağı örnekleme adım sayısı (varsayılan: 20) | INT | Evet | 1 ila 10000 |
| `alfa` | Beta zamanlayıcı için alfa parametresi, zamanlama eğrisini kontrol eder (varsayılan: 0.6) | FLOAT | Evet | 0.0 ila 50.0 |
| `beta` | Beta zamanlayıcı için beta parametresi, zamanlama eğrisini kontrol eder (varsayılan: 0.6) | FLOAT | Evet | 0.0 ila 50.0 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `SIGMAS` | Örnekleme sürecinde kullanılan bir dizi gürültü seviyesi (sigma) | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `8b3d17ef737107da3d5cacc84278de8a93f6889e6567619012729b205bbc421e`
