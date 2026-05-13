> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProDepthNode/tr.md)

Bu düğüm, derinlik kontrol görüntüsünü kılavuz olarak kullanarak görüntüler oluşturur. Bir kontrol görüntüsü ve bir metin istemi alır, ardından hem kontrol görüntüsündeki derinlik bilgisini hem de istemdeki açıklamayı takip eden yeni bir görüntü oluşturur. Düğüm, görüntü oluşturma işlemini gerçekleştirmek için harici bir API'ye bağlanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `control_image` | IMAGE | Evet | - | Görüntü oluşturmayı yönlendirmek için kullanılan derinlik kontrol görüntüsü |
| `prompt` | STRING | Hayır | - | Görüntü oluşturma için istem (varsayılan: boş dize) |
| `prompt_upsampling` | BOOLEAN | Hayır | - | İstem üzerinde yukarı örnekleme yapılıp yapılmayacağı. Etkinse, daha yaratıcı oluşturma için istemi otomatik olarak değiştirir, ancak sonuçlar deterministik değildir (aynı tohum, tam olarak aynı sonucu üretmez). (varsayılan: Yanlış) |
| `skip_preprocessing` | BOOLEAN | Hayır | - | Ön işlemenin atlanıp atlanmayacağı; `control_image` zaten derinlik haritasına dönüştürülmüşse Doğru, ham bir görüntüyse Yanlış olarak ayarlayın. (varsayılan: Yanlış) |
| `guidance` | FLOAT | Hayır | 1-100 | Görüntü oluşturma süreci için kılavuzluk gücü (varsayılan: 15) |
| `steps` | INT | Hayır | 15-50 | Görüntü oluşturma süreci için adım sayısı (varsayılan: 50) |
| `seed` | INT | Hayır | 0-18446744073709551615 | Gürültü oluşturmak için kullanılan rastgele tohum. (varsayılan: 0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output_image` | IMAGE | Derinlik kontrol görüntüsü ve isteme dayalı olarak oluşturulan görüntü |

---
**Source fingerprint (SHA-256):** `34b80d7d63158b7dc4ad02da6b3a573b713d77efd0955d3477409f776f964462`
