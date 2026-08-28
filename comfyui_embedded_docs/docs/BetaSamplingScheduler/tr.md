# BetaÖrneklemeZamanlayıcısı

BetaSamplingScheduler düğümü, beta zamanlama algoritmasını kullanarak örnekleme süreci için bir dizi gürültü seviyesi (sigma) üretir. Görüntü üretimi sırasında gürültü giderme sürecini kontrol eden özelleştirilmiş bir gürültü zamanlaması oluşturmak için bir model ve yapılandırma parametreleri alır. Bu zamanlayıcı, alfa ve beta parametreleri aracılığıyla gürültü azaltma yörüngesinin ince ayarını yapmayı sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme için kullanılan ve model örnekleme nesnesini sağlayan model | MODEL | Evet | - |
| `adımlar` | Sigma üretilecek örnekleme adım sayısı (varsayılan: 20) | INT | Evet | 1 ile 10000 |
| `alfa` | Beta zamanlayıcı için alfa parametresi, zamanlama eğrisini kontrol eder (varsayılan: 0.6, gelişmiş parametre) | FLOAT | Evet | 0.0 ile 50.0 |
| `beta` | Beta zamanlayıcı için beta parametresi, zamanlama eğrisini kontrol eder (varsayılan: 0.6, gelişmiş parametre) | FLOAT | Evet | 0.0 ile 50.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `SIGMAS` | Örnekleme sürecinde kullanılan bir dizi gürültü seviyesi (sigma) | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `80adae3cbedff7fe544a1fbcf638af7965f1216e422931063ecf67da53ddff95`
