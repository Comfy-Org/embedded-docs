# Flux.2 [max] Görsel

Flux.2 [max] ile BFL API üzerinden bir istem ve açık çıktı boyutları kullanarak, isteğe bağlı olarak referans görsellerle yönlendirilebilen bir görsel oluşturur. Flux.2 [pro] Image ile aynı girdileri sunar.

**Not:** Bu düğüm kaynak kodunda kullanımdan kaldırılmış olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istem` | Görsel oluşturma veya düzenleme için istem. | STRING | Evet | - |
| `genişlik` | Oluşturulan görselin piksel cinsinden genişliği (varsayılan: 1024). | INT | Evet | 256 ile 2048 arası (adım: 32) |
| `yükseklik` | Oluşturulan görselin piksel cinsinden yüksekliği (varsayılan: 768). | INT | Evet | 256 ile 2048 arası (adım: 32) |
| `tohum` | Gürültüyü oluşturmak için kullanılan rastgele tohum (varsayılan: 0). | INT | Evet | 0 ile 18446744073709551615 arası |
| `istem üst örnekleme` | İstem üzerinde üst örnekleme yapılıp yapılmayacağı. Etkinse, daha yaratıcı oluşturma için istem otomatik olarak değiştirilir (varsayılan: `True`). Bu gelişmiş bir ayardır. | BOOLEAN | Evet | True / False |
| `görseller` | Görselden görsele oluşturma için isteğe bağlı referans görseller. Her görsel, yüklenmeden önce en fazla 2048x2048 piksele kadar küçültülür. | IMAGE | Hayır | 0 ile 9 arası görüntü |

**Kısıtlamalar:**

* 9'dan fazla referans görsel bağlamak hata verir.
* Çıktı boyutu megapiksel başına ücretlendirilir; bu nedenle daha büyük `width` ve `height` değerleri daha fazla maliyet oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Oluşturulan görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2MaxImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `cd540606835e7808861d9a96584731100b1bf9c996f18586fed39e8a2d32a29f`
