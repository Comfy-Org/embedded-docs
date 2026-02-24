> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProEditVideoNode/tr.md)

Kling Omni Edit Video (Pro) düğümü, mevcut bir videoyu metin açıklamasına dayanarak düzenlemek için bir AI modeli kullanır. Bir kaynak video ve bir prompt sağlarsınız, düğüm de istenen değişikliklerle aynı uzunlukta yeni bir video oluşturur. İsteğe bağlı olarak tarzı yönlendirmek için referans görseller kullanabilir ve kaynak videodan orijinal sesi koruyabilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Evet | `"kling-video-o1"` | Video düzenleme için kullanılacak AI modeli. |
| `prompt` | STRING | Evet | | Video içeriğini tanımlayan bir metin prompt'u. Bu, hem olumlu hem de olumsuz açıklamalar içerebilir. |
| `video` | VIDEO | Evet | | Düzenlenecek video. Çıktı videosunun uzunluğu aynı olacaktır. |
| `keep_original_sound` | BOOLEAN | Evet | | Giriş videosundan gelen orijinal sesin çıktıda korunup korunmayacağını belirler (varsayılan: True). |
| `reference_images` | IMAGE | Hayır | | En fazla 4 ek referans görseli. |
| `resolution` | COMBO | Hayır | `"1080p"`<br>`"720p"` | Çıktı videosu için çözünürlük (varsayılan: "1080p"). |

**Kısıtlamalar ve Sınırlamalar:**

* `prompt` 1 ile 2500 karakter arasında olmalıdır.
* Giriş `video` süresi 3.0 ile 10.05 saniye arasında olmalıdır.
* Giriş `video` boyutları 720x720 ile 2160x2160 piksel arasında olmalıdır.
* Bir video kullanıldığında en fazla 4 `reference_images` sağlanabilir.
* Her bir `reference_image` en az 300x300 piksel olmalıdır.
* Her bir `reference_image` en boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | AI modeli tarafından oluşturulan düzenlenmiş video. |
