# Hunyuan3Dv2Koşullandırma

Hunyuan3Dv2Conditioning düğümü, 3D modeller için koşullandırma verileri oluşturmak üzere CLIP görüş çıktısını işler. Görüş çıktısından son gizli durum yerleştirmelerini çıkarır ve hem pozitif hem de negatif koşullandırma çiftleri oluşturur. Pozitif koşullandırma gerçek yerleştirmeleri kullanırken, negatif koşullandırma aynı şekle sahip sıfır değerli yerleştirmeleri kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_görü_çıktısı` | Görsel yerleştirmeler içeren bir CLIP görüş modelinin çıktısı | CLIP_VISION_OUTPUT | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | CLIP görüş yerleştirmelerini içeren pozitif koşullandırma verisi | CONDITIONING |
| `negative` | Pozitif yerleştirmelerle aynı şekle sahip sıfır değerli yerleştirmeler içeren negatif koşullandırma verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `114d23574a93bd31013fc909568023c143bba2e4ea75b35a0ebb808c19e83867`
