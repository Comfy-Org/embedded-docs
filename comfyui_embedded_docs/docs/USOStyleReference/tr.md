# USOTarzReferansı

USOStyleReference düğümü, bir referans görüntüsündeki stil bilgisini bir Flux modeline uygular. CLIP vision çıktısından bir stil yerleştirmesi oluşturur ve modelin bir kopyasına yama uygular; böylece üretim sırasında stil yerleştirmesi, metin istemi koşullandırmasının önüne eklenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Stil referansı yamasının uygulanacağı temel model | MODEL | Evet | - |
| `model_patch` | Stil referansı bilgisini içeren model yaması | MODEL_PATCH | Evet | - |
| `clip_vision_output` | CLIP vision işleminden çıkarılan kodlanmış görsel özellikler. Düğüm, -20 ve -11 katmanlarındaki gizli durumları sondan bir önceki gizli durumlarla birleştirerek stil yerleştirmesini oluşturur | CLIP_VISION_OUTPUT | Evet | - |

Not: Üç girdinin tümü zorunludur. Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Uygulanmış stil referansı yamasıyla değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/tr.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
