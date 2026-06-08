Kling Omni Video Düzenleme (Pro) düğümü, mevcut bir videoyu metin açıklamasına göre düzenlemek için bir yapay zeka modeli kullanır. Bir kaynak video ve bir istem sağlarsınız; düğüm, istenen değişikliklerle aynı uzunlukta yeni bir video oluşturur. İsteğe bağlı olarak, stili yönlendirmek için referans görseller kullanabilir ve kaynak videodaki orijinal sesi koruyabilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model_adı` | Video düzenleme için kullanılacak yapay zeka modeli (varsayılan: `"kling-v3-omni"`). | COMBO | Evet | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `istem` | Video içeriğini tanımlayan bir metin istemi. Bu, hem olumlu hem de olumsuz açıklamalar içerebilir. | STRING | Evet |  |
| `video` | Düzenlenecek video. Çıktı videosunun uzunluğu aynı olacaktır. | VIDEO | Evet |  |
| `orijinal_sesi_koru` | Giriş videosundaki orijinal sesin çıktıda tutulup tutulmayacağını belirler (varsayılan: True). | BOOLEAN | Evet |  |
| `referans_görseller` | En fazla 4 adet ek referans görseli. | IMAGE | Hayır |  |
| `çözünürlük` | Çıktı videosunun çözünürlüğü (varsayılan: `"1080p"`). | COMBO | Hayır | `"1080p"`<br>`"720p"` |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Hayır | 0 ile 2147483647 arası |

**Kısıtlamalar ve Sınırlamalar:**

* `prompt` 1 ile 2500 karakter arasında olmalıdır.
* Giriş `video` 3,0 ile 10,05 saniye arasında bir süreye sahip olmalıdır.
* Giriş `video` boyutları 720x720 ile 2160x2160 piksel arasında olmalıdır.
* Bir video kullanıldığında en fazla 4 `reference_images` sağlanabilir.
* Her `reference_image` en az 300x300 piksel olmalıdır.
* Her `reference_image` 1:2,5 ile 2,5:1 arasında bir en-boy oranına sahip olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Yapay zeka modeli tarafından oluşturulan düzenlenmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProEditVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `ddc3fdc8c97cdcdd34f16a0916b13ffe6adeb46e58e2933516c9a6aef7c36730`
