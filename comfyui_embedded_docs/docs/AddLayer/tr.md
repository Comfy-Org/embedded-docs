# AddLayer

Add Layer düğümü, bir girdi görüntüsünü katmana dönüştürür ve onu tuval üzerine yerleştirir; ya yeni bir katman yığını başlatır ya da mevcut bir katman yığınına ekler. Katmanın adını, konumunu, boyutunu, dönüşünü, opaklığını, karışım modunu, istifleme sırasını ve yatay veya dikey çevirme özelliklerini ayarlayabilirsiniz. Bu düğüm deneysel olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `katmanlar` | Eklenecek katman yığını. Yeni bir yığın başlatmak için bağlantısız bırakın. | LAYERS | Hayır | — |
| `görüntü` | Katman içeriği, doğal boyutunda. Bir grup, ardışık katmanlara genişler. | IMAGE | Evet | — |
| `maske` | Bu katman için saydamlık maskesi. Maskeli alanlar (değer 1) saydam hale gelir ve görüntünün zaten sahip olduğu alfa kanalıyla çarpılır. | MASK | Hayır | — |
| `isim` | Birleştirici düzenleyicide gösterilen katman adı. (varsayılan: "") | STRING | Hayır | — |
| `x` | Tuval üzerindeki başlangıç yatay konumu. (varsayılan: 0) | INT | Hayır | -MAX_RESOLUTION ile MAX_RESOLUTION |
| `y` | Tuval üzerindeki başlangıç dikey konumu. (varsayılan: 0) | INT | Hayır | -MAX_RESOLUTION ile MAX_RESOLUTION |
| `opaklık` | Başlangıç katman opaklığı. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 ile 1.0 (adım: 0.01) |
| `karışım_modu` | Alttaki katmanlara uygulanan başlangıç karışım modu. Varsayılan saydam arka plan üzerindeki en alt katmanda, normal olmayan modlar saydamlık üretir. (varsayılan: "normal") | COMBO | Hayır | Birden fazla seçenek mevcut |
| `dönüş` | Derece cinsinden başlangıç dönüşü, saat yönünde. (varsayılan: 0.0) | FLOAT | Hayır | -360.0 ile 360.0 (adım: 1.0) |
| `genişlik` | Başlangıç görüntüleme genişliği. 0, görüntünün doğal genişliğini korur. (varsayılan: 0) | INT | Hayır | 0 ile MAX_RESOLUTION |
| `yükseklik` | Başlangıç görüntüleme yüksekliği. 0, görüntünün doğal yüksekliğini korur. (varsayılan: 0) | INT | Hayır | 0 ile MAX_RESOLUTION |
| `z_indeksi` | İstifleme geçersiz kılma. Katmanlar z_index'e göre kararlı şekilde sıralanır; eşit değerler liste sıralarını korur. (varsayılan: 0) | INT | Hayır | -1000 ile 1000 |
| `yatay_çevir` | Katmanı yatay olarak çevir. (varsayılan: False) | BOOLEAN | Hayır | false / true |
| `dikey_çevir` | Katmanı dikey olarak çevir. (varsayılan: False) | BOOLEAN | Hayır | false / true |

Notlar:
- Yalnızca `image` gereklidir; diğer tüm girdiler isteğe bağlıdır.
- `layers` bağlantısız bırakıldığında yeni bir katman yığını oluşturulur. Bir katman yığını bağlandığında, yeni katman ona eklenir.
- `image` girdisindeki bir görüntü grubu, birden fazla ardışık katman oluşturur.
- `width` ve `height` varsayılan olarak 0'dır; bu, görüntünün doğal boyutlarını korur. 0'dan büyük değerler görüntüleme boyutunu geçersiz kılar.
- `opacity`, `blend_mode`, `rotation`, `width` ve `height` yalnızca varsayılan değerlerinden farklı olduklarında uygulanır.
- Bağlı bir katman yığınının tuval boyutu çıktıda korunur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `layers` | Bu katmanın eklendiği katman yığını. | LAYERS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddLayer/tr.md)

---
**Source fingerprint (SHA-256):** `b7bf1a012d17cb5768b49d5c0617e13562ba015f695e6c9b1d1bbefba4150f9e`
