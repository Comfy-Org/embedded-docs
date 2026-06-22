# Ses Ses Seviyesi Ayarla

Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/en.md)

AudioAdjustVolume düğümü, desibel (dB) cinsinden ses seviyesi ayarlamaları uygulayarak sesin yüksekliğini değiştirir. Bir ses girişi alır ve belirtilen ses seviyesine göre bir kazanç faktörü uygular; burada pozitif değerler sesi artırır, negatif değerler ise azaltır. Düğüm, orijinaliyle aynı örnekleme hızına sahip değiştirilmiş sesi döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ses` | İşlenecek ses girişi | AUDIO | Evet | - |
| `volume` | Desibel (dB) cinsinden ses seviyesi ayarı. 0 = değişiklik yok, +6 = iki katı, -6 = yarısı, vb. (varsayılan: 1) | INT | Evet | -100 ila 100 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `ses` | Ses seviyesi ayarlanmış işlenmiş ses | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/tr.md)

---
**Source fingerprint (SHA-256):** `0436765680671551239f7a89b575cdfb22590fbe662bdfe5da01bd1cd5c496ed`
