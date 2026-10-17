# Quiver Görselden SVG'ye (Eski)

Bu düğüm, Quiver AI'nin vektörleştirme modellerini kullanarak bir raster görüntüyü ölçeklenebilir bir vektör grafiğe (SVG) dönüştürür. Görüntüyü, işleyip vektörleştirilmiş sonucu döndüren harici bir API'ye gönderir.

**Not:** Bu düğüm kaynak kodda kullanımdan kaldırılmış olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Vektörleştirilecek giriş görüntüsü. | IMAGE | Evet | N/A |
| `auto_crop` | Baskın özneye otomatik olarak kırp (varsayılan: False). | BOOLEAN | Evet | True<br>False |
| `model` | SVG vektörleştirme için kullanılacak model. Bir model seçmek, o modele özel ek parametreleri gösterir: `target_size` (piksel cinsinden kare yeniden boyutlandırma hedefi; 0 kaynak görüntü boyutunu korur, aksi halde 128 ile 4096 arası), `temperature`, `top_p` ve `presence_penalty`. | DYNAMIC_COMBO | Evet | `"arrow-2"`<br>`"arrow-2-telos"` |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirlemek için tohum; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir. Bu parametre "generate sonrası kontrol" işlevine sahiptir (varsayılan: 0). | INT | Evet | 0 ile 2147483647 arası |
| `reasoning_effort` | Modelin çizim yapmadan önce ne kadar akıl yürütme harcayacağı. Daha yüksek seviyeler ayrıntıyı iyileştirir ve daha fazla token maliyetine yol açar. Yalnızca Arrow 2 modelleri tarafından kullanılır (varsayılan: "high"). | COMBO | Hayır | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `SVG` | Vektörleştirilmiş SVG çıktısı. | SVG |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNode/tr.md)

---
---
**Source fingerprint (SHA-256):** `196b0693328478bff21b11da87c52608e8bb57abb9bf482052782231f6d81c30`
