# Kamera Bilgisi Oluştur

Kamera Bilgisi Oluştur düğümü, 3D görüntüleme için bir kamera bilgi yapısı oluşturur. Kamerayı tanımlamak için üç modu destekler: yörünge (bir hedef etrafında yalpalama/eğim/mesafe), bakış (açık dünya konumu) ve dördül (konum artı dönüş). Koordinat sistemi, Y'nin yukarı eksen olduğu sağ ellidir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|----------|--------|
| `mod` | Kameranın nasıl tanımlanacağı: yörünge açıları, açık bir konum veya konum + dördül. | COMBO | Evet | `"orbit"`<br>`"look_at"`<br>`"quaternion"` |
| `hedef_x` | Bakış noktası (yörünge dönüş merkezi / nişan). Yörünge modunda, tüm kamerayı kaydırmak/taşımak için hareket ettirin. Dördül modunda yok sayılır. Varsayılan olarak orijin noktasıdır. (varsayılan: 0.0) | FLOAT | Hayır | -1000.0 ile 1000.0 arası |
| `hedef_y` | Hedef noktasının Y bileşeni. (varsayılan: 0.0) | FLOAT | Hayır | -1000.0 ile 1000.0 arası |
| `hedef_z` | Hedef noktasının Z bileşeni. (varsayılan: 0.0) | FLOAT | Hayır | -1000.0 ile 1000.0 arası |
| `roll` | Görüş ekseni etrafında kamera yatışı, derece cinsinden. (varsayılan: 0.0) | FLOAT | Hayır | -180.0 ile 180.0 arası |
| `fov` | Derece cinsinden dikey görüş alanı. (varsayılan: 35.0) | FLOAT | Hayır | 1.0 ile 120.0 arası |
| `zoom` | Dijital yakınlaştırma (odak uzaklığı çarpanı). 1'den büyük değerler kamerayı hareket ettirmeden yakınlaştırır. (varsayılan: 1.0) | FLOAT | Hayır | 0.01 ile 100.0 arası |
| `kamera_tipi` | Render Splat tarafından kullanılan izdüşüm: perspektif (küçültme) veya ortografik (paralel). (varsayılan: "perspective") | COMBO | Hayır | `"perspective"`<br>`"orthographic"` |

### Moda Özgü Parametreler

`mode` parametresi `"orbit"` olarak ayarlandığında, aşağıdaki parametreler kullanılabilir hale gelir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|----------|--------|
| `yaw` | Hedef etrafında yatay dönüş açısı. (varsayılan: 35.0) | FLOAT | Evet | -360.0 ile 360.0 arası |
| `pitch` | Hedef etrafında dikey dönüş açısı. (varsayılan: 30.0) | FLOAT | Evet | -89.0 ile 89.0 arası |
| `distance` | Kameranın hedefe olan mesafesi. (varsayılan: 4.0) | FLOAT | Evet | 0.01 ile 1000.0 arası |

`mode` parametresi `"look_at"` olarak ayarlandığında, aşağıdaki parametreler kullanılabilir hale gelir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|----------|--------|
| `position_x` | Dünya uzayında kamera konumu (sağ elli, Y yukarı). (varsayılan: 4.0) | FLOAT | Evet | -1000.0 ile 1000.0 arası |
| `position_y` | Kamera konumunun Y bileşeni. (varsayılan: 4.0) | FLOAT | Evet | -1000.0 ile 1000.0 arası |
| `position_z` | Kamera konumunun Z bileşeni. (varsayılan: 4.0) | FLOAT | Evet | -1000.0 ile 1000.0 arası |

`mode` parametresi `"quaternion"` olarak ayarlandığında, aşağıdaki parametreler kullanılabilir hale gelir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|----------|--------|
| `position_x` | Dünya uzayında kamera konumu (sağ elli, Y yukarı). (varsayılan: 4.0) | FLOAT | Evet | -1000.0 ile 1000.0 arası |
| `position_y` | Kamera konumunun Y bileşeni. (varsayılan: 4.0) | FLOAT | Evet | -1000.0 ile 1000.0 arası |
| `position_z` | Kamera konumunun Z bileşeni. (varsayılan: 4.0) | FLOAT | Evet | -1000.0 ile 1000.0 arası |
| `quat_x` | Kamera dünya dönüş dördülünün X bileşeni. (varsayılan: 0.0) | FLOAT | Evet | -1.0 ile 1.0 arası |
| `quat_y` | Kamera dünya dönüş dördülünün Y bileşeni. (varsayılan: 0.0) | FLOAT | Evet | -1.0 ile 1.0 arası |
| `quat_z` | Kamera dünya dönüş dördülünün Z bileşeni. (varsayılan: 0.0) | FLOAT | Evet | -1.0 ile 1.0 arası |
| `quat_w` | Kamera dünya dönüş dördülü (three.js: yerel -Z yönüne bakar). Sizin için normalize edilir. (varsayılan: 1.0) | FLOAT | Evet | -1.0 ile 1.0 arası |

**Not:** `target_x`, `target_y` ve `target_z` parametreleri, `mode` `"quaternion"` olarak ayarlandığında yok sayılır. `"orbit"` modunda, bu hedef parametreleri kameranın etrafında döndüğü dönüş noktasını tanımlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `kamera_bilgisi` | 3D görüntüleme için konum, dönüş, görüş alanı, yakınlaştırma ve izdüşüm türünü içeren kamera bilgi yapısı. | LOAD3DCAMERA |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateCameraInfo/tr.md)

---
**Source fingerprint (SHA-256):** `577c114130f72b753d5f15775fe05b3e1e734f5865cca32c576d042583f8e873`
