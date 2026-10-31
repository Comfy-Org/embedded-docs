# MiniMax H3 Max Camera Control

Bu düğüm, sabit bir görüntüden başlayan ve kamerayı konu etrafında yeni bir açı ve mesafeye hareket ettiren bir video oluşturur. Azimut, yükseklik ve mesafe, kameranın nerede sonlanacağını tanımlar; ilk kare tam olarak sağlandığı gibi kalır. İstem verilmediğinde sahne donmuş kalır ve yalnızca kamera hareket eder.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video üretimi için kullanılacak model. | DYNAMIC_COMBO | Evet | "MiniMax H3 Max" |

### MiniMax H3 Max Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Videonun ilk karesi, en az 256x256 piksel. En-boy oranı 0.4 ile 2.5 arasında olmalıdır. | IMAGE | Evet | Tek görüntü |
| `camera_info` | İsteğe bağlı bitiş kamerası; örneğin Create Camera Info veya Compose Camera Angle Prompt düğümlerinden, görüntü ön görünüm olacak şekilde. Bağlandığında azimut ve yüksekliği ayarlar. | LOAD3D_CAMERA | Hayır | Kamera bilgisi |
| `prompt` | İsteğe bağlı. Boş olduğunda sahne donmuş kalır ve yalnızca kamera hareket eder. | STRING | Evet | 0 ile 50000 karakter arası |
| `azimuth` | Videonun sonunda konu etrafındaki yatay yörünge, görüntüden itibaren derece cinsinden (varsayılan: 90). Pozitif değerler kamerayı sağa hareket ettirir, böylece konu karenin soluna doğru döner. Bu bir hedeftir: 90 derecelik bir yörünge genellikle 30 ile 90 derece arasında sonuçlanır. `camera_info` bağlı olduğunda yok sayılır. | INT | Evet | -360 ile 360 arası |
| `elevation` | Videonun sonunda dikey kamera açısı, derece cinsinden (varsayılan: 0). Pozitif değerler yukarıdan aşağıya bakar, negatif değerler aşağıdan yukarıya bakar. `camera_info` bağlı olduğunda yok sayılır. | INT | Evet | -90 ile 90 arası |
| `distance` | Videonun sonunda görüntüye göre kamera mesafesi: 1 korur, 1'in altı yaklaşır, 1'in üstü uzaklaşır (varsayılan: 1.0). | FLOAT | Evet | 0.1 ile 10.0 arası |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 1 ile 15 arası |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: "768P"). | COMBO | Evet | "480P"<br>"768P"<br>"1080P" |
| `prompt_expansion_mode` | Üretimden önce istemin yeniden yazılması için ne kadar çaba harcanacağı (varsayılan: "balanced"). | COMBO | Evet | "disabled"<br>"balanced"<br>"quality" |
| `seed` | Rastgele tohum. Aynı tohumla aynı istek benzer, ancak aynı olduğu garanti edilmeyen sonuçlar verir (varsayılan: 42). | INT | Evet | 0 ile 4294967295 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Kamera hareketi uygulanmış oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxCameraControlNode/tr.md)

---
**Source fingerprint (SHA-256):** `d9eed1a3ae91891b974bea39ea00101c0577cf5b204d4c701b13b232e0604153`
