> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/tr.md)

Hunyuan3Dv2Conditioning düğümü, video modelleri için koşullandırma verisi oluşturmak üzere CLIP görüntü çıktısını işler. Görüntü çıktısından son gizli durum yerleştirmelerini (embeddings) çıkarır ve hem pozitif hem de negatif koşullandırma çiftleri oluşturur. Pozitif koşullandırma gerçek yerleştirmeleri kullanırken, negatif koşullandırma aynı şekle sahip sıfır değerli yerleştirmeler kullanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip_görü_çıktısı` | CLIP_VISION_OUTPUT | Evet | - | Görsel yerleştirmeler içeren bir CLIP görüntü modeli çıktısı |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | CLIP görüntü yerleştirmelerini içeren pozitif koşullandırma verisi |
| `negative` | CONDITIONING | Pozitif yerleştirmelerin şekliyle eşleşen sıfır değerli yerleştirmeler içeren negatif koşullandırma verisi |