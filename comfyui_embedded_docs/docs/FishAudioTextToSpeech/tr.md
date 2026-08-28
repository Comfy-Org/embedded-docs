# FishAudioTextToSpeech

Bu düğüm, Fish Audio metin-konuşma modellerini kullanarak yazılı metni konuşma sesine dönüştürür. Metne gömülü duygu ipuçlarını (s2.1-pro'da [happy], [whispering]; s1'de (happy)) ve birden fazla ses bağlandığında @Voice1/@Voice2 etiketlerini kullanan çok konuşmacılı diyaloğu destekler. İki model mevcuttur: en fazla beş sesi ve çok konuşmacılı diyaloğu destekleyen s2.1-pro ile tek bir isteğe bağlı ses kullanan s1.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `metin` | Konuşmaya dönüştürülecek metin. İki veya daha fazla ses bağlandığında, konuşmacı değişikliklerini @Voice1, @Voice2 vb. ile işaretleyin. Boş olmamalıdır. (varsayılan: boş) | STRING | Evet | Boş olmayan herhangi bir metin |
| `model` | Metin-konuşma için kullanılacak model. | DYNAMIC_COMBO | Evet | "s2.1-pro"<br>"s1" |
| `seed` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ila 2147483647 |

### s2.1-pro Girdileri

Bu girdiler, s2.1-pro modeli seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `voices` | Genişletilebilir yuva: 1 ila 5 ses öğesi bağlayın (`voice_1`, `voice_2`, ...). Sentez için sesler. Varsayılan ses için boş bırakın. İki veya daha fazla ses varsa, metindeki konuşmacı değişikliklerini @Voice1, @Voice2 vb. ile işaretleyin. | FISHAUDIO_VOICE | Hayır | 0 ila 5 ses |
| `temperature` | İfade gücü. Daha yüksek değerler daha çeşitli, daha düşük değerler daha tutarlıdır. (varsayılan: 0.7) | FLOAT | Evet | 0.0 ila 1.0 |
| `top_p` | Nükleus örneklemesiyle çeşitlilik. (varsayılan: 0.7) | FLOAT | Evet | 0.01 ila 1.0 |
| `speed` | Konuşma hızı. 1.0 normal, <1.0 daha yavaş, >1.0 daha hızlıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.5 ila 2.0 |
| `volume` | Desibel cinsinden ses düzeyi ayarı. 0 değişiklik yok demektir. (varsayılan: 0.0) | FLOAT | Evet | -10.0 ila 10.0 |
| `normalize` | İngilizce ve Çince için sayıları ve metni normalleştirir, sayılar ve tarihler için kararlılığı artırır. (varsayılan: true) | BOOLEAN | Evet | true / false |

### s1 Girdileri

Bu girdiler, s1 modeli seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `voice` | Sentez için ses. Varsayılan ses için bağlantısız bırakın. | FISHAUDIO_VOICE | Hayır | İsteğe bağlı tek ses |
| `temperature` | İfade gücü. Daha yüksek değerler daha çeşitli, daha düşük değerler daha tutarlıdır. (varsayılan: 0.7) | FLOAT | Evet | 0.0 ila 1.0 |
| `top_p` | Nükleus örneklemesiyle çeşitlilik. (varsayılan: 0.7) | FLOAT | Evet | 0.01 ila 1.0 |
| `speed` | Konuşma hızı. 1.0 normal, <1.0 daha yavaş, >1.0 daha hızlıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.5 ila 2.0 |
| `volume` | Desibel cinsinden ses düzeyi ayarı. 0 değişiklik yok demektir. (varsayılan: 0.0) | FLOAT | Evet | -10.0 ila 10.0 |
| `normalize` | İngilizce ve Çince için sayıları ve metni normalleştirir, sayılar ve tarihler için kararlılığı artırır. (varsayılan: true) | BOOLEAN | Evet | true / false |

**Not:** `text` girdisi boş olmamalıdır. Konuşmacı etiketleri (@Voice1, @Voice2 vb.) büyük/küçük harfe duyarlı değildir ve bağlı bir sese işaret etmelidir; bağlı olmayan bir sese etiket eklemek hata verir. İki veya daha fazla ses bağlandığında, metin bağlı her sese en az bir kez atıfta bulunmalıdır; aksi takdirde düğüm eksik etiketleri rapor eder. s2.1-pro'da 0 ses bağlamak varsayılan sesi kullanır, 1 ses yalnızca o sesi kullanır ve 2 veya daha fazla ses çok konuşmacılı diyaloğu etkinleştirir. s1'de tek bir isteğe bağlı ses kullanılır ve bağlantısız bırakmak varsayılan sesi kullanır. Metne duygu ipuçları yerleştirilebilir: s2.1-pro'da [happy] ve [whispering], s1'de (happy).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Ses dosyası olarak oluşturulan konuşma. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioTextToSpeech/tr.md)

---
**Source fingerprint (SHA-256):** `6cc005ae76fc7b60d9399b1b0a3c5de40a6eff47cd6f0f0b73b4212c0270ae29`
