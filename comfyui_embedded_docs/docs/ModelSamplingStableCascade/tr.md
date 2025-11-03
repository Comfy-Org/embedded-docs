> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/tr.md)

**ModelSamplingStableCascade** düğümü, bir modele kararlı kademeli örnekleme uygular ve örnekleme parametrelerini bir kaydırma değeri ile ayarlar. Girdi modelinin, kararlı kademeli üretim için özel örnekleme yapılandırmasına sahip değiştirilmiş bir versiyonunu oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Kararlı kademeli örneklemenin uygulanacağı girdi modeli |
| `kaydırma` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme parametrelerine uygulanacak kaydırma değeri (varsayılan: 2.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Kararlı kademeli örnekleme uygulanmış değiştirilmiş model |