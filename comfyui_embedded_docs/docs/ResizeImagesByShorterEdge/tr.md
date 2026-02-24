> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByShorterEdge/tr.md)

Bu düğüm, görüntülerin boyutlarını, kısa kenarın uzunluğu belirtilen bir hedef değerle eşleşecek şekilde ayarlayarak yeniden boyutlandırır. Orijinal görüntünün en-boy oranını korumak için yeni boyutları hesaplar. Yeniden boyutlandırılmış görüntü döndürülür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Yeniden boyutlandırılacak giriş görüntüsü. |
| `shorter_edge` | INT | Hayır | 1 - 8192 | Kısa kenar için hedef uzunluk. (varsayılan: 512) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Yeniden boyutlandırılmış görüntü. |
