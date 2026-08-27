# RotateMesh

Bir 3B ağı dünya eksenleri etrafında Euler XYZ açılarını (derece cinsinden) veya bir kuaterniyon kullanarak döndürün. Döndürme ağın köşelerine uygulanır; normaller ve teğetler de döndürülerek aydınlatma ve gölgelemenin doğru kalması sağlanır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mod` | Kullanılacak döndürme modu. `"euler_xyz"`, dünya eksenleri etrafında X, sonra Y, sonra Z açıları olarak döndürmeyi uygular (derece cinsinden). `"quaternion"`, otomatik olarak normalleştirilen bir (w, x, y, z) kuaterniyonu kullanır. | DYNAMIC_COMBO | Evet | `"euler_xyz"`<br>`"quaternion"` |
| `ağ` | Döndürülecek 3B ağ. | MESH | Evet | — |

### euler_xyz Girdileri

Bu girdiler `mode` `"euler_xyz"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `angle_x` | X ekseni etrafında derece cinsinden döndürme. (varsayılan: 0.0) | FLOAT | Hayır | -360.0 ile 360.0 (adım: 0.1) |
| `angle_y` | Y ekseni etrafında derece cinsinden döndürme. (varsayılan: 0.0) | FLOAT | Hayır | -360.0 ile 360.0 (adım: 0.1) |
| `angle_z` | Z ekseni etrafında derece cinsinden döndürme. (varsayılan: 0.0) | FLOAT | Hayır | -360.0 ile 360.0 (adım: 0.1) |

### quaternion Girdileri

Bu girdiler `mode` `"quaternion"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `qw` | Kuaterniyonun W bileşeni (w, x, y, z). (varsayılan: 1.0) | FLOAT | Hayır | -1.0 ile 1.0 (adım: 0.001) |
| `qx` | Kuaterniyonun X bileşeni (w, x, y, z). (varsayılan: 0.0) | FLOAT | Hayır | -1.0 ile 1.0 (adım: 0.001) |
| `qy` | Kuaterniyonun Y bileşeni (w, x, y, z). (varsayılan: 0.0) | FLOAT | Hayır | -1.0 ile 1.0 (adım: 0.001) |
| `qz` | Kuaterniyonun Z bileşeni (w, x, y, z). (varsayılan: 0.0) | FLOAT | Hayır | -1.0 ile 1.0 (adım: 0.001) |

**Not:** `mode` `"euler_xyz"` iken üç açının tümü 0.0 olduğunda veya `mode` `"quaternion"` iken kuaterniyon birim (1, 0, 0, 0) olduğunda ağ değiştirilmeden döndürülür. Kuaterniyon kullanımdan önce otomatik olarak normalleştirilir; büyüklüğü sıfıra çok yakınsa düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Döndürülmüş ağ. Köşeler döndürülür ve normaller yönler olarak döndürülür. Teğetlerin X, Y, Z bileşenleri döndürülürken W (yönlülük) bileşeni değiştirilmeden korunur. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RotateMesh/tr.md)

---
**Source fingerprint (SHA-256):** `38b120a3f719264d1269275ecfefa145b507c688735e4a461bb89517c697674f`
