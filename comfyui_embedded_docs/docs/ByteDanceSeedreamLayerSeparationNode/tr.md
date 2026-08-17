# ByteDance Seedream 5.0 Pro Katman Ayrıştırma

ByteDance Seedream 5.0 Pro Layer Separation, bir görüntüyü bir arka plan plakası ve en fazla 16 saydam katmana ayrıştırır; her katmanın kendi istifleme sırası, sınırlayıcı kutusu, adı ve açıklaması bulunur. Arka planı, katman başına maskeli görüntüleri, yerleştirme kutularını ve düzenlemeye hazır bir katman yığınını döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Ayrıştırılacak görüntü. Tam olarak bir görüntü, en az 512x512 piksel, en boy oranı 1:16 ile 16:1 arasında. Yaklaşık 4MP'den büyük girdiler yüklemeden önce küçültülür. | IMAGE | Evet | Single image |
| `prompt` | Görüntünün nasıl ayrıştırılacağı. Tüm ana öğeleri otomatik algılamak ve ayırmak için boş bırakın. Ayrıştırmayı denetlemek için öğeleri doğal dilde tanımlayın veya `<bbox>left top right bottom</bbox>` etiketleriyle tam bölgeleri hedefleyin (0-1000 binde birlik koordinatlar). Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `size` | Çıktı çözünürlük düzeyi. "auto", girdi görüntü boyutunu izler (1K-2K aralığına sınırlandırılır). Varsayılan: "auto". | COMBO | Evet | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Üretim için kullanılacak tohum. Varsayılan: 0. | INT | Evet | 0 to 2147483647 |
| `prompt_optimization` | İstem iyileştirme modu: "standard" daha yüksek kalite sağlar, "fast" daha kısa üretim süresi sağlar. Varsayılan: "standard". | COMBO | Hayır | "standard"<br>"fast" |
| `watermark` | Görüntülere "AI generated" filigranı eklenip eklenmeyeceği. Varsayılan: false. | BOOLEAN | Hayır | false<br>true |
| `crop_layers` | Katmanlar/maskeler toplu çıktılarının geometrisi (layer_stack etkilenmez ve her zaman sıkı kırpılmıştır). Full canvas: her katman, sınırlayıcı kutusu konumunda temel boyutlu bir tuval üzerinde - ImageCompositeMasked ile doğrudan yeniden birleştirin. Minimal size: her katman sınırlayıcı kutusuna kırpılır (toplu işleme için en büyük katmana dolgulanır) - çok daha küçük tensörler; bboxes çıktısını kullanarak Layers From Bounding Boxes ile yerleşimi yeniden oluşturun. Varsayılan: false (full canvas). | BOOLEAN | Hayır | false (full canvas)<br>true (minimal size) |

Not: Girdi görüntüsü tek bir görüntü olmalıdır; toplu işlemler desteklenmez. Görüntü en az 512x512 piksel olmalı ve en boy oranı 1:16 ile 16:1 arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `base_image` | Katmanların üzerine yığıldığı temel görüntü (arka plan plakası). | IMAGE |
| `base_mask` | Temel görüntünün saydamlığı (1 = saydam, LoadImage kuralı); şu anda her zaman tamamen opak. | MASK |
| `layers` | Alttan üste sıralanmış saydam katmanlar. Full canvas modunda: siyah, temel boyutlu bir tuval üzerinde sınırlayıcı kutu konumlarına yerleştirilir. Minimal size modunda: sınırlayıcı kutularına kırpılır, sol üst köşeye hizalanır ve en büyük katmana dolgulanır. | IMAGE |
| `masks` | Katman başına saydamlık, katman topluluğuyla dizin hizalı (1 = saydam, LoadImage kuralı). ImageCompositeMasked tarzı birleştirme için önce InvertMask ekleyin. | MASK |
| `bboxes` | Katman başına bir yerleştirme kutusu, katman topluluğuyla dizin hizalı (katman başına yerleşimi yeniden oluşturmak için her ikisini ve maskeleri Layers From Bounding Boxes'a verin): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]`, katmanın kendi çerçevesi içindeki içerik bölgesidir; tuval üzerinde kutu konumuna bu uzaklığın eklenmesiyle konumlanır. | BOUNDING_BOX |
| `layer_stack` | Create Layered Image için düzenlemeye hazır katman belgesi: temel plaka ve her öğe, gerçek konumunda ve istifleme sırasında kendi adlandırılmış, sıkı kırpılmış katmanı olarak. Doğrudan bağlayın veya Add Layer ile genişletin. | LAYERS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/tr.md)

---
**Source fingerprint (SHA-256):** `5062760f2930333f8ed7d8b09dff2492c23fdf906ef71b111348687bef572821`
