# HeyGen Video 1.0 Image to Video

HeyGen Video 1.0 kullanarak bir görseli senkronize diyalog ve sesle videoya canlandırın. Bağlanan görsel ilk kare olarak kullanılır ve oluşturulan video en-boy oranını korur. İstemde, söylenen replikler dahil olmak üzere ne olması gerektiğini açıklayın. Düğüm görseli yükler, video işini oluşturur, tamamlanmasını bekler ve sonuç videosunu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Oluşturma için kullanılan model sürümü. (varsayılan: `"heygen-video-1"`) | DYNAMIC_COMBO | Evet | `"heygen-video-1"` |
| `image` | Videonun ilk karesi. Tam olarak bir görsel gereklidir; bir toplu grup reddedilir. Çıktı bu görselin en-boy oranını koruduğu için videonun şeklini değiştirmek üzere görseli kırpın. | IMAGE | Evet | 1 görsel, en-boy oranı 1:4 - 4:1 |
| `prompt` | Videoda ne olduğunun açıklaması, herhangi bir diyalog dahil. (varsayılan: boş dize) | STRING | Evet | 1 - 32000 karakter |
| `duration` | Çıktı videosunun saniye cinsinden süresi. (varsayılan: 5) | INT | Evet | 5 - 15 |
| `resolution` | Çıktı çözünürlüğü. (varsayılan: `"768p"`) | COMBO | Evet | `"768p"`<br>`"480p"`<br>`"2k"` |
| `seed` | Oluşturma için seed. Sonuçlar aynı seed ile çalıştırmalar arasında yine de değişebilir. (varsayılan: 42) | INT | Evet | 0 - 4294967295 |

### Parametre Kısıtlamaları

- **Tek görsel:** `image` tam olarak bir görsel içermelidir. Bir toplu grup bağlamak hata verir.
- **Görsel en-boy oranı:** görsel, yüksekliğinin 4 katından daha geniş olamaz ve genişliğinin 4 katından daha yüksek olamaz (1:4 ile 4:1 arasında); aksi halde çalıştırma başarısız olur.
- **İstem gerekli:** istem en az bir boşluk olmayan karakter ve en fazla 32000 karakter içermelidir.
- **Seed:** seed yalnızca düğümün yeniden çalıştırılıp çalıştırılmayacağını belirler; sonuçlar aynı seed ile yeniden üretilemez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Girdi görselinin en-boy oranında, senkronize diyalog ve ses içeren oluşturulmuş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `e15def8ce378572247be7dd197ac469fb655bcecf76521c8e9495bbad34e0284`
