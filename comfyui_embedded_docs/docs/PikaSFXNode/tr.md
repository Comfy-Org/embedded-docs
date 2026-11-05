# Pika SFX

Bu düğüm, Pika ile bir metin açıklamasından ses efekti üretir. Sesi ve ne kadar süreceğini tanımlayın; düğüm bir ses klibi döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `prompt` | Ses efektinin ne olması gerektiği. Boş olmamalıdır. Varsayılan: "" (boş dize). | STRING | Evet | 1 ile 4000 karakter arası |
| `duration` | Ses efektinin saniye cinsinden uzunluğu. Varsayılan: 5.0. | FLOAT | Evet | 1.0 ile 20.0 arası (adım: 0.1) |
| `seed` | Örnekleme için tohum. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `AUDIO` | Oluşturulan ses efekti. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaSFXNode/tr.md)

---
**Source fingerprint (SHA-256):** `a1dcd374d158009aceae2aecd87ed08f8105bff7db75160a99e8624be9459dfa`
