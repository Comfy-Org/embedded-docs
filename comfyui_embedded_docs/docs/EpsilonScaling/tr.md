> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/tr.md)

Araştırma makalesi "Elucidating the Exposure Bias in Diffusion Models"dan Epsilon Ölçeklendirme yöntemini uygular. Bu yöntem, örnekleme sürecinde tahmin edilen gürültüyü ölçeklendirerek örnek kalitesini iyileştirir. Yayılım modellerindeki maruz kalma yanlılığını azaltmak için tekdüzen bir program kullanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Epsilon ölçeklendirmenin uygulanacağı model |
| `scaling_factor` | FLOAT | Hayır | 0.5 - 1.5 | Tahmin edilen gürültüyü ölçeklendirmek için kullanılan faktör (varsayılan: 1.005) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Epsilon ölçeklendirme uygulanmış model |