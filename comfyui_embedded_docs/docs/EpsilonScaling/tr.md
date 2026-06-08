"Elucidating the Exposure Bias in Diffusion Models" araştırma makalesindeki Epsilon Ölçekleme yöntemini uygular. Bu yöntem, örnekleme süreci sırasında tahmin edilen gürültüyü ölçeklendirerek örnek kalitesini artırır. Difüzyon modellerindeki maruz kalma yanlılığını azaltmak için tekdüze bir program kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Epsilon ölçeklemenin uygulanacağı model | MODEL | Evet | - |
| `scaling_factor` | Tahmin edilen gürültüyü ölçeklendirmek için kullanılan faktör (varsayılan: 1.005) | FLOAT | Hayır | 0.5 - 1.5 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Epsilon ölçekleme uygulanmış model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/tr.md)
