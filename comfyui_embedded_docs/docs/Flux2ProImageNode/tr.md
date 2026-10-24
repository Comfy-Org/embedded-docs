# Flux.2 [pro] Görsel

Bir istem ve belirtilen çıktı boyutlarıyla, isteğe bağlı olarak referans görüntülerle yönlendirilerek BFL API üzerinden Flux.2 [pro] ile bir görüntü oluşturur.

**Not:** Bu düğüm, kaynak kodda kullanımdan kaldırılmış olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `istem` | Görüntü oluşturma veya düzenleme için istem. | STRING | Evet | - |
| `genişlik` | Oluşturulan görüntünün piksel cinsinden genişliği (varsayılan: 1024). | INT | Evet | 256 ile 2048 arası (adım: 32) |
| `yükseklik` | Oluşturulan görüntünün piksel cinsinden yüksekliği (varsayılan: 768). | INT | Evet | 256 ile 2048 arası (adım: 32) |
| `tohum` | Gürültüyü oluşturmak için kullanılan rastgele tohum (varsayılan: 0). | INT | Evet | 0 ile 18446744073709551615 arası |
| `istem üst örnekleme` | İstem üzerinde üst örnekleme yapılıp yapılmayacağı. Etkinse, daha yaratıcı oluşturma için istem otomatik olarak değiştirilir (varsayılan: `True`). Bu gelişmiş bir ayardır. | BOOLEAN | Evet | True / False |
| `görseller` | Görüntüden görüntüye oluşturma için isteğe bağlı referans görüntüler. Her görüntü yüklenmeden önce en fazla 2048x2048 piksele kadar küçültülür. | IMAGE | Hayır | 0 ile 9 arası görüntü |

**Kısıtlamalar:**

* 9'dan fazla referans görüntü bağlamak hata oluşturur.
* Çıktı boyutu megapiksel başına ücretlendirilir; bu nedenle daha büyük `width` ve `height` değerleri daha maliyetlidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Oluşturulan görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ProImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `ffa3934abaa38e030eedf2624e7a91333e24a92d7ac89af8637e59d59341eb6d`
