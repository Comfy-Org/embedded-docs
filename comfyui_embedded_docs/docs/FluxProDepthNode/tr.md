Bu düğüm, derinlik kontrol görüntüsünü kılavuz olarak kullanarak görüntüler oluşturur. Bir kontrol görüntüsü ve bir metin istemi alır, ardından hem kontrol görüntüsündeki derinlik bilgisini hem de istemdeki açıklamayı takip eden yeni bir görüntü oluşturur. Düğüm, görüntü oluşturma işlemini gerçekleştirmek için harici bir API'ye bağlanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `control_image` | Görüntü oluşturmayı yönlendirmek için kullanılan derinlik kontrol görüntüsü | IMAGE | Evet | - |
| `prompt` | Görüntü oluşturma için istem (varsayılan: boş dize) | STRING | Hayır | - |
| `prompt_upsampling` | İstem üzerinde yukarı örnekleme yapılıp yapılmayacağı. Etkinse, daha yaratıcı oluşturma için istemi otomatik olarak değiştirir, ancak sonuçlar deterministik değildir (aynı tohum, tam olarak aynı sonucu üretmez). (varsayılan: Yanlış) | BOOLEAN | Hayır | - |
| `skip_preprocessing` | Ön işlemenin atlanıp atlanmayacağı; `control_image` zaten derinlik haritasına dönüştürülmüşse Doğru, ham bir görüntüyse Yanlış olarak ayarlayın. (varsayılan: Yanlış) | BOOLEAN | Hayır | - |
| `guidance` | Görüntü oluşturma süreci için kılavuzluk gücü (varsayılan: 15) | FLOAT | Hayır | 1-100 |
| `steps` | Görüntü oluşturma süreci için adım sayısı (varsayılan: 50) | INT | Hayır | 15-50 |
| `seed` | Gürültü oluşturmak için kullanılan rastgele tohum. (varsayılan: 0) | INT | Hayır | 0-18446744073709551615 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output_image` | Derinlik kontrol görüntüsü ve isteme dayalı olarak oluşturulan görüntü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProDepthNode/tr.md)

---
**Source fingerprint (SHA-256):** `34b80d7d63158b7dc4ad02da6b3a573b713d77efd0955d3477409f776f964462`
