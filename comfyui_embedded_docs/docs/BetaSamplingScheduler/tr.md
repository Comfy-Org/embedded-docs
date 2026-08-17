# BetaÖrneklemeZamanlayıcısı

BetaSamplingScheduler düğümü, görüntü üretiminde örnekleme süreci sırasında gürültünün nasıl kaldırılacağını kontrol eden bir dizi gürültü seviyesi (sigma) oluşturur. Bir beta zamanlama algoritması kullanır; `alpha` ve `beta` ayarları gürültü zamanlamasının şeklini ayarlar. Üretilen sigmalar, gürültü giderme sürecini yönlendirmek için bir örnekleyiciye iletilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme için kullanılan model; model örnekleme nesnesini sağlar. | MODEL | Evet | - |
| `steps` | Sigmaların oluşturulacağı örnekleme adımı sayısı (varsayılan: 20). | INT | Evet | 1 to 10000 |
| `alpha` | Beta zamanlayıcı için alfa parametresi; zamanlama eğrisini kontrol eder (varsayılan: 0.6). Gelişmiş parametre. | FLOAT | Evet | 0.0 to 50.0 |
| `beta` | Beta zamanlayıcı için beta parametresi; zamanlama eğrisini kontrol eder (varsayılan: 0.6). Gelişmiş parametre. | FLOAT | Evet | 0.0 to 50.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `SIGMAS` | Örnekleme süreci için kullanılan bir dizi gürültü seviyesi (sigma). | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `80adae3cbedff7fe544a1fbcf638af7965f1216e422931063ecf67da53ddff95`
