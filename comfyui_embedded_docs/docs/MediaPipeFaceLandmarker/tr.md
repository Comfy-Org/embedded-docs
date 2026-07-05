# MediaPipe Yüz İşaretleyici

## Genel Bakış

Bir görüntüdeki yüzleri algılar ve MediaPipe'in BlazeFace ile FaceMesh modellerini kullanarak her yüzde 468 yüz işaret noktasını (anahtar noktalar) tanımlar. Ayrıca yüz ifadesi analizi için ARKit-52 karışım şekli katsayılarını hesaplar. Düğüm, toplu halde birden fazla görüntüyü işleyebilir ve algılanan her yüz için hem işaret noktası verilerini hem de sınırlayıcı kutuları çıktı olarak verir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `face_detection_model` | İşaret noktası algılama için kullanılacak MediaPipe yüz algılama modeli. | FACE_DETECTION_MODEL | Evet |  |
| `image` | Yüz algılanacak giriş görüntüsü veya görüntü topluluğu. | IMAGE | Evet |  |
| `detector_variant` | Yüz algılayıcı menzili. `"short"`, yakın çekim yüzler için ayarlanmıştır (kameradan ~2 m içinde); `"full"`, daha uzak/küçük yüzleri kapsar (~5 m'ye kadar) ancak daha yavaştır. `"both"`, her iki algılayıcıyı da çalıştırır ve kare başına daha fazla yüz bulanı korur (~2x algılama maliyeti). Varsayılan: `"short"`. | COMBO | Evet | `"short"`<br>`"full"`<br>`"both"` |
| `num_faces` | Kare başına döndürülecek maksimum yüz sayısı. 0, sınır yok anlamına gelir (algılanan tüm yüzleri döndürür). Varsayılan: 1. | INT | Evet | 0 ile 16 |
| `min_confidence` | BlazeFace puan eşiği. Daha düşük değerler, küçük veya kısmen görünen yüzleri yakalamaya yardımcı olur. Varsayılan: 0,5. | FLOAT | Hayır | 0,00 ile 1,00 |
| `missing_frame_fallback` | Bir toplulukta algılama başarısız olduğunda kare başına davranış. `"empty"`, kareyi yüzsüz bırakır. `"previous"`, en son başarılı algılamayı kopyalar. `"interpolate"`, başarılı kareler arasında işaret noktaları/sınırlayıcı kutular/karışım şekilleri arasında doğrusal enterpolasyon yapar. Çoklu yüz: yüzleri kareler arasında açgözlü sınırlayıcı kutu merkezi NN ile eşleştirir. Varsayılan: `"empty"`. | COMBO | Hayır | `"empty"`<br>`"previous"`<br>`"interpolate"` |


| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `face_landmarks` | Kare başına yüz algılama sonuçlarını içeren yapılandırılmış bir çıktı. 468 yüz işaret noktası, ARKit-52 karışım şekli katsayıları, dönüşüm matrisleri ve ağ görselleştirme için bağlantı kümelerini içerir. | FACE_LANDMARKS |
| `bboxes` | Algılanan her yüz için sınırlayıcı kutuların listesi; koordinatlar (x, y, genişlik, yükseklik), "yüz" etiketi ve güven puanı ile birlikte. Giriş karesi başına bir liste. | BOUNDING_BOX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceLandmarker/tr.md)

---
**Source fingerprint (SHA-256):** `f60ed6201288a59d65d62cc98c12f227a353870c36decea8da81a063cfdf2bba`
