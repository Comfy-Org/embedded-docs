> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ThresholdMask/tr.md)

ThresholdMask düğümü, bir eşik değeri uygulayarak maskeyi ikili (binary) maskeye dönüştürür. Giriş maskesindeki her pikseli belirtilen eşik değeriyle karşılaştırır ve eşiğin üzerindeki piksellerin 1 (beyaz), eşiğe eşit veya altındaki piksellerin 0 (siyah) olduğu yeni bir maske oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `maske` | MASK | Evet | - | İşlenecek giriş maskesi |
| `değer` | FLOAT | Evet | 0.0 - 1.0 | İkili hale getirme için eşik değeri (varsayılan: 0.5) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `maske` | MASK | Eşikleme sonrası elde edilen ikili maske |

---
**Source fingerprint (SHA-256):** `5c61433c05ef8106d928306b64035078e7598605512f20aaf992255f7b166456`
