> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProCannyNode/tr.md)

# FluxProCannyNode

Bir kontrol görüntüsü (canny) kullanarak görüntü oluşturun. Bu düğüm, bir kontrol görüntüsü alır ve kontrol görüntüsünde algılanan kenar yapısını takip ederek sağlanan istem doğrultusunda yeni bir görüntü oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `control_image` | IMAGE | Evet | - | Canny kenar algılama kontrolü için kullanılan giriş görüntüsü |
| `prompt` | STRING | Hayır | - | Görüntü oluşturma için istem (varsayılan: boş dize) |
| `prompt_upsampling` | BOOLEAN | Hayır | - | İstem üzerinde yukarı örnekleme yapılıp yapılmayacağı. Etkinleştirilirse, daha yaratıcı oluşturma için istemi otomatik olarak değiştirir, ancak sonuçlar deterministik değildir (aynı tohum değeri tam olarak aynı sonucu üretmez). (varsayılan: False) |
| `canny_low_threshold` | FLOAT | Hayır | 0.01 - 0.99 | Canny kenar algılama için düşük eşik değeri; `skip_preprocessing` True ise yok sayılır (varsayılan: 0.1) |
| `canny_high_threshold` | FLOAT | Hayır | 0.01 - 0.99 | Canny kenar algılama için yüksek eşik değeri; `skip_preprocessing` True ise yok sayılır (varsayılan: 0.4) |
| `skip_preprocessing` | BOOLEAN | Hayır | - | Ön işlemenin atlanıp atlanmayacağı; `control_image` zaten canny uygulanmışsa True, ham görüntü ise False olarak ayarlayın. (varsayılan: False) |
| `guidance` | FLOAT | Hayır | 1 - 100 | Görüntü oluşturma süreci için yönlendirme gücü (varsayılan: 30) |
| `steps` | INT | Hayır | 15 - 50 | Görüntü oluşturma süreci için adım sayısı (varsayılan: 50) |
| `seed` | INT | Hayır | 0 - 18446744073709551615 | Gürültü oluşturmak için kullanılan rastgele tohum değeri. (varsayılan: 0) |

**Not:** `skip_preprocessing` True olarak ayarlandığında, `canny_low_threshold` ve `canny_high_threshold` parametreleri yok sayılır çünkü kontrol görüntüsünün zaten canny kenar görüntüsü olarak işlenmiş olduğu varsayılır. Bu durumda `control_image`, ön işlenmiş görüntü olarak doğrudan kullanılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `output_image` | IMAGE | Kontrol görüntüsü ve istem temel alınarak oluşturulan görüntü |

---
**Source fingerprint (SHA-256):** `dedf55a2b2c183519d7f5be0d9a96abbe40716a247f574fc0d50f10f715949a7`
