# ModelPatchLoader

ModelPatchLoader düğümü, model_patches klasöründeki özel model yamalarını yükler. Dosya türünü otomatik olarak algılar ve uygun model mimarisini yükler, ardından iş akışında kullanılmak üzere bir ModelPatcher içine sarar. Bu düğüm; controlnet blokları, öznitelik gömme (feature embedder) modelleri ve diğer özel mimariler dahil olmak üzere farklı yama türlerini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `name` | model_patches dizininden yüklenecek model yamasının dosya adı | STRING | Evet | model_patches klasöründeki mevcut tüm model yama dosyaları |

Not: Bu düğüm ComfyUI'de deneysel olarak işaretlenmiştir. Yama türü dosya içeriğinden otomatik olarak algılanır, bu nedenle tek bir düğüm birden fazla yama türünü işleyebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL_PATCH` | İş akışında kullanılmak üzere bir ModelPatcher içine sarılmış yüklenmiş model yaması | MODEL_PATCH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/tr.md)

---
**Source fingerprint (SHA-256):** `7f5225521b82b39b85183ccc7957fc4172e64aed9289f66d53969ea4a2e81b7f`
