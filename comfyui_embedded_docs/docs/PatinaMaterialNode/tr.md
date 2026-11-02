# Patina Material

Bir metin açıklamasından eksiksiz, kesintisiz döşenen bir PBR materyali oluşturur: bir temel doku ve isteğe bağlı SeedVR harita ölçeklendirmesiyle en fazla beş materyal haritası. Bir giriş görüntüsü, sonucu görüntüden görüntüye geçiş olarak yönlendirebilir; bir maskeyle birlikte verilen giriş görüntüsü ise bunu bir inpaint geçişine dönüştürür. Gerçek bir materyali taramadan oyuna hazır veya 3B'ye hazır yüzeyler üretmek için kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak materyalin veya dokunun açıklaması. | STRING | Evet | Çok satırlı metin |
| `image_size` | Çıktı doku boyutu. `"custom"`, `width` ve `height` girişlerini gösterir. Varsayılan: `"1:1 (1024x1024)"`. | DYNAMIC_COMBO | Evet | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | basecolor (albedo) haritasını oluşturur. Varsayılan: True. | BOOLEAN | Evet | true<br>false |
| `normal` | Normal haritasını oluşturur. Varsayılan: True. | BOOLEAN | Evet | true<br>false |
| `roughness` | Pürüzlülük haritasını oluşturur. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `metalness` | Metaliklik haritasını oluşturur. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `height` | Yükseklik (yer değiştirme) haritasını oluşturur. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `upscale_factor` | PBR haritalarının kesintisiz SeedVR ölçeklendirmesi. Temel doku ölçeklendirilmez ve 4x, 2048 piksellik bir haritayı 8K boyutuna dönüştürür. Varsayılan: 0 (kapalı). | INT | Evet | 0 ile 4 arası (adım: 2) |
| `seed` | Tekrarlanabilir üretim için tohum. Varsayılan: 42. | INT | Evet | 0 ile 2147483646 arası |
| `tiling_mode` | Döşeme yönü: çok yönlü, yatay veya dikey. Gelişmiş ayar. Varsayılan: `"both"`. | COMBO | Evet | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | Doku üretimi için gürültü giderme adımları. Gelişmiş ayar. Varsayılan: 8. | INT | Evet | 1 ile 8 arası |
| `tile_size` | Gizli uzaydaki döşeme boyutu; burada 64, 512 piksel ve 128, 1024 piksel anlamına gelir. Gelişmiş ayar. Varsayılan: 128. | INT | Evet | 32 ile 256 arası (adım: 2) |
| `tile_stride` | Gizli uzaydaki döşeme adımı. Gelişmiş ayar. Varsayılan: 64. | INT | Evet | 16 ile 128 arası (adım: 2) |
| `image` | İsteğe bağlı kaynak görüntü. Tek başına verildiğinde görüntüden görüntüye çalışır; bir maskeyle birlikte verildiğinde bir inpaint geçişi çalıştırır. | IMAGE | Hayır | - |
| `mask` | İsteğe bağlı inpaint maskesi; bir giriş görüntüsü gerektirir. Beyaz alanlar yeniden oluşturulur ve siyah alanlar korunur. | MASK | Hayır | - |
| `strength` | Giriş görüntüsünün ne kadar dönüştürüleceği. Yalnızca bir görüntü bağlandığında kullanılır. Gelişmiş ayar. Varsayılan: 0.6. | FLOAT | Evet | 0.01 ile 1.0 arası (adım: 0.01) |
| `prompt_expansion` | Daha zengin doku ayrıntısı için istemi bir dil modeliyle genişletir. Genişletme, istemi bir fotoğraf olarak yeniden çerçevelediğinden ve metalness haritasını soluklaştırma eğiliminde olduğundan varsayılan olarak kapalıdır. Gelişmiş ayar. | BOOLEAN | Evet | true<br>false |
| `safety_checker` | Sağlayıcının içerik güvenliği denetimini istek üzerinde çalıştırır. Gelişmiş ayar. Varsayılan: False. | BOOLEAN | Evet | true<br>false |

### Özel Görüntü Boyutu Girdileri

Bu girişler, `image_size` `"custom"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image_size.width` | Piksel cinsinden doku genişliği. Varsayılan: 1024. | INT | Evet | 512 ile 2048 arası (adım: 16) |
| `image_size.height` | Piksel cinsinden doku yüksekliği. Varsayılan: 1024. | INT | Evet | 512 ile 2048 arası (adım: 16) |

**Kısıtlar ve davranış:**

* Hiçbir materyal haritasının etkinleştirilmemesine izin verilir: düğüm bu durumda yalnızca temel dokuyu döndürür ve her harita çıktısı 1x1 yer tutucu olarak kalır.
* Bir maske, bir giriş görüntüsü gerektirir; tek başına bir maske hata verir.
* 8K bir sonuç, tek bir 8K üretimden değil, 2048 piksellik bir renderın haritalarının 4x ölçeklendirilmesinden gelir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `texture` | Materyalin, herhangi bir harita uygulanmamış temel dokusu. | IMAGE |
| `basecolor` | basecolor (albedo) haritası veya bu harita devre dışı bırakıldığında 1x1 yer tutucu. | IMAGE |
| `normal` | Normal haritası veya bu harita devre dışı bırakıldığında 1x1 yer tutucu. | IMAGE |
| `roughness` | Pürüzlülük haritası veya bu harita devre dışı bırakıldığında 1x1 yer tutucu. | IMAGE |
| `metalness` | Metaliklik haritası veya bu harita devre dışı bırakıldığında 1x1 yer tutucu. | IMAGE |
| `height` | Yükseklik (yer değiştirme) haritası veya bu harita devre dışı bırakıldığında 1x1 yer tutucu. | IMAGE |
| `expanded_prompt` | Sağlayıcının gerçekte kullandığı istem; yalnızca `prompt_expansion` etkinleştirildiğinde girişten farklıdır. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialNode/tr.md)

---
**Source fingerprint (SHA-256):** `4e8305fa56a29dce72c54de12ae05207e8de39a1fea1f4753906c26e8af60383`
