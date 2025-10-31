> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/tr.md)

ModelPatchLoader düğümü, model_patches klasöründen özelleştirilmiş model yamalarını yükler. Yamalama dosyasının türünü otomatik olarak algılar ve uygun model mimarisini yükleyerek, iş akışında kullanılmak üzere bir ModelPatcher içine sarar. Bu düğüm, controlnet blokları ve feature embedder modelleri dahil olmak üzere farklı yama türlerini destekler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `name` | STRING | Evet | model_patches klasöründeki tüm mevcut model yama dosyaları | model_patches dizininden yüklenecek model yamasının dosya adı |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `MODEL_PATCH` | MODEL_PATCH | İş akışında kullanılmak üzere ModelPatcher içine sarılmış yüklenmiş model yaması |