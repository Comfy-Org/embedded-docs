> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/tr.md)

USOStyleReference düğümü, CLIP görüntü çıktısından elde edilen kodlanmış görüntü özelliklerini kullanarak modellere stil referans yamaları uygular. Görsel girdilerden çıkarılan stil bilgilerini dahil ederek girdi modelinin değiştirilmiş bir versiyonunu oluşturur ve stil aktarımı veya referans tabanlı üretim yetenekleri sağlar.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Stil referans yamasının uygulanacağı temel model |
| `model_patch` | MODEL_PATCH | Evet | - | Stil referans bilgilerini içeren model yaması |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Evet | - | CLIP görüntü işlemeden çıkarılan kodlanmış görsel özellikler |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Uygulanmış stil referans yamalarına sahip değiştirilmiş model |