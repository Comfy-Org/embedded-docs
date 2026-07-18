# SyncTalkingImageNode

Bir portre fotoğrafını, sync.so'nun sync-3 modelini kullanarak konuşma sesiyle yönlendirilen bir konuşan videoya dönüştürün. Çıktı süresi, ses süresiyle eşleşir ve maliyet, çıktı süresine göre ölçeklenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Yüzü net bir şekilde görünen, 4K'ya (4096x2160) kadar tek bir görsel. | IMAGE | Evet | Tam olarak bir görsel gerekli |
| `audio` | Konuşan videoyu yönlendiren konuşma sesi; çıktı süresi bununla eşleşir. Animasyonu metinden yönlendirmek için herhangi bir TTS düğümünü buraya zincirleyin. | AUDIO | Evet | Maksimum süre: 600 saniye |
| `prompt` | Portrenin nasıl canlanacağına dair isteğe bağlı yönlendirme, örn. 'kişinin gülümsemesini ve kameraya bakmasını sağla'. Doğal konuşma hareketi için boş bırakın. (varsayılan: "") | STRING | Hayır | Çok satırlı metin |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 arası |
| `model` | sync.so üretim modeli. Görsel girişi yalnızca sync-3'e özeldir. | COMBO | Evet | `"sync-3"` |
| `speaker_selection` | Birden fazla kişi görünür olduğunda hangi yüzün canlandırılacağı. `default`: modelin karar vermesine izin verir. `coordinates`: görseldeki piksel (speaker_x, speaker_y) konumundaki yüzü hedefler. Görseller için otomatik algılama desteklenmez. (varsayılan: "default") | COMBO | Hayır | `"default"`<br>`"coordinates"` |
| `speaker_x` | Konuşmacının yüzünün X piksel koordinatı. Yalnızca speaker_selection 'coordinates' olduğunda kullanılır. (varsayılan: 0) | INT | Hayır | 0 ile 4096 arası |
| `speaker_y` | Konuşmacının yüzünün Y piksel koordinatı. Yalnızca speaker_selection 'coordinates' olduğunda kullanılır. (varsayılan: 0) | INT | Hayır | 0 ile 4096 arası |
| `auto_downscale` | Görsel 4K (4096x2160) giriş sınırını aşarsa otomatik olarak küçültür; konuşmacı koordinatları buna göre ölçeklenir. Devre dışı bırakıldığında, aşırı büyük bir görsel bunun yerine bir hataya neden olur. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |

**Not:** `speaker_x` ve `speaker_y` parametreleri yalnızca `speaker_selection` `"coordinates"` olarak ayarlandığında kullanılır. `auto_downscale` etkinleştirildiğinde, konuşmacı koordinatları, küçültülmüş görsel boyutlarına uyacak şekilde otomatik olarak ölçeklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Canlandırılmış portrenin giriş sesiyle senkronize olduğu, oluşturulan konuşan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SyncTalkingImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `21f722cdcc5ff017949887ed2252854feebb9b913034dc6a6c3ce196ad089468`
