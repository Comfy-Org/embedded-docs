> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/tr.md)

ModelPatchLoader düğümü, model_patches klasöründen özelleştirilmiş model yamalarını yükler. Yama dosyasının türünü otomatik olarak algılar ve uygun model mimarisini yükler, ardından iş akışında kullanılmak üzere bir ModelPatcher içine sarar. Bu düğüm, controlnet blokları, özellik gömücü modeller ve diğer özel mimariler dahil olmak üzere farklı yama türlerini destekler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `name` | STRING | Evet | model_patches klasöründeki tüm mevcut model yama dosyaları | model_patches dizininden yüklenecek model yamasının dosya adı |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `MODEL_PATCH` | MODEL_PATCH | İş akışında kullanılmak üzere bir ModelPatcher içine sarılmış yüklenen model yaması |

---
**Source fingerprint (SHA-256):** `e394e165cf416019ed53d9fde42d97c3c9b9f9afd843b12371a624467a4841bf`
