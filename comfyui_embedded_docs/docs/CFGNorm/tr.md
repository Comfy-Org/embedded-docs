# CFGNorm

CFGNorm düğümü, yayılım modellerinde sınıflandırıcısız yönlendirme (CFG) sürecine bir normalizasyon tekniği uygular. Koşullu ve koşulsuz çıktıların normlarını karşılaştırarak gürültü giderme tahmininin ölçeğini ayarlar ve ardından etkiyi kontrol etmek için bir güç çarpanı uygular. Bu, yönlendirme ölçeklemesinde aşırı değerleri önleyerek üretim sürecini dengelemeye yardımcı olur.

## Girişler

| Parametre | Açıklama | Veri Türü | Giriş Türü | Varsayılan | Aralık |
| --- | --- | --- | --- | --- | --- |
| `model` | CFG normalizasyonunun uygulanacağı yayılım modeli | MODEL | zorunlu | - | - |
| `güç` | CFG ölçeklemesine uygulanan normalizasyon etkisinin yoğunluğunu kontrol eder | FLOAT | zorunlu | 1.0 | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `patched_model` | Örnekleme sürecine CFG normalizasyonu uygulanmış değiştirilmiş modeli döndürür | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/tr.md)

---
**Source fingerprint (SHA-256):** `af9e5f965500b959ff46f781e9329524fc0a4b94af2ce6d74116fe27b0e9005e`
