# Hunyuan3Dv2Koşullandırma

Hunyuan3Dv2Conditioning düğümü, 3B modeller için koşullandırma verileri oluşturmak amacıyla CLIP görüntü çıktısını işler. Görüntü çıktısından son gizli durum yerleştirmelerini (embeddings) çıkarır ve hem pozitif hem de negatif koşullandırma çiftleri oluşturur. Pozitif koşullandırma, gerçek yerleştirmeleri kullanırken, negatif koşullandırma aynı şekle sahip sıfır değerli yerleştirmeleri kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip_görü_çıktısı` | Görsel yerleştirmeler içeren bir CLIP görüntü modelinin çıktısı | CLIP_VISION_OUTPUT | Evet | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | CLIP görüntü yerleştirmelerini içeren pozitif koşullandırma verileri | CONDITIONING |
| `negative` | Pozitif yerleştirmelerin şekliyle eşleşen sıfır değerli yerleştirmeler içeren negatif koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `3a32967d62a0645b0c375b17ab96e20805c2e0005e585dddf5a3a77d35994fec`
