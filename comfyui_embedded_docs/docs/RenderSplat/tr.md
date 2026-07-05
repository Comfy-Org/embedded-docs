# Splat Oluştur

Bir gaussian splat'ı, yönlendirilmiş eliptik splatlar, kenar yumuşatma ve derinlik sıralı önden arkaya işleme ile anizotropik EWA rasterleştirici kullanarak görüntü olarak işler. Kamera, bir `camera_info` girişinden gelir veya splat'ı otomatik çerçevelemek için boş bırakabilirsiniz. Bir Video düğümünü beslemek için döner tabla görüntü grubu oluşturmak üzere kare sayısını 1'den büyük ayarlayın.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `splat` | İşlenecek gaussian splat verisi | SPLAT | Evet | - |
| `genişlik` | Çıktı görüntüsünün genişliği (varsayılan: 1024) | INT | Evet | 64 ila 2048 (adım: 8) |
| `yükseklik` | Çıktı görüntüsünün yüksekliği (varsayılan: 1024) | INT | Evet | 64 ila 2048 (adım: 8) |
| `kareler` | İşlenecek kare sayısı. -1, 0 veya 1 tek bir hareketsiz görüntü üretir. 1'den büyük değerler, kameranın tam 360 derece döndüğü bir döner tabla animasyonu oluşturur. Negatif değerler ters yönde döner (varsayılan: 1) | INT | Evet | -240 ila 240 |
| `splat_ölçeği` | Her splat'ın öngörülen ayak izindeki çarpan. Düşük değerler daha keskin noktalar, yüksek değerler daha yumuşak ve dolgun yüzeyler üretir (varsayılan: 1.0) | FLOAT | Evet | 0.1 ila 5.0 (adım: 0.05) |
| `keskinleştir` | Örtüşen splatların keskinliğini kontrol eder. 1.0 değeri fiziksel olarak doğru karıştırma sağlar. 1.0'ın üzerindeki değerler, splatları küçültmeden veya boşluklar açmadan daha keskin doku için her pikseli baskın (en yakın) splat'a yönlendirir (varsayılan: 2.0) | FLOAT | Evet | 1.0 ila 8.0 (adım: 0.5) |
| `far_gölgeleme` | Splat yüzey normalini kullanarak kamera konumundaki bir ışıktan gelen yaygın gölgelendirme. Görüşten uzaklaşan yüzeyleri karartarak form ve eğriliği ortaya çıkarır. 0 düz albedo verir, 1 en güçlü gölgelendirmeyi sağlar (varsayılan: 0.0) | FLOAT | Evet | 0.0 ila 3.0 (adım: 0.05) |
| `opaklık_eşiği` | Opaklığı bu eşiğin altında olan gaussianları ayıklar, böylece soluk yüzen parçacıkları kaldırır (varsayılan: 0.0) | FLOAT | Evet | 0.0 ila 1.0 (adım: 0.01) |
| `oluşturma_stili` | Görüntü çıktısının ne gösterdiği. Seçenekler: color (tam renkli işleme), clay (nötr albedo gölgeli), depth (yakın nesneler parlak görünür), normal (OpenGL normal haritası) (varsayılan: "color") | COMBO | Evet | "color"<br>"clay"<br>"depth"<br>"normal" |
| `arka_plan` | İşleme için düz arka plan rengi (varsayılan: #000000) | COLOR | Evet | - |
| `arka_plan_görseli` | Splat'ın arkasına yerleştirilen isteğe bağlı arka plan plakası. Düz arka plan rengini geçersiz kılar. İşleme boyutuna yeniden boyutlandırılır. Kare başına bir görüntü grubu kullanılır, tüm kareler için tek bir görüntü kullanılır. Yalnızca color ve clay işleme stilleriyle çalışır | IMAGE | Hayır | - |
| `camera_info` | İşleme yapılacak kamera. Load3D, Preview3D veya Create Camera Info düğümünden gelebilir. Boşsa, splat varsayılan 3/4 görünümden otomatik çerçevelenir | CAMERA_3D | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `görsel` | Gaussian splat'ın işlenmiş görüntüsü | IMAGE |
| `mask` | İşlenmiş splat'ın alfa maskesi | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderSplat/tr.md)

---
**Source fingerprint (SHA-256):** `038bd9fb032f347ecda665c03719a64b0cf907599b701606f5cf6d0606d19d98`
