> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/tr.md)

"Elucidating the Exposure Bias in Diffusion Models" araştırma makalesindeki Epsilon Ölçekleme yöntemini uygular. Bu yöntem, örnekleme süreci sırasında tahmin edilen gürültüyü ölçeklendirerek örnek kalitesini artırır. Difüzyon modellerindeki maruz kalma yanlılığını azaltmak için tekdüze bir program kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Epsilon ölçeklemenin uygulanacağı model |
| `scaling_factor` | FLOAT | Hayır | 0.5 - 1.5 | Tahmin edilen gürültüyü ölçeklendirmek için kullanılan faktör (varsayılan: 1.005) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Epsilon ölçekleme uygulanmış model |