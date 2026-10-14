# Fish Audio Metinden Konuşmaya

Bu düğüm, Fish Audio metinden konuşmaya modellerini kullanarak yazılı metni konuşma sesine dönüştürür. Metne gömülü ipuçlarını destekler: s2.1-pro'da [happy] ve [whispering], s1'de (happy) ve drama-3'te düz dille [directions] ile `<whisper>...</whisper>` sözcük etiketleri. Çoklu konuşmacı diyaloğu, birden fazla ses bağlandığında @Voice1/@Voice2 etiketlerini kullanır. Üç model mevcuttur: her ikisi de en fazla beş sesi ve çoklu konuşmacı diyaloğunu destekleyen drama-3 ve s2.1-pro ile tek isteğe bağlı ses kullanan s1.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `metin` | Konuşmaya dönüştürülecek metin. İki veya daha fazla ses bağlıyken konuşmacı değişimlerini @Voice1, @Voice2 vb. ile işaretleyin. (varsayılan: boş) | STRING | Evet | Boş olmayan herhangi bir metin |
| `model` | Metinden konuşmaya dönüşümünde kullanılacak model. | DYNAMIC_COMBO | Evet | "drama-3"<br>"s2.1-pro"<br>"s1" |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 - 2147483647 |

### drama-3 ve s2.1-pro Girdileri

Bu girdiler, `drama-3` veya `s2.1-pro` modeli seçildiğinde görünür. Parametre kümeleri aynıdır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `voices` | Genişletilebilir yuva: 0 ile 5 arasında ses öğesi bağlayın (`voice_1`, `voice_2`, ...). Sentez için sesler. Rastgele bir ses için boş bırakın. İki veya daha fazla sesle, metindeki konuşmacı değişimlerini @Voice1, @Voice2 vb. ile işaretleyin. | FISHAUDIO_VOICE | Hayır | 0 - 5 ses |
| `temperature` | İfade gücü. Yüksek değerler daha çeşitli, düşük değerler daha tutarlıdır. (varsayılan: 0.7) | FLOAT | Evet | 0.0 - 1.0 |
| `top_p` | Nucleus örneklemesi yoluyla çeşitlilik. (varsayılan: 0.7) | FLOAT | Evet | 0.01 - 1.0 |
| `speed` | Konuşma hızı. 1.0 normal, <1.0 daha yavaş, >1.0 daha hızlıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.5 - 2.0 |
| `volume` | Desibel cinsinden ses düzeyi ayarı. 0 değişiklik yok demektir. (varsayılan: 0.0) | FLOAT | Evet | -10.0 - 10.0 |
| `normalize` | İngilizce ve Çince için sayıları ve metni normalleştirir; sayılar ve tarihler için kararlılığı artırır. (varsayılan: true) | BOOLEAN | Evet | true / false |

### s1 Girdileri

Bu girdiler, s1 modeli seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `voice` | Sentez için ses. Rastgele bir ses için bağlamadan bırakın. | FISHAUDIO_VOICE | Hayır | İsteğe bağlı tek ses |
| `temperature` | İfade gücü. Yüksek değerler daha çeşitli, düşük değerler daha tutarlıdır. (varsayılan: 0.7) | FLOAT | Evet | 0.0 - 1.0 |
| `top_p` | Nucleus örneklemesi yoluyla çeşitlilik. (varsayılan: 0.7) | FLOAT | Evet | 0.01 - 1.0 |
| `speed` | Konuşma hızı. 1.0 normal, <1.0 daha yavaş, >1.0 daha hızlıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.5 - 2.0 |
| `volume` | Desibel cinsinden ses düzeyi ayarı. 0 değişiklik yok demektir. (varsayılan: 0.0) | FLOAT | Evet | -10.0 - 10.0 |
| `normalize` | İngilizce ve Çince için sayıları ve metni normalleştirir; sayılar ve tarihler için kararlılığı artırır. (varsayılan: true) | BOOLEAN | Evet | true / false |

**Not:** `text` girdisi boş olmamalıdır. Konuşmacı etiketleri (@Voice1, @Voice2 vb.) büyük/küçük harfe duyarsızdır ve bağlı bir sesi belirtmelidir; bağlı olmayan bir sesi etiketlemek hata verir. İki veya daha fazla ses bağlıysa metin, bağlı her sesi en az bir kez belirtmelidir; aksi halde düğüm eksik etiketleri bildirir. drama-3 ve s2.1-pro'da 0 ses bağlamak rastgele bir ses kullanır, 1 ses yalnızca o sesi kullanır ve 2 veya daha fazla ses çoklu konuşmacı diyaloğunu etkinleştirir. s1'de isteğe bağlı tek ses kullanılır ve bağlı bırakılmazsa rastgele bir ses kullanılır. İpuçları metne yerleştirilebilir: s2.1-pro'da [happy] ve [whispering], s1'de (happy) ve drama-3'te düz dille [directions] ile `<whisper>...</whisper>` sözcük etiketleri.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Oluşturulan konuşma, bir ses dosyası olarak. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioTextToSpeech/tr.md)

---
**Source fingerprint (SHA-256):** `adcfe8f994b8fbe07efb3dd3f86c8955ea3cec62cc3f0321efd2b63c0470b7a3`
