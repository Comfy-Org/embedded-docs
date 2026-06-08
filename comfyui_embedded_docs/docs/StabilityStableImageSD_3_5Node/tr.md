Bu belge, Stability AI'nın Stable Diffusion 3.5 modelini kullanarak eşzamanlı olarak görseller üretir. Metin istemlerine dayalı görseller oluşturur ve girdi olarak sağlandığında mevcut görselleri de değiştirebilir. Düğüm, çıktıyı özelleştirmek için çeşitli en-boy oranlarını ve stil ön ayarlarını destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | Çıktı görselinde görmek istediğiniz şey. Öğeleri, renkleri ve konuları net bir şekilde tanımlayan güçlü, açıklayıcı bir istem daha iyi sonuçlara yol açacaktır. (varsayılan: boş dize) | STRING | Evet | - |
| `model` | Üretim için kullanılacak Stable Diffusion 3.5 modeli. | COMBO | Evet | `sd3.5-large`<br>`sd3.5-large-turbo`<br>`sd3.5-medium` |
| `en_boy_oranı` | Oluşturulan görselin en-boy oranı. (varsayılan: 1:1) | COMBO | Evet | `16:9`<br>`1:1`<br>`21:9`<br>`2:3`<br>`3:2`<br>`4:5`<br>`5:4`<br>`9:16`<br>`9:21` |
| `stil_önayarı` | Oluşturulan görsel için isteğe bağlı istenen stil. Stil ön ayarı kullanılmaması için "None" seçeneğini belirleyin. | COMBO | Hayır | `3d-model`<br>`analog-film`<br>`anime`<br>`cinematic`<br>`comic-book`<br>`digital-art`<br>`enhance`<br>`fantasy-art`<br>`isometric`<br>`line-art`<br>`low-poly`<br>`modeling-compound`<br>`neon-punk`<br>`origami`<br>`photographic`<br>`pixel-art`<br>`tile-texture`<br>`None` |
| `cfg_ölçeği` | Difüzyon sürecinin istem metnine ne kadar sıkı bağlı kalacağı (daha yüksek değerler görselinizi isteminize daha yakın tutar). (varsayılan: 4.0) | FLOAT | Evet | 1.0 ile 10.0 arası |
| `tohum` | Gürültüyü oluşturmak için kullanılan rastgele tohum. (varsayılan: 0) | INT | Evet | 0 ile 4294967294 arası |
| `görüntü` | Görselden görsele üretim için isteğe bağlı girdi görseli. Sağlandığında, düğüm görselden görsele moduna geçer ve `en_boy_oranı` parametresi yok sayılır. | IMAGE | Hayır | - |
| `negatif_istem` | Çıktı görselinde görmek istemediğiniz anahtar kelimeler. Bu gelişmiş bir özelliktir. (varsayılan: boş dize) | STRING | Hayır | - |
| `görüntü_gürültü_azaltma` | Girdi görselinin gürültü giderme oranı; 0.0, girdiyle aynı görseli verir, 1.0 ise hiç görsel sağlanmamış gibidir. (varsayılan: 0.5) Bu parametre yalnızca bir `görüntü` sağlandığında kullanılır. | FLOAT | Hayır | 0.0 ile 1.0 arası |

**Not:** Bir `image` sağlandığında, düğüm görselden görsele üretim moduna geçer ve `aspect_ratio` parametresi otomatik olarak girdi görselinden belirlenir. Hiçbir `image` sağlanmadığında, `image_denoise` parametresi yok sayılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Oluşturulan veya değiştirilen görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageSD_3_5Node/tr.md)

---
**Source fingerprint (SHA-256):** `80dbb27f19bb3286ee988f020f7f65623a73d7cac77ca0cdfc7a428254102aa3`
