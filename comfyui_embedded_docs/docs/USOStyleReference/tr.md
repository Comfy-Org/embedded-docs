## Genel Bakış

USOStyleReference düğümü, CLIP görüntü işleme çıktısından alınan kodlanmış görüntü özniteliklerini kullanarak modellere stil referansı yamaları uygular. Görsel girdilerden çıkarılan stil bilgilerini modele entegre ederek, giriş modelinin değiştirilmiş bir sürümünü oluşturur ve stil aktarımı veya referans tabanlı üretim yetenekleri sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Stil referansı yamasının uygulanacağı temel model | MODEL | Evet | - |
| `model_yama` | Stil referansı bilgilerini içeren model yaması | MODEL_PATCH | Evet | - |
| `clip_vision_çıktısı` | CLIP görüntü işlemeden çıkarılan kodlanmış görsel öznitelikler | CLIP_VISION_OUTPUT | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Stil referansı yamaları uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/tr.md)

---
**Source fingerprint (SHA-256):** `fd800fb927677da29e148bfa1b287efed82895860ce4b0241d662579d2c07ff4`
