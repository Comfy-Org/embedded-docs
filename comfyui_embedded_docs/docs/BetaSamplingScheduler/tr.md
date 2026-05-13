> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/tr.md)

BetaSamplingScheduler düğümü, beta zamanlama algoritmasını kullanarak örnekleme süreci için bir dizi gürültü seviyesi (sigma) oluşturur. Bir model ve yapılandırma parametreleri alarak, görüntü oluşturma sırasında gürültü giderme sürecini kontrol eden özelleştirilmiş bir gürültü zamanlaması oluşturur. Bu zamanlayıcı, alfa ve beta parametreleri aracılığıyla gürültü azaltma yörüngesinin ince ayarını yapmaya olanak tanır.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | MODEL | Evet | - | Örnekleme için kullanılan ve model örnekleme nesnesini sağlayan model |
| `steps` | INT | Evet | 1 ila 10000 | Sigma değerlerinin oluşturulacağı örnekleme adım sayısı (varsayılan: 20) |
| `alpha` | FLOAT | Evet | 0.0 ila 50.0 | Beta zamanlayıcı için alfa parametresi, zamanlama eğrisini kontrol eder (varsayılan: 0.6) |
| `beta` | FLOAT | Evet | 0.0 ila 50.0 | Beta zamanlayıcı için beta parametresi, zamanlama eğrisini kontrol eder (varsayılan: 0.6) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `SIGMAS` | SIGMAS | Örnekleme sürecinde kullanılan bir dizi gürültü seviyesi (sigma) |

---
**Source fingerprint (SHA-256):** `8b3d17ef737107da3d5cacc84278de8a93f6889e6567619012729b205bbc421e`
