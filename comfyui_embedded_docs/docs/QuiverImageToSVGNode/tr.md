> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNode/tr.md)

Bu belge, Quiver AI'nin vektörleştirme modellerini kullanarak bir raster görüntüyü ölçeklenebilir vektör grafiğine (SVG) dönüştürür. Görüntüyü, işleyip vektörleştirilmiş sonucu döndüren harici bir API'ye gönderir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | Yok | Vektörleştirilecek giriş görüntüsü. |
| `auto_crop` | BOOLEAN | Hayır | `True`<br>`False` | Baskın nesneye otomatik olarak kırpma yapar. Bu gelişmiş bir parametredir (varsayılan: `False`). |
| `model` | DYNAMICCOMBO | Evet | Birden çok seçenek mevcut | SVG vektörleştirmesi için kullanılacak model. Bir model seçmek, o modele özgü ek parametreleri ortaya çıkarır: `target_size` (piksel cinsinden kare yeniden boyutlandırma hedefi, varsayılan: 1024, aralık: 128-4096), `temperature`, `top_p` ve `presence_penalty`. |
| `seed` | INT | Hayır | 0 ile 2147483647 arası | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar, tohum değerinden bağımsız olarak deterministik değildir. Bu parametre "oluşturma sonrası kontrol" işlevine sahiptir (varsayılan: 0). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `SVG` | SVG | Vektörleştirilmiş SVG çıktısı. |

---
**Source fingerprint (SHA-256):** `4539277fd6c23aef149c44eeafca4d373cad658d85872de0883245eb4f2479e8`
