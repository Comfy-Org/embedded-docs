ThresholdMask düğümü, bir eşik değeri uygulayarak maskeyi ikili (binary) maskeye dönüştürür. Giriş maskesindeki her pikseli belirtilen eşik değeriyle karşılaştırır ve eşiğin üzerindeki piksellerin 1 (beyaz), eşiğe eşit veya altındaki piksellerin 0 (siyah) olduğu yeni bir maske oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `maske` | İşlenecek giriş maskesi | MASK | Evet | - |
| `değer` | İkili hale getirme için eşik değeri (varsayılan: 0.5) | FLOAT | Evet | 0.0 - 1.0 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `maske` | Eşikleme sonrası elde edilen ikili maske | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ThresholdMask/tr.md)

---
**Source fingerprint (SHA-256):** `5c61433c05ef8106d928306b64035078e7598605512f20aaf992255f7b166456`
