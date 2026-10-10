# Compose Camera Angle Prompt

Bu düğüm, bir öznenin etrafındaki kamera açısını seçer ve bu seçimi iki şeye dönüştürür: 3B düğümlerin render edebileceği bir `camera_info` yapısı ve bir isteme yapıştırabileceğiniz sade İngilizce çekim açıklaması. Özne, sahnenin orijininde yer alır; alt akıştaki 3B düğümler modellerini burada ortalar, böylece burada seçtiğiniz açı önizlemeyle eşleşir.

Bunu, oluşturmadan önce bir render'ı çerçevelemek veya bir görsel ya da video modeli için `front view eye-level shot medium shot` gibi bir bakış açısını tanımlamak için kullanın. Düğümdeki 3B önizleme, ortaya çıkan kamera konumunu gösterir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `horizontal_angle` | Özne etrafındaki azimut, derece cinsinden: 0 ön, 90 sağ taraf ve 180 arkadır. (varsayılan: 0) | INT | Evet | 0 ile 360 arası |
| `vertical_angle` | Yükseklik açısı, derece cinsinden. Negatif değerler aşağıdan yukarıya bakar, pozitif değerler yukarıdan aşağıya bakar. (varsayılan: 0) | INT | Evet | -30 ile 60 arası |
| `zoom` | Öznede lens yakınlaştırması: 0 geniş çekim, 10 yakın çekimdir. Değer ayrıca `camera_info.zoom` içine taşınır. (varsayılan: 5.0) | FLOAT | Evet | 0.0 ile 10.0 arası (adım: 0.1) |
| `image` | İsteğe bağlı referans görseli; 3B önizlemede özne küpünün ön yüzünde gösterilir. | IMAGE | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `camera_info` | 3B düğümler için kamera bilgileri: konum, bakış hedefi, yakınlaştırma faktörü, kamera türü ve görüş alanı. Kamera sabit 35 derece görüş alanını korur ve hedeften 6 birim uzağa yerleştirilir. | LOAD3DCAMERA |
| `prompt` | Açı, yükseklik ve mesafeden oluşturulan kısa çekim açıklaması; örneğin `front view eye-level shot medium shot`. | STRING |

## Çekim Açıklaması Terimleri

`prompt` çıktısı aşağıdaki her gruptan bir terim birleştirir. Değerler önce widget aralıklarına kırpılır.

- Yatay açı, 45 derecelik sekiz sektöre ayrılır: `front view`, `front-right quarter view`, `right side view`, `back-right quarter view`, `back view`, `back-left quarter view`, `left side view`, `front-left quarter view`.
- Dikey açı -15 derecenin altında `low-angle shot`, 15'in altında `eye-level shot`, 45'in altında `elevated shot` ve 45 dereceden yukarısı için `high-angle shot` olur.
- Yakınlaştırma 2'nin altında `wide shot`, 6'nın altında `medium shot` ve 6 veya daha fazlasında `close-up` olur.

`camera_info.zoom` faktörü, widget değerini 1.0 ile 1.875 aralığına ölçekler; böylece zoom 0, 1.0 verir ve zoom 10, 1.875 verir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CameraAngle/tr.md)

---
**Source fingerprint (SHA-256):** `8ed2cd186bc6ca02dbc8da006b2e9156245ef691a2257f286f6e32ffa480fd5d`
