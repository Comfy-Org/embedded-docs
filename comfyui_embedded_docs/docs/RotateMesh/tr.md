# RotateMesh

Bir 3D mesh'i, Euler XYZ açılarını (derece cinsinden) veya bir kuaterniyonu kullanarak dünya eksenleri etrafında döndürür. Döndürme, mesh'in köşelerine uygulanır; normaller ve teğetler de döndürülerek aydınlatma ve gölgelendirmenin doğru kalması sağlanır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mode` | Kullanılacak döndürme modu. `"euler_xyz"` döndürmeyi dünya eksenleri etrafında sırasıyla X, Y ve Z açıları (derece cinsinden) olarak uygular. `"quaternion"` otomatik olarak normalleştirilen bir (w, x, y, z) kuaterniyonu kullanır. | DYNAMIC_COMBO | Evet | `"euler_xyz"`<br>`"quaternion"` |
| `mesh` | Döndürülecek 3B mesh. | MESH | Evet | — |

### euler_xyz Girdileri

Bu girdiler, `mode` `"euler_xyz"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `angle_x` | X ekseni etrafında derece cinsinden döndürme. (varsayılan: 0.0) | FLOAT | Hayır | -360.0 to 360.0 (step: 0.1) |
| `angle_y` | Y ekseni etrafında derece cinsinden döndürme. (varsayılan: 0.0) | FLOAT | Hayır | -360.0 to 360.0 (step: 0.1) |
| `angle_z` | Z ekseni etrafında derece cinsinden döndürme. (varsayılan: 0.0) | FLOAT | Hayır | -360.0 to 360.0 (step: 0.1) |

### quaternion Girdileri

Bu girdiler, `mode` `"quaternion"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `qw` | Kuaterniyonun (w, x, y, z) W bileşeni. (varsayılan: 1.0) | FLOAT | Hayır | -1.0 to 1.0 (step: 0.001) |
| `qx` | Kuaterniyonun (w, x, y, z) X bileşeni. (varsayılan: 0.0) | FLOAT | Hayır | -1.0 to 1.0 (step: 0.001) |
| `qy` | Kuaterniyonun (w, x, y, z) Y bileşeni. (varsayılan: 0.0) | FLOAT | Hayır | -1.0 to 1.0 (step: 0.001) |
| `qz` | Kuaterniyonun (w, x, y, z) Z bileşeni. (varsayılan: 0.0) | FLOAT | Hayır | -1.0 to 1.0 (step: 0.001) |

**Not:** `mode` `"euler_xyz"` iken üç açının tümü 0.0 olduğunda veya `mode` `"quaternion"` iken kuaterniyon birim (1, 0, 0, 0) olduğunda, mesh değiştirilmeden döndürülür. Kuaterniyon kullanımdan önce otomatik olarak normalleştirilir; büyüklüğü sıfıra çok yakınsa düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Döndürülmüş mesh. Köşeler döndürülür ve normaller yönler olarak döndürülür. Teğetlerin X, Y, Z bileşenleri döndürülürken W (yönlülük) bileşeni değiştirilmeden korunur. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RotateMesh/tr.md)

---
**Source fingerprint (SHA-256):** `38b120a3f719264d1269275ecfefa145b507c688735e4a461bb89517c697674f`
