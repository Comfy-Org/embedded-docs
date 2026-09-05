# SenseNovaSamplingOptions

SenseNova Sampling Options, bir modelde SenseNova akış kaydırmasını (flow shift) ayarlar. Girdi modelini kopyalar, seçilen akış kaydırma değerini kullanarak bir SenseNova model örnekleme yapılandırması ekler ve örnekleme sırasında kullanılmak üzere yamalanmış modeli döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | SenseNova akış kaydırma örnekleme yapılandırmasının uygulandığı model. | MODEL | Evet | - |
| `shift` | SenseNova model örneklemesinde ayarlanacak akış kaydırma değeri (varsayılan: 3.0; arayüz adımı: 0.01). | FLOAT | Evet | Minimum veya maksimum tanımlanmamıştır |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MODEL` | Örnekleme yapılandırmasına SenseNova akış kaydırması uygulanmış girdi modelinin bir kopyası. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaSamplingOptions/tr.md)

---
**Source fingerprint (SHA-256):** `b0dea4a5c226bccb54bb1d70e8ea2791a645018853571429c556034351e9e75a`
