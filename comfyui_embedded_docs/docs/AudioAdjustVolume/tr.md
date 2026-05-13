> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/tr.md)

Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/en.md)

AudioAdjustVolume düğümü, desibel (dB) cinsinden ses seviyesi ayarlamaları uygulayarak sesin yüksekliğini değiştirir. Bir ses girişi alır ve belirtilen ses seviyesine göre bir kazanç faktörü uygular; burada pozitif değerler sesi artırır, negatif değerler ise azaltır. Düğüm, orijinaliyle aynı örnekleme hızına sahip değiştirilmiş sesi döndürür.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `ses` | AUDIO | Evet | - | İşlenecek ses girişi |
| `volume` | INT | Evet | -100 ila 100 | Desibel (dB) cinsinden ses seviyesi ayarı. 0 = değişiklik yok, +6 = iki katı, -6 = yarısı, vb. (varsayılan: 1) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `ses` | AUDIO | Ses seviyesi ayarlanmış işlenmiş ses |

---
**Source fingerprint (SHA-256):** `0436765680671551239f7a89b575cdfb22590fbe662bdfe5da01bd1cd5c496ed`
