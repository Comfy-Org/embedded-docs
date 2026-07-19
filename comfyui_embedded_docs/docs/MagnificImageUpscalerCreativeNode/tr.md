# Magnific Görüntü Büyütme (Yaratıcı)

Bu düğüm, bir görseli büyütmek ve yaratıcı bir şekilde geliştirmek için Magnific AI hizmetini kullanır. Geliştirmeyi bir metin istemiyle yönlendirmenize, optimize edilecek belirli bir stil seçmenize ve detay, orijinale benzerlik ve stilizasyon gücü gibi yaratıcı sürecin çeşitli yönlerini kontrol etmenize olanak tanır. Düğüm, seçtiğiniz faktöre (2x, 4x, 8x veya 16x) göre büyütülmüş bir görsel çıktısı verir ve maksimum çıktı boyutu 25,3 megapikseldir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Büyütülecek ve geliştirilecek giriş görseli. | IMAGE | Evet | - |
| `prompt` | Görselin yaratıcı gelişimini yönlendirecek bir metin açıklaması. Bu isteğe bağlıdır (varsayılan: boş). | STRING | Hayır | - |
| `ölçek_faktörü` | Görselin boyutlarının büyütüleceği faktör. | COMBO | Evet | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `için_optimize_edildi` | Geliştirme sürecinin optimize edileceği stil veya içerik türü. | COMBO | Evet | `"standard"`<br>`"soft_portraits"`<br>`"hard_portraits"`<br>`"art_n_illustration"`<br>`"videogame_assets"`<br>`"nature_n_landscapes"`<br>`"films_n_photography"`<br>`"3d_renders"`<br>`"science_fiction_n_horror"` |
| `yaratıcılık` | Görsele uygulanan yaratıcı yorumlama düzeyini kontrol eder (varsayılan: 0). | INT | Hayır | -10 ile 10 |
| `hdr` | Tanımlama ve detay düzeyi (varsayılan: 0). | INT | Hayır | -10 ile 10 |
| `benzerlik` | Orijinal görsele benzerlik düzeyi (varsayılan: 0). | INT | Hayır | -10 ile 10 |
| `fraktalite` | İstemin gücü ve piksel kare başına karmaşıklık (varsayılan: 0). | INT | Hayır | -10 ile 10 |
| `motor` | İşleme için kullanılacak belirli AI motoru. Bu gelişmiş bir parametredir. | COMBO | Evet | `"automatic"`<br>`"magnific_illusio"`<br>`"magnific_sharpy"`<br>`"magnific_sparkle"` |
| `otomatik_küçültme` | Etkinleştirildiğinde, istenen büyütme izin verilen maksimum çıktı boyutu olan 25,3 megapikseli aşarsa düğüm, giriş görselini otomatik olarak küçültür. Bu gelişmiş bir parametredir (varsayılan: False). | BOOLEAN | Hayır | - |

**Kısıtlamalar:**

* Giriş `image` tam olarak bir görsel olmalıdır.
* Giriş görselinin minimum yükseklik ve genişliği 160 piksel olmalıdır.
* Giriş görselinin en-boy oranı 1:3 ile 3:1 arasında olmalıdır.
* Nihai çıktı boyutu (giriş boyutları `scale_factor` ile çarpılarak) 25.300.000 pikseli aşamaz. `auto_downscale` devre dışıysa ve bu sınır aşılacaksa, düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Yaratıcı bir şekilde geliştirilmiş ve büyütülmüş çıktı görseli. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerCreativeNode/tr.md)

---
**Source fingerprint (SHA-256):** `f5f046347c2992a2589153e803de14fc23b27187864b45eb566556418ebc161c`
