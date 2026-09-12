# ByteDance Seedream 5.0 Pro Katman Ayrıştırma

ByteDance Seedream 5.0 Pro Layer Separation, bir görüntüyü bir arka plan plakası ve yeniden konumlandırılabilir en fazla 16 şeffaf katmana ayırır; her katmanın yığın sırası, sınırlayıcı kutusu, adı ve açıklaması vardır. Arka planı, maskelerle birlikte katman başına görüntüleri, yerleştirme kutularını ve düzenlemeye hazır bir katman yığınını döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Ayrıştırılacak görüntü. Tam olarak bir görüntü, en az 512x512 piksel, en-boy oranı 1:16 ile 16:1 arasında. Yaklaşık 4MP'den büyük girdiler yüklemeden önce küçültülür. | IMAGE | Evet | Single image |
| `prompt` | Görüntünün nasıl ayrıştırılacağı. Tüm ana öğeleri otomatik algılamak ve ayırmak için boş bırakın. Ayrıştırmayı kontrol etmek için öğeleri doğal dille tanımlayın veya `<bbox>left top right bottom</bbox>` etiketleriyle (0-1000 binde bir koordinatlar) tam bölgeleri hedefleyin. Varsayılan: boş dize. | STRING | Evet | Multiline text |
| `size` | Çıktı çözünürlük düzeyi. "auto" girdi görüntü boyutunu izler (1K-2K aralığına sınırlandırılır). Varsayılan: "auto". | COMBO | Evet | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Üretim için kullanılacak tohum. Varsayılan: 0. | INT | Evet | 0 to 2147483647 |
| `prompt_optimization` | İstem optimizasyonu modu: "standard" daha yüksek kalite, "fast" daha kısa üretim süresi verir. Varsayılan: "standard". | COMBO | Hayır | "standard"<br>"fast" |
| `watermark` | Görüntülere "AI generated" filigranı eklenip eklenmeyeceği. Varsayılan: false. | BOOLEAN | Hayır | false<br>true |
| `crop_layers` | Katmanlar/maskeler toplu çıktılarının geometrisi (`layer_stack` etkilenmez ve her zaman sıkı kırpılmıştır). Tam tuval: her katman, taban boyutunda bir tuval üzerinde sınırlayıcı kutusu konumunda - ImageCompositeMasked ile doğrudan yeniden birleştirin. Minimum boyut: her katman sınırlayıcı kutusuna kırpılır (toplu işlem için en büyük katmana kadar doldurulur) - çok daha küçük tensörler; `bboxes` çıktısını kullanarak Layers From Bounding Boxes ile yerleşimi yeniden oluşturun. Varsayılan: false (tam tuval). | BOOLEAN | Hayır | false (full canvas)<br>true (minimal size) |

Not: `image` girdisi tek bir görüntü olmalıdır; toplu işlemler desteklenmez. Görüntü en az 512x512 piksel olmalı ve en-boy oranı 1:16 ile 16:1 arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `base_image` | Katmanların üzerine yığıldığı taban görüntü (arka plan plakası). | IMAGE |
| `base_mask` | Taban görüntünün şeffaflığı (1 = şeffaf, LoadImage kuralı); şu anda her zaman tamamen opaktır. | MASK |
| `layers` | Alttan üste sıralanmış şeffaf katmanlar. Tam tuval modu: taban boyutunda siyah bir tuval üzerinde sınırlayıcı kutusu konumuna yerleştirilir. Minimum boyut modu: sınırlayıcı kutusuna kırpılır, sol üste sabitlenir, en büyük katmana kadar doldurulur. | IMAGE |
| `masks` | Katman başına şeffaflık, katmanlar toplu işiyle dizin hizalı (1 = şeffaf, LoadImage kuralı). ImageCompositeMasked tarzı birleştirme için önce InvertMask ekleyin. | MASK |
| `bboxes` | Katman başına bir yerleştirme kutusu, katmanlar toplu işiyle dizin hizalı (katman başına yerleşimi yeniden oluşturmak için her ikisini ve maskeleri Layers From Bounding Boxes'a besleyin): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]`, katmanın kendi çerçevesi içindeki içerik bölgesidir; tuval üzerinde kutunun konumuna artı bu uzaklığa denk gelen yere oturur. | BOUNDING_BOX |
| `layer_stack` | Create Layered Image için düzenlemeye hazır katman belgesi: taban plakası artı her öğe, gerçek konumunda ve yığın sırasında kendi adlandırılmış, sıkı kırpılmış katmanı olarak. Doğrudan bağlayın veya Add Layer ile genişletin. | LAYERS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/tr.md)

---
**Source fingerprint (SHA-256):** `5062760f2930333f8ed7d8b09dff2492c23fdf906ef71b111348687bef572821`
