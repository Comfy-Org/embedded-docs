Bu düğüm, görselleri orijinal en-boy oranını koruyarak kısa kenarı belirtilen uzunluğa denk gelecek şekilde yeniden boyutlandırır. Kısa kenar için hedef uzunluğa göre yeni boyutları hesaplar ve yeniden boyutlandırılmış görseli döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Yeniden boyutlandırılacak giriş görseli. | IMAGE | Evet | - |
| `kısa_kenar` | Kısa kenar için hedef uzunluk. (varsayılan: 512) | INT | Hayır | 1 ile 8192 arası |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Kısa kenarı belirtilen hedef uzunluğa denk gelecek şekilde yeniden boyutlandırılmış görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByShorterEdge/tr.md)

---
**Source fingerprint (SHA-256):** `011949390faa9032587aec210d9e38d55b79e474c7a6dcd5d3c0e75594a1fc29`
