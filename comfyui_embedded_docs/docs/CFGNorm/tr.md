> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/tr.md)

CFGNorm düğümü, yayılım modellerinde sınıflandırıcısız kılavuzluk (CFG) sürecine bir normalleştirme tekniği uygular. Koşullu ve koşulsuz çıktıların normlarını karşılaştırarak gürültüsü giderilmiş tahminin ölçeğini ayarlar ve ardından etkiyi kontrol etmek için bir güç çarpanı uygular. Bu, kılavuzluk ölçeklendirmesindeki aşırı değerleri önleyerek üretim sürecini stabilize etmeye yardımcı olur.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | gerekli | - | - | CFG normalleştirmesinin uygulanacağı yayılım modeli |
| `strength` | FLOAT | gerekli | 1.0 | 0.0 - 100.0 | CFG ölçeklendirmesine uygulanan normalleştirme etkisinin yoğunluğunu kontrol eder |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `patched_model` | MODEL | Örnekleme sürecine CFG normalleştirmesi uygulanmış olarak değiştirilmiş modeli döndürür |