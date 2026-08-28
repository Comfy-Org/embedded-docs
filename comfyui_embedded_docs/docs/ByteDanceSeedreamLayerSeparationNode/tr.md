# ByteDance Seedream 5.0 Pro Katman Ayrıştırma

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Ayrıştırılacak görsel. Tam olarak bir görsel; en az 512x512 piksel, 1:16 ile 16:1 arasında en boy oranı. Yaklaşık 4MP'den büyük girdiler yüklemeden önce küçültülür. | IMAGE | Evet | Tek görsel |
| `istem` | Görselin nasıl ayrıştırılacağı. Otomatik algılama ve tüm ana öğeleri ayırma için boş bırakın. Ayrıştırmayı kontrol etmek için öğeleri doğal dilde tanımlayın veya `<bbox>left top right bottom</bbox>` etiketleriyle belirli bölgeleri hedefleyin (0-1000 binde birlik koordinatlar). Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `boyut` | Çıktı çözünürlük düzeyi. "auto", girdi görselinin boyutunu izler (1K-2K aralığına sınırlanır). Varsayılan: "auto". | COMBO | Evet | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `tohum` | Üretim için kullanılacak tohum değeri. Varsayılan: 0. | INT | Evet | 0 - 2147483647 |
| `istem_optimizasyonu` | İstem iyileştirme modu: "standard" daha yüksek kalite, "fast" daha kısa üretim süresi sağlar. Varsayılan: "standard". | COMBO | Hayır | "standard"<br>"fast" |
| `filigran` | Görsellere "AI generated" filigranı eklenip eklenmeyeceği. Varsayılan: false. | BOOLEAN | Hayır | false<br>true |
| `katmanları_kırp` | Katman/maske toplu çıktılarının geometrisi (`layer_stack` etkilenmez ve her zaman içeriğe tam oturacak şekilde kırpılmıştır). Tam tuval: her katman, sınırlayıcı kutusu konumunda taban boyutunda bir tuval üzerine yerleştirilir - ImageCompositeMasked ile doğrudan yeniden birleştirin. Minimum boyut: her katman, sınırlayıcı kutusuna göre kırpılır (toplu işlem için en büyük katmana dolgulanır) - çok daha küçük tensörler; yerleşimi, `bboxes` çıktısını kullanarak Layers From Bounding Boxes ile yeniden oluşturun. Varsayılan: false (tam tuval). | BOOLEAN | Hayır | false (tam tuval)<br>true (minimum boyut) |

Not: `image` girdisi tek bir görsel olmalıdır; toplu işlemler desteklenmez. Görsel, en az 512x512 piksel boyutunda ve 1:16 ile 16:1 arasında bir en boy oranına sahip olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `taban_görüntü` | Katmanların üzerine yerleştiği temel görsel (arka plan katmanı). | IMAGE |
| `taban_maske` | Temel görselin saydamlığı (1 = saydam, LoadImage kuralı); şu anda her zaman tamamen opaktır. | MASK |
| `katmanlar` | Alttan üste sıralanmış saydam katmanlar. Tam tuval modu: sınırlayıcı kutusu konumlarında, siyah taban boyutunda bir tuval üzerine yerleştirilir. Minimum boyut modu: sınırlayıcı kutularına göre kırpılır, sol üste hizalanır ve en büyük katmana dolgulanır. | IMAGE |
| `maskeler` | Katman başına saydamlık; katman toplu işlemiyle dizin uyumludur (1 = saydam, LoadImage kuralı). ImageCompositeMasked tarzı birleştirme için önce InvertMask ekleyin. | MASK |
| `bboxes` | Katman başına bir yerleştirme kutusu; katman toplu işlemiyle dizin uyumludur (katman başına yerleşimi yeniden oluşturmak için her ikisini ve maskeleri Layers From Bounding Boxes düğümüne verin): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]`, katmanın kendi çerçevesi içindeki içerik bölgesidir; kutu konumuna bu ofset eklenmiş haliyle tuval üzerine yerleşir. | BOUNDING_BOX |
| `katman_yığını` | Create Layered Image için düzenlemeye hazır katman belgesi: temel katman artı her öğe, kendi adlandırılmış, içeriğine tam oturacak şekilde kırpılmış katmanı olarak gerçek konumunda ve istifleme sırasındadır. Doğrudan bağlayın veya Add Layer ile genişletin. | LAYERS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/tr.md)

---
**Source fingerprint (SHA-256):** `5062760f2930333f8ed7d8b09dff2492c23fdf906ef71b111348687bef572821`
