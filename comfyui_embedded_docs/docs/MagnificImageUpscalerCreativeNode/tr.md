# Magnific Görüntü Büyütme (Yaratıcı)

Bu düğüm, bir görüntüyü büyütmek ve yaratıcı bir şekilde geliştirmek için Magnific AI hizmetini kullanır. Geliştirmeyi bir metin istemiyle yönlendirmenize, optimize edilecek belirli bir stil seçmenize ve ayrıntı, orijinale benzerlik ve stilizasyon gücü gibi yaratıcı sürecin çeşitli yönlerini kontrol etmenize olanak tanır. Düğüm, seçtiğiniz faktörde (2x, 4x, 8x veya 16x) büyütülmüş bir görüntü çıkarır; maksimum çıktı boyutu 25,3 megapikseldir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Büyütülecek ve geliştirilecek giriş görüntüsü. | IMAGE | Evet | - |
| `prompt` | Görüntünün yaratıcı gelişimini yönlendirecek metin açıklaması. İsteğe bağlıdır (varsayılan: boş). | STRING | Hayır | - |
| `ölçek_faktörü` | Görüntünün boyutlarının büyütülme faktörü. | COMBO | Evet | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `için_optimize_edildi` | Geliştirme sürecinin optimize edileceği stil veya içerik türü. | COMBO | Evet | `"standard"`<br>`"soft_portraits"`<br>`"hard_portraits"`<br>`"art_n_illustration"`<br>`"videogame_assets"`<br>`"nature_n_landscapes"`<br>`"films_n_photography"`<br>`"3d_renders"`<br>`"science_fiction_n_horror"` |
| `yaratıcılık` | Görüntüye uygulanan yaratıcı yorumlama düzeyini kontrol eder (varsayılan: 0). | INT | Hayır | -10 ile 10 |
| `hdr` | Netlik ve ayrıntı düzeyi (varsayılan: 0). | INT | Hayır | -10 ile 10 |
| `benzerlik` | Orijinal görüntüye benzerlik düzeyi (varsayılan: 0). | INT | Hayır | -10 ile 10 |
| `fraktalite` | İstemin gücü ve piksel kare başına karmaşıklık (varsayılan: 0). | INT | Hayır | -10 ile 10 |
| `motor` | İşleme için kullanılacak belirli AI motoru. Bu gelişmiş bir parametredir. | COMBO | Evet | `"automatic"`<br>`"magnific_illusio"`<br>`"magnific_sharpy"`<br>`"magnific_sparkle"` |
| `otomatik_küçültme` | Çıktı maksimum piksel sınırını aşarsa giriş görüntüsünü otomatik olarak küçült (varsayılan: False). Bu gelişmiş bir parametredir. | BOOLEAN | Hayır | - |

**Kısıtlamalar:**

* Giriş `image` değeri tam olarak bir görüntü olmalıdır.
* Giriş görüntüsünün minimum yüksekliği ve genişliği 160 piksel olmalıdır.
* Giriş görüntüsünün en-boy oranı 1:3 ile 3:1 arasında olmalıdır.
* Nihai çıktı boyutu (`scale_factor` ile çarpılmış giriş boyutları) 25.300.000 pikseli aşamaz. Bu sınır aşılacaksa:
  - `auto_downscale` etkinleştirildiğinde, düğüm giriş görüntüsü boyutunu otomatik olarak (en fazla 2 kat) küçültür veya çıktının sınır içinde kalması için daha düşük bir `scale_factor` kullanır.
  - `auto_downscale` devre dışı bırakıldığında, düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Yaratıcı bir şekilde geliştirilmiş ve büyütülmüş çıktı görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerCreativeNode/tr.md)

---
**Source fingerprint (SHA-256):** `36c38e87f9f1e568c78cf794aeb0a268c6d25d639006eb2cf18ee040d3071ad4`
