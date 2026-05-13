> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DifferentialDiffusion/tr.md)

Diferansiyel Difüzyon düğümü, zaman adımı eşiklerine dayalı ikili bir maske uygulayarak gürültü giderme sürecini değiştirir. Orijinal gürültü giderme maskesi ile eşik tabanlı ikili maske arasında geçiş yapan bir maske oluşturarak difüzyon süreci gücünün kontrollü bir şekilde ayarlanmasını sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Değiştirilecek difüzyon modeli |
| `güç` | FLOAT | Hayır | 0.0 - 1.0 | Orijinal gürültü giderme maskesi ile ikili eşik maskesi arasındaki geçiş gücünü kontrol eder (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Güncellenmiş gürültü giderme maskesi işlevine sahip değiştirilmiş difüzyon modeli |

---
**Source fingerprint (SHA-256):** `3b1727baa6c546516f5dfb53e6e39f27fc7429cde2ac7fd7dfbab99eebb39816`
