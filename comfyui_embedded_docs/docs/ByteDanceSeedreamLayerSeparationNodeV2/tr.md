# ByteDance Seedream 5.0 Layer Separation

ByteDance Seedream 5.0 Layer Separation, bir görüntüyü bir arka plan plakası ve yeniden konumlandırılabilir en fazla 16 saydam katmana ayrıştırır; her katmanın yığın sırası, sınırlayıcı kutusu, adı ve açıklaması bulunur. Arka planı, maskelerle birlikte katman başına görüntüleri, yerleştirme kutularını ve düzenlemeye hazır bir katman yığınını döndürür. `model` seçicisi, Seedream 5.0 Pro ile daha hızlı olan Seedream 5.0 Flash arasında seçim yapar.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Ayrıştırma için kullanılan Seedream modeli. "seedream 5.0 pro" (varsayılan) en yüksek ayrıştırma kalitesini sunar ve ayrıca bir `prompt_optimization` kontrolü sağlar; "seedream 5.0 flash" daha hızlı ve daha ucuzdur ve istem optimizasyonu kontrolü yoktur. | DYNAMIC_COMBO | Evet | "seedream 5.0 pro"<br>"seedream 5.0 flash" |

### Seedream 5.0 Pro ve 5.0 Flash Girdileri

Bu girdiler her iki modelde de kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Ayrıştırılacak görüntü. Tam olarak bir görüntü, en az 512x512 piksel, en-boy oranı 1:16 ile 16:1 arasında olmalıdır. Yaklaşık 4MP'den büyük girdiler yüklemeden önce küçültülür. | IMAGE | Evet | Tek görüntü |
| `prompt` | Görüntünün nasıl ayrıştırılacağı. Boş bırakıldığında tüm ana öğeleri otomatik algılar ve ayrıştırır. Ayrıştırmayı kontrol etmek için öğeleri doğal dille tanımlayın veya `<bbox>left top right bottom</bbox>` etiketleriyle (0-1000 aralığında binde bir koordinatlar) tam bölgeleri hedefleyin. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `size` | Çıktı çözünürlük düzeyi. "auto" girdi görüntü boyutunu izler (1K-2K aralığına sınırlandırılır). Varsayılan: "auto". | COMBO | Evet | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Üretim için kullanılacak tohum. Varsayılan: 42. | INT | Evet | 0 - 2147483647 |
| `watermark` | Görüntülere "AI generated" filigranı eklenip eklenmeyeceği. Varsayılan: false. | BOOLEAN | Evet | false<br>true |
| `crop_layers` | `layers`/`masks` toplu çıktılarının geometrisi (`layer_stack` etkilenmez ve her zaman sıkı kırpılmıştır). Tam tuval: her katman, temel boyutunda bir tuval üzerinde sınırlayıcı kutu konumunda bulunur - doğrudan ImageCompositeMasked ile yeniden birleştirin. Minimum boyut: her katman sınırlayıcı kutusuna kırpılır (toplu işleme için en büyük katmana doldurulur) - çok daha küçük tensörler; `bboxes` çıktısını kullanarak Layers From Bounding Boxes ile yerleşimi yeniden oluşturun. Varsayılan: false (tam tuval). | BOOLEAN | Evet | false (tam tuval)<br>true (minimum boyut) |

### Yalnızca Seedream 5.0 Pro Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt_optimization` | İstem optimizasyonu modu: "standard" daha yüksek kalite, "fast" daha kısa üretim süresi verir. Yalnızca Seedream 5.0 Pro ile kullanılabilir. Varsayılan: "standard". | COMBO | Evet | "standard"<br>"fast" |

**Not:** `image` girdisi tek bir görüntü olmalıdır; toplu işlemler desteklenmez. Görüntü en az 512x512 piksel olmalı ve en-boy oranı 1:16 ile 16:1 arasında olmalıdır. Seedream 5.0 Flash'ta `prompt_optimization` girişi yoktur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `base_image` | Katmanların üzerine yığıldığı temel görüntü (arka plan plakası). | IMAGE |
| `base_mask` | Temel görüntünün saydamlığı (1 = saydam, LoadImage kuralı); şu anda her zaman tamamen opaktır. | MASK |
| `layers` | Alttan üste sıralanmış saydam katmanlar. Tam tuval modu: temel boyutunda siyah bir tuval üzerinde sınırlayıcı kutu konumlarına yerleştirilir. Minimum boyut modu: sınırlayıcı kutularına kırpılır, sol üste sabitlenir, en büyük katmana doldurulur. | IMAGE |
| `masks` | Katman başına saydamlık, `layers` toplu işlemiyle dizin hizalıdır (1 = saydam, LoadImage kuralı). ImageCompositeMasked tarzı birleştirme için önce InvertMask ekleyin. | MASK |
| `bboxes` | Katman başına bir yerleştirme kutusu, `layers` toplu işlemiyle dizin hizalıdır (katman başına yerleşimi yeniden oluşturmak için `layers` ile bunu ve ayrıca `masks` çıktısını Layers From Bounding Boxes düğümüne verin): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]`, katmanın kendi çerçevesi içindeki içerik bölgesidir; tuval üzerine kutu konumuna bu uzaklık eklenerek yerleşir. | BOUNDING_BOX |
| `layer_stack` | Create Layered Image için düzenlemeye hazır katman belgesi: arka plan plakası ve her öğe, gerçek konumunda ve yığın sırasında kendi adlandırılmış, sıkı kırpılmış katmanı olarak. Doğrudan bağlayın veya Add Layer ile genişletin. | LAYERS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `b106ca63d37aea68079f0032a1f7dfeefee9f759c71bb1605bbfe66c3d9dad62`
