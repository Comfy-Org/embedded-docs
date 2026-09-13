# Magnific Görüntü Büyütme (Yaratıcı)

Bu düğüm, bir görüntüyü büyütmek ve yaratıcı biçimde iyileştirmek için Magnific AI hizmetini kullanır. İyileştirmeyi bir metin istemiyle yönlendirmenize, optimize edilecek belirli bir stil seçmenize ve ayrıntı, orijinale benzerlik ve stilizasyon gücü gibi yaratıcı sürecin çeşitli yönlerini kontrol etmenize olanak tanır. Düğüm, seçtiğiniz katsayıda (2x, 4x, 8x veya 16x) ve maksimum 25,3 megapiksel çıktı boyutuyla büyütülmüş bir görüntü verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Büyütülecek ve iyileştirilecek giriş görüntüsü. | IMAGE | Evet | - |
| `prompt` | Görüntünün yaratıcı iyileştirmesini yönlendirmek için bir metin açıklaması. Varsayılan boş bir dizedir (bu durumda hiçbir istem gönderilmez). | STRING | Evet | - |
| `ölçek_faktörü` | Görüntünün boyutlarının büyütüleceği katsayı. | COMBO | Evet | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `için_optimize_edildi` | İyileştirme sürecinin optimize edileceği stil veya içerik türü. | COMBO | Evet | `"standard"`<br>`"soft_portraits"`<br>`"hard_portraits"`<br>`"art_n_illustration"`<br>`"videogame_assets"`<br>`"nature_n_landscapes"`<br>`"films_n_photography"`<br>`"3d_renders"`<br>`"science_fiction_n_horror"` |
| `yaratıcılık` | Görüntüye uygulanan yaratıcı yorumlama düzeyini kontrol eder (varsayılan: 0). | INT | Evet | -10 - 10 |
| `hdr` | Netlik ve ayrıntı düzeyi (varsayılan: 0). | INT | Evet | -10 - 10 |
| `benzerlik` | Orijinal görüntüye benzerlik düzeyi (varsayılan: 0). | INT | Evet | -10 - 10 |
| `fraktalite` | İstemin gücü ve kare piksel başına karmaşıklık (varsayılan: 0). | INT | Evet | -10 - 10 |
| `motor` | İşleme için kullanılacak belirli yapay zeka motoru. Bu gelişmiş bir parametredir. | COMBO | Evet | `"automatic"`<br>`"magnific_illusio"`<br>`"magnific_sharpy"`<br>`"magnific_sparkle"` |
| `otomatik_küçültme` | Çıktı maksimum piksel sınırını aşacaksa giriş görüntüsünü otomatik olarak küçültür (varsayılan: False). Bu gelişmiş bir parametredir. | BOOLEAN | Evet | - |

**Kısıtlamalar:**

* Giriş `image` tam olarak bir görüntü olmalıdır.
* Giriş görüntüsünün minimum yüksekliği ve genişliği 160 piksel olmalıdır.
* Giriş görüntüsünün en-boy oranı 1:3 ile 3:1 arasında olmalıdır.
* Nihai çıktı boyutu (giriş boyutları `scale_factor` ile çarpılır) 25.300.000 pikseli aşamaz. Bu sınır aşılacaksa:
  - `auto_downscale` etkinleştirildiğinde, düğüm giriş görüntüsü boyutunu otomatik olarak azaltır (ek küçültme en fazla 2x ile sınırlı tutulur) veya çıktının sınır içinde kalması için daha düşük bir `scale_factor` kullanır.
  - `auto_downscale` devre dışı bırakıldığında, düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Yaratıcı biçimde iyileştirilmiş ve büyütülmüş çıktı görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerCreativeNode/tr.md)

---
**Source fingerprint (SHA-256):** `36c38e87f9f1e568c78cf794aeb0a268c6d25d639006eb2cf18ee040d3071ad4`
