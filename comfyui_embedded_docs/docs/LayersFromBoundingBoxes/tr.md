# LayersFromBoundingBoxes

Bu düğüm, bir görüntü kümesini ve sınırlayıcı kutularını bir katman yığınına dönüştürür; her kare için bir katman oluşturur ve her katmanı eşleşen kutusuna göre yerleştirir. Bir düğüm katmanları bir küme olarak çıktıladığında bunu kullanın; çünkü bir küme her kare için yalnızca tek bir yerleşim taşır ve aksi takdirde tek tek konumlar kaybolur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görsel` | Görüntü kümesi; her kare bir katman olur. | IMAGE | Evet | — |
| `sınırlayıcı_kutular` | Yerleştirme kutuları, görüntü kümesiyle dizin hizalıdır. Sınırlayıcı kutuları (x, y, genişlik, yükseklik), normalleştirilmiş öğeleri ("bbox" içeren — bunlar piksele dönüştürülmek için canvas_width/canvas_height gerektirir) veya bunlardan birinin JSON dizgesini kabul eder. Eşleşen kutusu olmayan kareler orijine yerleştirilir. Bir kutunun genişliği/yüksekliği, katmanı ona sığacak şekilde ölçekler. metadata.name (veya desc) ve metadata.z_index varsa kullanılır; metadata.content_rect (kareye göreli) kareyi gerçek içeriğine göre kırpar. | BOUNDING_BOX, ARRAY veya STRING | Evet | — |
| `maske` | Kare başına saydamlık, görüntü kümesiyle dizin hizalıdır (1 = saydam, LoadImage kuralı). | MASK | Hayır | — |
| `katmanlar` | Eklenecek katman yığını. Yeni bir yığın başlatmak için bağlantısız bırakın. | LAYERS | Hayır | — |
| `içeriğe_kırp` | Her kareyi, varsa metadata.content_rect'e göre kırpın ve içeriği kutu konumu artı dikdörtgen ofsetiyle yerleştirin. Kareleri dolgulu olan kümeler için açık bırakın — yalnızca gerçek içeriği gerçek konumunda tutar. (varsayılan: true) | BOOLEAN | Hayır | true<br>false |
| `tuval_genişliği` | Belge tuvali genişliği. 0, yerleştirilen katmanlardan türetir. (varsayılan: 0) | INT | Hayır | 0 ile MAX_RESOLUTION |
| `tuval_yüksekliği` | Belge tuvali yüksekliği. 0, yerleştirilen katmanlardan türetir. (varsayılan: 0) | INT | Hayır | 0 ile MAX_RESOLUTION |

Notlar:

- `bboxes` ve `mask`, `image` ile dizin hizalı olmalıdır: n. kutu ve n. maske karesi, n. görüntü karesine karşılık gelir. Eşleşen kutusu olmayan kareler orijine yerleştirilir.
- `bboxes` normalleştirilmiş öğeler içerdiğinde ("bbox" ile), bu normalleştirilmiş konumların piksele dönüştürülebilmesi için `canvas_width` ve `canvas_height` sağlanmalıdır.
- Belge tuvalini açıkça ayarlamak için `canvas_width` ve `canvas_height` değerlerinin her ikisi de 0'dan büyük olmalıdır. Herhangi biri 0 ise, tuval yerleştirilen katmanlardan türetilir veya bağlı `layers` yığınından devralınır.
- `layers` bağlı olduğunda, yeni katmanlar ona eklenir ve yığında zaten mevcut olan en yüksek z-index değerinin üzerinde z-index değerleri alır.
- `crop_to_content` etkinleştirildiğinde ve bir karede metadata.content_rect varsa, kare bu dikdörtgene kırpılır ve kutunun genişlik/yükseklik ölçeklemesi uygulanmaz; bunun yerine, dikdörtgenin ofseti kutu konumuna eklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `LAYERS` | Create Layered Image için hazır katman yığını. | LAYERS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LayersFromBoundingBoxes/tr.md)

---
**Source fingerprint (SHA-256):** `a70956bf0d7ea8bdbd16767ed8b19600b274a6eeb745728f95219578adc73712`
