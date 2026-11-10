# Create Camera Orbit

İlk kameranın hedefi etrafında bir kamera düzeneği oluşturur: varsayılan olarak bir döner tabla, `pitch` ayarlandığında eğimli bir süpürme ve isteğe bağlı olarak doğrudan aşağı ve yukarı bakışlar. Render Mesh her kamera için bir görüntü oluşturur ve Bake Texture From Views bunları mesh üzerine geri yansıtır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `camera_info` | Yörüngenin ilk kamerası. Bir kamera listesi, içindeki her kameranın yörüngesini oluşturur. | LOAD3D_CAMERA | Evet | - |
| `count` | Süpürme boyunca eşit aralıklarla yerleştirilmiş kamera sayısı. Varsayılan: 4. | INT | Evet | 1 ile 64 arası |
| `yaw` | Hedef etrafındaki toplam dönüş; Create Camera Info'nun yaw yönünde. Tam turlar ilk kameradan bir adım önce durur; diğer süpürmeler son kamerada biter. Varsayılan: 360.0. | FLOAT | Evet | -720.0 ile 720.0 arası (adım: 1.0) |
| `pitch` | Hedef üzerindeki toplam eğim; pozitif değer Create Camera Info'nun pitch yönünde yükselir; 90'ı geçince kameralar tepenin üzerinden geçer. Tam turlar `yaw` gibi döngü yapar. Varsayılan: 0.0. | FLOAT | Evet | -720.0 ile 720.0 arası (adım: 1.0) |
| `poles` | Hedefe doğrudan aşağıdan ve/veya yukarıdan bakan görüşler; yörüngeden sonra eklenir. Görüntülerinin üst kısmı ilk kameradan uzağa bakar. Varsayılan: `"none"`. | COMBO | Evet | `"none"`<br>`"top"`<br>`"bottom"`<br>`"top and bottom"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `camera_info` | Düzeneğin kamera listesi; yörünge sırası ve ardından kutup görünümleri. | LOAD3D_CAMERA |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateCameraOrbit/tr.md)

---
**Source fingerprint (SHA-256):** `b251efc969f8db7cf03527594be3bbd2af037f1ebb56bdf508bf264ddd9f8c08`
