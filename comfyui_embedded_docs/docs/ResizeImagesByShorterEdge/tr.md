> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByShorterEdge/tr.md)

Bu düğüm, görselleri orijinal en-boy oranını koruyarak kısa kenarı belirtilen uzunluğa denk gelecek şekilde yeniden boyutlandırır. Kısa kenar için hedef uzunluğa göre yeni boyutları hesaplar ve yeniden boyutlandırılmış görseli döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `image` | IMAGE | Evet | - | Yeniden boyutlandırılacak giriş görseli. |
| `shorter_edge` | INT | Hayır | 1 ile 8192 arası | Kısa kenar için hedef uzunluk. (varsayılan: 512) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `image` | IMAGE | Kısa kenarı belirtilen hedef uzunluğa denk gelecek şekilde yeniden boyutlandırılmış görsel. |

---
**Source fingerprint (SHA-256):** `011949390faa9032587aec210d9e38d55b79e474c7a6dcd5d3c0e75594a1fc29`
