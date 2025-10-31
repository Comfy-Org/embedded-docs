> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/tr.md)

RenormCFG düğümü, yayılım modellerinde sınıflandırıcısız kılavuzluk (CFG) sürecini, koşullu ölçeklendirme ve normalleştirme uygulayarak değiştirir. Görüntü oluşturma sırasında koşullu ve koşulsuz tahminlerin etkisini kontrol etmek için, belirtilen zaman adımı eşikleri ve yeniden normalleştirme faktörlerine dayalı olarak gürültü giderme işlemini ayarlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Yeniden normalleştirilmiş CFG uygulanacak yayılım modeli |
| `cfg_kesme` | FLOAT | Hayır | 0.0 - 100.0 | CFG ölçeklendirmesinin uygulanacağı zaman adımı eşiği (varsayılan: 100.0) |
| `yenidenorm_cfg` | FLOAT | Hayır | 0.0 - 100.0 | Koşullu kılavuzluk gücünü kontrol etmek için yeniden normalleştirme faktörü (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Yeniden normalleştirilmiş CFG işlevi uygulanmış değiştirilmiş model |