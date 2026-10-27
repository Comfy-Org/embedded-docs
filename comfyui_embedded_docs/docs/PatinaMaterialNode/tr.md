# Patina Material

Bir metin açıklamasından eksiksiz, dikişsiz döşemeli bir PBR malzemesi üretir: bir temel doku ile en fazla beş malzeme haritası ve haritaların isteğe bağlı SeedVR ile büyütülmesi. Bir giriş görüntüsü, sonucu görüntüden görüntüye geçişi olarak yönlendirebilir; bir maskeyle birlikte verilen giriş görüntüsü ise bunu içe boyama (inpaint) geçişine dönüştürür. Gerçek bir malzemeyi taramadan oyuna veya 3D'ye hazır yüzeyler üretmek için kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak malzemenin veya dokunun açıklaması. | STRING | Evet | Çok satırlı metin |
| `image_size` | Çıktı doku boyutu. `"custom"`, `width` ve `height` girdilerini gösterir. Varsayılan: `"1:1 (1024x1024)"`. | DYNAMIC_COMBO | Evet | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | Temel renk (albedo) haritasını oluşturur. Varsayılan: True. | BOOLEAN | Evet | true<br>false |
| `normal` | Normal haritasını oluşturur. Varsayılan: True. | BOOLEAN | Evet | true<br>false |
| `roughness` | Pürüzlülük haritasını oluşturur. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `metalness` | Metaliklik haritasını oluşturur. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `height` | Yükseklik (deplasman) haritasını oluşturur. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `upscale_factor` | PBR haritalarının dikişsiz SeedVR ile büyütülmesi. Temel doku büyütülmez ve 4x, 2048 piksellik bir haritayı 8K'ya dönüştürür. Varsayılan: 0 (kapalı). | INT | Evet | 0 - 4 (adım 2) |
| `seed` | Tekrarlanabilir üretim için tohum. Varsayılan: 42. | INT | Evet | 0 - 2147483646 |
| `tiling_mode` | Döşeme yönü: çok yönlü, yatay veya dikey. Gelişmiş ayar. Varsayılan: `"both"`. | COMBO | Evet | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | Doku oluşturma için gürültü giderme adımları. Gelişmiş ayar. Varsayılan: 8. | INT | Evet | 1 - 8 |
| `tile_size` | Latent uzayda karo boyutu; burada 64, 512 piksel ve 128, 1024 piksel anlamına gelir. Gelişmiş ayar. Varsayılan: 128. | INT | Evet | 32 - 256 (adım 2) |
| `tile_stride` | Latent uzayda karo adımı. Gelişmiş ayar. Varsayılan: 64. | INT | Evet | 16 - 128 (adım 2) |
| `image` | İsteğe bağlı kaynak görüntü. Tek başına olduğunda görüntüden görüntüye çalışır; bir maskeyle birlikte içe boyama geçişi çalıştırır. | IMAGE | Hayır | - |
| `mask` | İsteğe bağlı içe boyama maskesi; bir giriş görüntüsü gerektirir. Beyaz alanlar yeniden oluşturulur, siyah alanlar korunur. | MASK | Hayır | - |
| `strength` | Giriş görüntüsünün ne kadar dönüştürüleceği. Yalnızca bir görüntü bağlandığında kullanılır. Gelişmiş ayar. Varsayılan: 0.6. | FLOAT | Evet | 0.01 - 1.0 (adım 0.01) |
| `prompt_expansion` | Daha zengin doku ayrıntısı için istemi bir dil modeliyle genişletir. Varsayılan olarak kapalıdır; çünkü genişletme istemi bir fotoğraf olarak yeniden çerçeveler ve metaliklik haritasını soluklaştırma eğilimindedir. Gelişmiş ayar. | BOOLEAN | Evet | true<br>false |
| `safety_checker` | Sağlayıcının içerik güvenliği denetimini istek üzerinde çalıştırır. Gelişmiş ayar. Varsayılan: False. | BOOLEAN | Evet | true<br>false |

### Özel Görüntü Boyutu Girdileri

Bu girdiler, `image_size` `"custom"` değerine ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image_size.width` | Piksel cinsinden doku genişliği. Varsayılan: 1024. | INT | Evet | 512 - 2048 (adım 16) |
| `image_size.height` | Piksel cinsinden doku yüksekliği. Varsayılan: 1024. | INT | Evet | 512 - 2048 (adım 16) |

**Kısıtlamalar ve davranış:**

* En az bir malzeme haritası etkinleştirilmelidir, aksi halde çalıştırma başarısız olur.
* Bir maske giriş görüntüsü gerektirir; tek başına bir maske hata verir.
* 8K sonuç, tek bir 8K üretimden değil, 2048 piksellik bir render'ın haritalarının 4x büyütülmesinden gelir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `texture` | Malzemenin temel dokusu, herhangi bir harita uygulanmadan. | IMAGE |
| `basecolor` | Temel renk (albedo) haritası veya bu harita devre dışıyken 1x1 yer tutucu. | IMAGE |
| `normal` | Normal haritası veya bu harita devre dışıyken 1x1 yer tutucu. | IMAGE |
| `roughness` | Pürüzlülük haritası veya bu harita devre dışıyken 1x1 yer tutucu. | IMAGE |
| `metalness` | Metaliklik haritası veya bu harita devre dışıyken 1x1 yer tutucu. | IMAGE |
| `height` | Yükseklik (deplasman) haritası veya bu harita devre dışıyken 1x1 yer tutucu. | IMAGE |
| `expanded_prompt` | Sağlayıcının gerçekte kullandığı istem; yalnızca `prompt_expansion` etkinleştirildiğinde girişten farklıdır. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialNode/tr.md)

---
**Source fingerprint (SHA-256):** `4e8305fa56a29dce72c54de12ae05207e8de39a1fea1f4753906c26e8af60383`
