# ByteDanceSeedreamLayerSeparationNode

ByteDance Seedream 5.0 Pro Layer Separation, bir görüntüyü bir arka plan katmanına ve her biri kendi istifleme sırasına, sınırlayıcı kutusuna, adına ve açıklamasına sahip en fazla 16 şeffaf katmana ayrıştırır. Arka planı, maskeli katman görüntülerini, yerleştirme kutularını ve düzenlemeye hazır bir katman yığınını döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Ayrıştırılacak görüntü. Tam olarak bir görüntü, en az 512x512 piksel, 1:16 ile 16:1 arasında en-boy oranı. Yaklaşık 4MP'den büyük girdiler yüklemeden önce küçültülür. | IMAGE | Evet | Tek görüntü |
| `prompt` | Görüntünün nasıl ayrıştırılacağı. Otomatik algılama ve tüm ana öğeleri ayırma için boş bırakın. Ayrıştırmayı kontrol etmek için öğeleri doğal dilde tanımlayın veya `<bbox>left top right bottom</bbox>` etiketleriyle (0-1000 bindelik koordinatlar) belirli bölgeleri hedefleyin. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `size` | Çıktı çözünürlük seviyesi. "auto", girdi görüntü boyutunu takip eder (1K-2K aralığına sınırlandırılmıştır). Varsayılan: "auto". | STRING | Evet | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Üretim için kullanılacak seed değeri. Varsayılan: 0. | INT | Evet | 0 ile 2147483647 arası |
| `prompt_optimization` | Prompt optimizasyon modu: "standard" daha yüksek kalite sağlar, "fast" daha kısa üretim süresi sağlar. Varsayılan: "standard". | STRING | Hayır | "standard"<br>"fast" |
| `watermark` | Görüntülere "AI generated" filigranı eklenip eklenmeyeceği. Varsayılan: false. | BOOLEAN | Hayır | false<br>true |
| `crop_layers` | Katman/mask toplu çıktılarının geometrisi (layer_stack bundan etkilenmez ve her zaman sıkıdır). Full canvas modu: her katman, sınırlayıcı kutu konumunda temel boyutunda bir tuval üzerinde - ImageCompositeMasked ile doğrudan yeniden birleştirin. Minimal size modu: her katman sınırlayıcı kutusuna kırpılır (toplu işleme için en büyük katmana dolgulanır) - çok daha küçük tensörler; yerleşimi, bboxes çıktısını kullanarak Layers From Bounding Boxes ile yeniden oluşturun. Varsayılan: false (full canvas). | BOOLEAN | Hayır | false (full canvas)<br>true (minimal size) |

Not: Girdi görüntüsü tek bir görüntü olmalıdır; batch girişleri desteklenmez. Görüntü en az 512x512 piksel olmalı ve en-boy oranı 1:16 ile 16:1 arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `base_image` | Katmanların üzerine istiflendiği temel görüntü (arka plan katmanı). | IMAGE |
| `base_mask` | Temel görüntünün şeffaflığı (1 = şeffaf, LoadImage kuralı); şu anda her zaman tamamen opak. | MASK |
| `layers` | Alttan üste doğru sıralanmış şeffaf katmanlar. Full canvas modu: sınırlayıcı kutu konumlarında temel boyutunda siyah bir tuval üzerine yerleştirilir. Minimal size modu: sınırlayıcı kutularına kırpılır, sol üstten hizalanır, en büyük katman boyutuna dolgulanır. | IMAGE |
| `masks` | Katman başına şeffaflık, katman batch'iyle dizin uyumlu (1 = şeffaf, LoadImage kuralı). ImageCompositeMasked tarzı birleştirme için önce InvertMask ekleyin. | MASK |
| `bboxes` | Katman başına bir yerleştirme kutusu, katman batch'iyle dizin uyumlu (katman başına yerleşimi yeniden oluşturmak için her ikisini ve maskeleri Layers From Bounding Boxes'a besleyin): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]`, katmanın kendi çerçevesi içindeki içerik bölgesidir; tuvale kutu konumu artı bu uzaklıkta yerleşir. | BOUNDING_BOX |
| `layer_stack` | Create Layered Image için düzenlemeye hazır katman belgesi: temel katman artı her öğenin, kendi adlandırılmış, sıkı kırpılmış katmanı olarak gerçek konumunda ve istifleme sırasında yer alması. Doğrudan bağlayın veya Add Layer ile genişletin. | LAYERS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/tr.md)

---
**Source fingerprint (SHA-256):** `059d0a1a5f5793aadda72f50b549b8b10e2ecae3ce003f82c0c28191c3460954`
