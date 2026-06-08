# MoGe Çıkarımı

## Genel Bakış

MoGe'yi tek bir görüntü üzerinde çalıştırarak derinlik ve geometri tahmini yapın. Bu düğüm, giriş görüntüsünü MoGe modeli aracılığıyla işleyerek 3B nokta bulutu, derinlik haritası, kamera iç parametreleri, bir maske ve yüzey normalleri oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `moge_model` | Çıkarım için kullanılacak MoGe modeli. | MOGE_MODEL | Evet | Yok |
| `image` | Derinlik ve geometri tahmini için giriş görüntüsü. | IMAGE | Evet | Yok |
| `resolution_level` | İşleme çözünürlüğünü kontrol eder. 0 en hızlı, 9 en fazla detayı sağlar. (varsayılan: 9) | INT | Evet | 0 ile 9 |
| `fov_x_degrees` | Kaynak kameranın derece cinsinden yatay görüş alanı. Derinlik haritasını 3B'ye dönüştürmek için kullanılan odak uzunluğunu ayarlar. Tahmin edilen noktalardan görüş alanını otomatik olarak kurtarmak için 0,0 olarak ayarlayın. (varsayılan: 0,0) | FLOAT | Evet | 0,0 ile 170,0 |
| `batch_size` | Her çıkarım çağrısında işlenen görüntü sayısı. Uzun videoları veya büyük görüntü kümelerini işlerken bellek sorunu yaşıyorsanız bu değeri düşürün. (varsayılan: 4) | INT | Evet | 1 ile 64 |
| `force_projection` | (Gelişmiş) Tahmin edilen noktaların izdüşümünü zorlar. (varsayılan: Doğru) | BOOLEAN | Evet | Doğru/Yanlış |
| `apply_mask` | Etkinleştirildiğinde, maskelenmiş (gökyüzü veya geçersiz) pikselleri nokta ve derinlik çıktılarında sonsuz olarak ayarlar. Bu, örgü oluşturma araçlarının bu alanları yok saymasına yardımcı olur. Ham tahmin edilen geometriyi her yerde tutmak için devre dışı bırakın; maske yine de ayrı olarak döndürülür. (varsayılan: Doğru) | BOOLEAN | Evet | Doğru/Yanlış |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `moge_geometry` | Tahmin edilen geometriyi içeren bir sözlük. Orijinal `image`'i içerir ve `points` (3B nokta bulutu), `depth` (derinlik haritası), `intrinsics` (kamera iç parametre matrisi), `mask` (geçerli pikselleri tanımlayan maske) ve `normal` (yüzey normalleri) içerebilir. | MOGE_GEOMETRY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/tr.md)

---
**Source fingerprint (SHA-256):** `5213b280513850eeef2e22ae723ebb015789109435e28ddd79f91f9a4b4a1e79`
