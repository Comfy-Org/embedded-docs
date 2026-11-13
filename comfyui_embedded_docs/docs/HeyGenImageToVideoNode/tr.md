# HeyGen Video 1.0 Görüntüden Videoya

Bir görseli HeyGen Video 1.0 kullanarak senkronize diyalog ve sesle videoya dönüştürün. Bağlanan görsel ilk kare olarak kullanılır ve oluşturulan video en-boy oranını korur. İstemde, söylenecek replikler dahil, ne olması gerektiğini açıklayın. Düğüm görseli yükler, video işini oluşturur, tamamlanmasını bekler ve ortaya çıkan videoyu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Üretim için kullanılan model sürümü. (varsayılan: `"heygen-video-1"`) | DYNAMIC_COMBO | Evet | `"heygen-video-1"` |
| `image` | Videonun ilk karesi. Tam olarak bir görsel gerekir; bir toplu iş reddedilir. Çıktı bu görselin en-boy oranını koruduğu için videonun şeklini değiştirmek üzere görseli kırpın. | IMAGE | Evet | 1 görsel, en-boy oranı 1:4 ile 4:1 arası |
| `prompt` | Videoda ne olduğunun, herhangi bir diyalog dahil, açıklaması. (varsayılan: boş dize) | STRING | Evet | 1 ile 16000 karakter arası |
| `duration` | Çıktı videosunun saniye cinsinden süresi. `auto_duration` `"enabled"` olduğunda yok sayılır. (varsayılan: 5) | INT | Evet | 5 ile 30 arası |
| `resolution` | Çıktı çözünürlüğü. (varsayılan: `"768p"`) | COMBO | Evet | `"768p"`<br>`"480p"`<br>`"1080p"`<br>`"2k"` |
| `seed` | Üretim için tohum. Aynı tohumla çalıştırmalar arasında sonuçlar yine de değişebilir. (varsayılan: 42) | INT | Evet | 0 ile 4294967295 arası |
| `auto_duration` | Etkinleştirildiğinde, video uzunluğu istemdeki alıntılanan diyaloğu izler (8 ile 30 saniye arası) ve `duration` yok sayılır. (varsayılan: `"disabled"`) | COMBO | Hayır | `"disabled"`<br>`"enabled"` |

### Parametre Kısıtlamaları

- **Tek görsel:** `image` tam olarak bir görsel içermelidir. Bir toplu iş bağlamak hata verir.
- **Görsel en-boy oranı:** görsel, yüksekliğinin 4 katından daha geniş ve genişliğinin 4 katından daha yüksek olmamalıdır (1:4 ile 4:1 arası); aksi takdirde çalıştırma başarısız olur.
- **İstem gerekli:** istem en az bir boşluk olmayan karakter ve en fazla 16000 karakter içermelidir.
- **Tohum:** tohum yalnızca düğümün yeniden çalışıp çalışmayacağına karar verir; sonuçlar aynı tohumla yeniden üretilemez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Girdi görselinin en-boy oranında, senkronize diyalog ve ses içeren oluşturulmuş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `e711d1d84c6c73a2ee177903f982042086a57b3e1afff8390c6e5b3bcd09c914`
