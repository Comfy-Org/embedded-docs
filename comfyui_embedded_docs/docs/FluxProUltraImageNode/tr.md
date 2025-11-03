> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProUltraImageNode/tr.md)

Metin açıklamasına ve belirtilen boyutlara göre API üzerinden Flux Pro 1.1 Ultra kullanarak görüntü oluşturur. Bu düğüm, metin açıklamanıza ve belirttiğiniz boyutlara göre görüntü oluşturmak için harici bir servise bağlanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Görüntü oluşturma için prompt (varsayılan: boş string) |
| `istem_yükseltme` | BOOLEAN | Hayır | - | Prompt üzerinde yukarı örnekleme yapılıp yapılmayacağı. Aktif olduğunda, prompt'u daha yaratıcı oluşturum için otomatik olarak değiştirir, ancak sonuçlar belirsizdir (aynı seed tam olarak aynı sonucu üretmez). (varsayılan: False) |
| `tohum` | INT | Hayır | 0 ile 18446744073709551615 | Gürültü oluşturmak için kullanılan rastgele seed. (varsayılan: 0) |
| `en_boy_oranı` | STRING | Hayır | - | Görüntünün en-boy oranı; 1:4 ile 4:1 arasında olmalıdır. (varsayılan: "16:9") |
| `ham` | BOOLEAN | Hayır | - | True olduğunda, daha az işlenmiş, daha doğal görünümlü görüntüler oluşturur. (varsayılan: False) |
| `görüntü_istemi` | IMAGE | Hayır | - | Oluşturumu yönlendirmek için isteğe bağlı referans görüntü |
| `görüntü_istemi_gücü` | FLOAT | Hayır | 0.0 ile 1.0 | Prompt ile görüntü prompt'u arasındaki karışım oranı. (varsayılan: 0.1) |

**Not:** `aspect_ratio` parametresi 1:4 ile 4:1 arasında olmalıdır. `image_prompt` sağlandığında, `image_prompt_strength` aktif hale gelir ve referans görüntünün nihai çıktıyı ne kadar etkileyeceğini kontrol eder.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output_image` | IMAGE | Flux Pro 1.1 Ultra'dan oluşturulan görüntü |