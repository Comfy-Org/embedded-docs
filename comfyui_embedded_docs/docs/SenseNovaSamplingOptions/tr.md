# SenseNova Örnekleme Seçenekleri

SenseNova Sampling Options, bir model üzerinde SenseNova flow shift değerini ayarlar. Girdi modelini klonlar, seçilen flow shift değerini kullanarak bir SenseNova model örnekleme yapılandırması ekler ve örnekleme sırasında kullanılmak üzere yamalanmış modeli döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | SenseNova flow shift örnekleme yapılandırmasının uygulanacağı model. | MODEL | Evet | - |
| `shift` | SenseNova model örneklemesinde ayarlanacak flow shift değeri (varsayılan: 3.0; arayüz adımı: 0.01). | FLOAT | Evet | Tanımlanmış minimum veya maksimum yok |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MODEL` | Örnekleme yapılandırmasına SenseNova flow shift uygulanmış girdi modelinin bir klonu. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaSamplingOptions/tr.md)

---
**Source fingerprint (SHA-256):** `b0dea4a5c226bccb54bb1d70e8ea2791a645018853571429c556034351e9e75a`
