# Hunyuan3Dv2Koşullandırma

Hunyuan3Dv2Conditioning düğümü, 3D modeller için koşullandırma verileri oluşturmak üzere CLIP görüntü çıktısını işler. Görüntü çıktısından son gizli durum gömme vektörlerini çıkarır ve hem pozitif hem de negatif koşullandırma çiftleri oluşturur. Pozitif koşullandırma gerçek gömme vektörlerini kullanırken, negatif koşullandırma aynı boyutlara sahip sıfır değerli gömme vektörlerini kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip_vision_output` | Görsel gömme vektörleri içeren bir CLIP görüntü modelinin çıktısı | CLIP_VISION_OUTPUT | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | CLIP görüntü gömme vektörlerini içeren pozitif koşullandırma verileri | CONDITIONING |
| `negative` | Pozitif gömme vektörlerinin boyutuyla eşleşen sıfır değerli gömme vektörlerini içeren negatif koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `114d23574a93bd31013fc909568023c143bba2e4ea75b35a0ebb808c19e83867`
