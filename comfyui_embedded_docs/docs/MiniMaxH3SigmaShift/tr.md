# MiniMax H3 Sigma Shift

MiniMax H3 modeli için video ve ses akış kaydırma değerlerini ayarlar. Video kaydırma, örnekleyicinin sigma çizelgesini kontrol eder ve her iki kaydırma değeri modelin dahili transformer'ına iletilir; transformer, ortak temel ızgaradan ses çizelgesini türetmek için bu değerleri kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Sigma kaydırma yamasının uygulanacağı model. Düğüm modeli kopyalar, böylece orijinal model değişmeden kalır. | MODEL | Evet | - |
| `video_kaydır` | Video akış kaydırma değeri. Örnekleyicinin sigma çizelgesini belirler. Varsayılan: 12.0. | FLOAT | Evet | 0.01 to 100.0 |
| `ses_kaydır` | Ses akış kaydırma değeri. Model tarafından ses çizelgesini türetmek için kullanılır. Varsayılan: 3.0. | FLOAT | Evet | 0.01 to 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MODEL` | Video ve ses sigma kaydırma ayarları uygulanmış kopyalanmış model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3SigmaShift/tr.md)

---
**Source fingerprint (SHA-256):** `0f731585cc1a9c87a3e54341757c4cf4e490d1d4718ecf458bd2b9f4378af63f`
