# HeyGen Video 1.0 Görüntüden Videoya

HeyGen Video 1.0 kullanarak bir görüntüyü eşzamanlı diyalog ve ses içeren videoya dönüştürün. Bağlanan görüntü ilk kare olarak kullanılır ve oluşturulan video en-boy oranını korur. İstemde, söylenen replikler dahil olmak üzere ne olması gerektiğini açıklayın. Düğüm görüntüyü yükler, video işi oluşturur, bitmesini bekler ve ortaya çıkan videoyu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Oluşturma için kullanılan model sürümü. (varsayılan: `"heygen-video-1"`) | DYNAMIC_COMBO | Evet | `"heygen-video-1"` |
| `image` | Videonun ilk karesi. Tam olarak bir görüntü gereklidir; toplu iş reddedilir. Çıktı bu görüntünün en-boy oranını koruduğu için videonun şeklini değiştirmek üzere görüntüyü kırpın. | IMAGE | Evet | 1 görsel, en-boy oranı 1:4 ile 4:1 arası |
| `prompt` | Videoda ne olduğunun açıklaması, diyalog dahil. (varsayılan: boş dize) | STRING | Evet | 1 ile 16000 karakter arası |
| `duration` | Çıktı videosunun saniye cinsinden süresi. `auto_duration` `"enabled"` olduğunda yok sayılır. (varsayılan: 5) | INT | Evet | 5 ile 30 arası |
| `resolution` | Çıktı çözünürlüğü. 1080p ve 2k yalnızca 16:9 veya 9:16 oranında işlenir; bu nedenle görüntünün bu biçimde olması gerekir; önce görüntüyü kırpın. (varsayılan: `"768p"`) | COMBO | Evet | `"768p"`<br>`"480p"`<br>`"1080p"`<br>`"2k"` |
| `seed` | Oluşturma için tohum. Aynı tohumla çalıştırmalar arasında sonuçlar yine de değişebilir. (varsayılan: 42) | INT | Evet | 0 ile 4294967295 arası |
| `auto_duration` | Etkinleştirildiğinde, video uzunluğu istemdeki tırnak içine alınmış diyaloğu izler (8 ile 30 saniye arası) ve `duration` yok sayılır. (varsayılan: `"disabled"`) | COMBO | Hayır | `"disabled"`<br>`"enabled"` |

### Parametre Kısıtlamaları

- **Tek görüntü:** `image` tam olarak bir görüntü içermelidir. Bir toplu grup bağlamak hata verir.
- **Görüntü en-boy oranı:** görüntü, yüksekliğinin 4 katından daha geniş ve genişliğinin 4 katından daha yüksek olmamalıdır (1:4 ile 4:1 arası); aksi halde çalıştırma başarısız olur.
- **İstem gerekli:** istem en az bir boşluk olmayan karakter ve en fazla 16000 karakter içermelidir.
- **Yüksek çözünürlükler:** `resolution` `"1080p"` ve `"2k"`, 16:9 veya 9:16 bir görüntü gerektirir; çünkü video görüntünün en-boy oranını korur. Diğer biçimler için görüntüyü kırpın.
- **Tohum:** tohum yalnızca düğümün yeniden çalışıp çalışmayacağına karar verir; sonuçlar aynı tohumla yeniden üretilemez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Giriş görüntüsünün en-boy oranında, eşzamanlı diyalog ve ses içeren oluşturulmuş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `e711d1d84c6c73a2ee177903f982042086a57b3e1afff8390c6e5b3bcd09c914`
