# ModelPatchLoader

ModelPatchLoader düğümü, model_patches klasöründen özel model patch dosyalarını yükler. Patch türünü dosya içeriğinden otomatik olarak algılar ve ilgili model mimarisini yükler, ardından iş akışında kullanılmak üzere bir ModelPatcher içine sarar. Bu düğüm; controlnet blokları, feature embedder modelleri ve diğer özel mimariler dahil olmak üzere farklı patch türlerini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ad` | model_patches dizininden yüklenecek model patch dosyasının adı | STRING | Evet | model_patches klasöründeki tüm mevcut model patch dosyaları |

Not: Bu düğüm deneysel olarak işaretlenmiştir. Patch türü dosya içeriğinden otomatik olarak algılandığından, manuel tür seçimi gerekmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL_PATCH` | İş akışında kullanılmak üzere bir ModelPatcher içine sarılmış yüklenmiş model patch | MODEL_PATCH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/tr.md)

---
**Source fingerprint (SHA-256):** `7f5225521b82b39b85183ccc7957fc4172e64aed9289f66d53969ea4a2e81b7f`
