# Quiver Image to SVG

Quiver AI ile bir raster görüntüyü ölçeklenebilir bir vektör grafiğe (SVG) dönüştürün. Görüntü Quiver AI'nin API'sine gönderilir ve API vektörleştirilmiş sonucu döndürür.

Bir `model` seçildiğinde, aşağıda listelenen modele özgü parametreler gösterilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | SVG vektörleştirme için kullanılacak model. | DYNAMIC_COMBO | Evet | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `image` | Vektörleştirilecek giriş görüntüsü. | IMAGE | Evet | N/A |
| `auto_crop` | Baskın konuya otomatik olarak kırpar. Gelişmiş parametre (varsayılan: False). | BOOLEAN | Evet | `True`<br>`False` |
| `target_size` | Vektörleştirmeden önce giriş görüntüsüne uygulanan kare yeniden boyutlandırma, piksel cinsinden, 128 ile 4096 arası. 0 kaynak boyutu korur; bu, yeniden boyutlandırmaya zorlamaktan daha temiz vektörleştirme sağlar. Bu, çıktı tuvalini ayarlamaz; bunun için `width` ve `height` kullanın. Gelişmiş parametre (varsayılan: 0). | INT | Evet | 0 - 4096 |
| `width` | Çıktı SVG tuvalinin (viewBox) genişliği, kullanıcı birimleri cinsinden. Çıktı boyutunu ve en-boy oranını kontrol etmek için hem `width` hem de `height` değerlerini ayarlayın; modelin seçmesine izin vermek için birini 0 bırakın; bu genellikle kare bir tuval verir. Gelişmiş parametre (varsayılan: 0). | INT | Evet | 0 - 8192 |
| `height` | Çıktı SVG tuvalinin (viewBox) yüksekliği, kullanıcı birimleri cinsinden. Çıktı boyutunu ve en-boy oranını kontrol etmek için hem `width` hem de `height` değerlerini ayarlayın; modelin seçmesine izin vermek için birini 0 bırakın; bu genellikle kare bir tuval verir. Gelişmiş parametre (varsayılan: 0). | INT | Evet | 0 - 8192 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirlemek için tohum; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir. Bu parametre "oluşturma sonrası kontrol" işlevselliğine sahiptir (varsayılan: 42). | INT | Evet | 0 - 2147483647 |

### Modele Özgü Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Modelin çizim yapmadan önce ne kadar akıl yürütmeye harcadığı. Daha yüksek seviyeler ayrıntıyı artırır ve daha fazla token harcar. Yalnızca `"arrow-2"` ve `"arrow-2-telos"` modelleri tarafından kullanılır (varsayılan: `"high"`). | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |
| `temperature` | Rastgelelik kontrolü. Daha yüksek değerler rastgeleliği artırır. `"arrow-2-telos"` modeli tarafından kullanılmaz. Gelişmiş parametre (varsayılan: 1.0). | FLOAT | Evet | 0.0 - 2.0 (adım 0.1) |
| `top_p` | Nucleus örnekleme parametresi. `"arrow-2-telos"` modeli tarafından kullanılmaz. Gelişmiş parametre (varsayılan: 1.0). | FLOAT | Evet | 0.05 - 1.0 (adım 0.05) |
| `presence_penalty` | Token varlık cezası. `"arrow-2-telos"` modeli tarafından kullanılmaz. Gelişmiş parametre (varsayılan: 0.0). | FLOAT | Evet | -2.0 - 2.0 (adım 0.1) |

**Not:** `target_size` vektörleştirmeden önce uygulanır ve çıktı tuvalini değiştirmez. Modelin tuval boyutunu seçmesine izin vermek için `width` veya `height` değerini 0 bırakın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `SVG` | Vektörleştirilmiş SVG çıktısı. | SVG |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `186769b09bef2d2dbbfc26102f375ff80f8b324a24cd593da20afcea9cc2095b`
