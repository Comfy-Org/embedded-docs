> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageNode/tr.md)

ByteDance Görsel düğümü, metin istemlerine dayalı olarak bir API aracılığıyla ByteDance modellerini kullanarak görseller oluşturur. Bir model seçmenize, görsel boyutlarını belirlemenize ve tohum (seed) ile yönlendirme ölçeği (guidance scale) gibi çeşitli oluşturma parametrelerini kontrol etmenize olanak tanır. Düğüm, ByteDance'in görsel oluşturma hizmetine bağlanır ve oluşturulan görseli döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | STRING | Evet | `"seedream-3-0-t2i-250415"` | Görsel oluşturma için kullanılacak ByteDance modeli. Şu anda yalnızca bir model seçeneği mevcuttur. |
| `prompt` | STRING | Evet | - | Görseli oluşturmak için kullanılan metin istemi. Boşluklar temizlendikten sonra en az 1 karakter uzunluğunda olmalıdır. |
| `size_preset` | STRING | Evet | Açıklamaya bakın | Önerilen bir boyutu seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Özel (Custom) seçeneğini belirleyin. Mevcut ön ayarlar `RECOMMENDED_PRESETS` listesi tarafından tanımlanır. |
| `width` | INT | Evet | 512 ila 2048 (64'er adım) | Görsel için özel genişlik. Bu değer yalnızca `size_preset` "Özel" (Custom) olarak ayarlandığında kullanılır. Varsayılan: 1024. |
| `height` | INT | Evet | 512 ila 2048 (64'er adım) | Görsel için özel yükseklik. Bu değer yalnızca `size_preset` "Özel" (Custom) olarak ayarlandığında kullanılır. Varsayılan: 1024. |
| `seed` | INT | Hayır | 0 ila 2147483647 (1'er adım) | Oluşturma için kullanılacak tohum (seed) değeri. Varsayılan: 0. |
| `guidance_scale` | FLOAT | Hayır | 1.0 ila 10.0 (0.01'er adım) | Daha yüksek değer, görselin istemi daha yakından takip etmesini sağlar. Varsayılan: 2.5. |
| `watermark` | BOOLEAN | Hayır | Doğru / Yanlış | Görsele "AI tarafından oluşturuldu" filigranı eklenip eklenmeyeceği. Varsayılan: Yanlış. Bu bir gelişmiş parametredir. |

**Boyut parametreleri hakkında not:** `width` ve `height` parametreleri yalnızca `size_preset` "Özel" (Custom) olarak ayarlandığında kullanılır. Bir ön ayar boyutu seçilirse, ön ayarın boyutları özel genişlik ve yükseklik değerlerini geçersiz kılar. Özel boyutlar kullanıldığında hem genişlik hem de yükseklik 512 ile 2048 piksel arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | ByteDance API'sinden bir tensör olarak döndürülen oluşturulmuş görsel. |

---
**Source fingerprint (SHA-256):** `6ad3011ae942e81bc5e5296fa7120ee89637ef7487e2f12822d84b6917ec211e`
