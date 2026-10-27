# Patina Material Extract

Bir girdi görüntüsünün bir bölgesinden, neyin alınacağını belirten bir komut istemiyle yönlendirilerek, sorunsuz döşenen bir PBR malzemesi çıkarır: bir duvar, bir zemin, bir kumaş. Çıkarılan temel dokuyu ve isteğe bağlı SeedVR ile haritaların ölçeklendirilmesiyle birlikte en fazla beş malzeme haritası döndürür. Gerçek bir yüzeyin fotoğrafını yeniden kullanılabilir, döşenebilir bir malzemeye dönüştürmek için kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Doku çıkarılacak görüntü. | IMAGE | Evet | - |
| `prompt` | Görüntüden hangi dokunun çıkarılacağının açıklaması, örneğin `"the wall"`. | STRING | Evet | Çok satırlı metin |
| `image_size` | Çıktı doku boyutu. `"custom"` seçeneği `width` ve `height` girdilerini gösterir. Varsayılan: `"1:1 (1024x1024)"`. | DYNAMIC_COMBO | Evet | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | Basecolor (albedo) haritasını oluştur. Varsayılan: True. | BOOLEAN | Evet | true<br>false |
| `normal` | Normal haritasını oluştur. Varsayılan: True. | BOOLEAN | Evet | true<br>false |
| `roughness` | Pürüzlülük haritasını oluştur. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `metalness` | Metaliklik haritasını oluştur. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `height` | Yükseklik (yer değiştirme) haritasını oluştur. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `upscale_factor` | PBR haritalarının sorunsuz SeedVR ölçeklendirmesi. Temel doku ölçeklendirilmez ve 4x, 2048 piksellik bir haritayı 8K'ya dönüştürür. Varsayılan: 0 (kapalı). | INT | Evet | 0 - 4 (adım 2) |
| `seed` | Yeniden üretilebilir oluşturma için tohum. Varsayılan: 42. | INT | Evet | 0 - 2147483646 |
| `strength` | Girdi görüntüsünün ne kadar dönüştürüleceği. Gelişmiş ayar. Varsayılan: 0.6. | FLOAT | Evet | 0.01 - 1.0 (adım 0.01) |
| `tiling_mode` | Döşeme yönü: çok yönlü, yatay veya dikey. Gelişmiş ayar. Varsayılan: `"both"`. | COMBO | Evet | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | Doku oluşturma için gürültü giderme adımları. Gelişmiş ayar. Varsayılan: 8. | INT | Evet | 1 - 8 |
| `tile_size` | Gizli uzayda döşeme boyutu; burada 64, 512 piksel ve 128, 1024 piksel anlamına gelir. Gelişmiş ayar. Varsayılan: 128. | INT | Evet | 32 - 256 (adım 2) |
| `tile_stride` | Gizli uzayda döşeme adımı. Gelişmiş ayar. Varsayılan: 64. | INT | Evet | 16 - 128 (adım 2) |
| `prompt_expansion` | Daha zengin doku ayrıntısı için komut istemini bir dil modeliyle genişletin. Varsayılan olarak kapalıdır, çünkü genişletme komut istemini bir fotoğraf olarak yeniden çerçeveler ve metaliklik haritasını soluklaştırma eğilimindedir. Gelişmiş ayar. | BOOLEAN | Evet | true<br>false |
| `safety_checker` | İstek üzerinde sağlayıcının içerik güvenliği kontrolünü çalıştır. Gelişmiş ayar. Varsayılan: False. | BOOLEAN | Evet | true<br>false |

### Özel Görüntü Boyutu Girdileri

Bu girdiler `image_size` `"custom"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image_size.width` | Doku genişliği piksel cinsinden. Varsayılan: 1024. | INT | Evet | 512 - 2048 (adım 16) |
| `image_size.height` | Doku yüksekliği piksel cinsinden. Varsayılan: 1024. | INT | Evet | 512 - 2048 (adım 16) |

**Kısıtlamalar ve davranış:**

* En az bir malzeme haritası etkinleştirilmelidir, aksi takdirde çalıştırma başarısız olur.
* Komut istemi gereklidir ve boş olmamalıdır; çıkarılacak bölgeyi olabildiğince hassas bir şekilde adlandırın.
* 8K sonuç, tek bir 8K oluşturmadan değil, 2048 piksellik bir render'ın haritalarının 4x ölçeklendirilmesinden gelir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `texture` | Herhangi bir harita uygulanmadan çıkarılan temel doku. | IMAGE |
| `basecolor` | Basecolor (albedo) haritası veya bu harita devre dışı bırakıldığında 1x1 yer tutucu. | IMAGE |
| `normal` | Normal haritası veya bu harita devre dışı bırakıldığında 1x1 yer tutucu. | IMAGE |
| `roughness` | Pürüzlülük haritası veya bu harita devre dışı bırakıldığında 1x1 yer tutucu. | IMAGE |
| `metalness` | Metaliklik haritası veya bu harita devre dışı bırakıldığında 1x1 yer tutucu. | IMAGE |
| `height` | Yükseklik (yer değiştirme) haritası veya bu harita devre dışı bırakıldığında 1x1 yer tutucu. | IMAGE |
| `expanded_prompt` | Sağlayıcının gerçekte kullandığı komut istemi; yalnızca `prompt_expansion` etkinleştirildiğinde girdiden farklıdır. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialExtractNode/tr.md)

---
**Source fingerprint (SHA-256):** `484b8eaa57388541e352cd88c8998c63aa0b2a99d98cd8e602252625064f16ba`
