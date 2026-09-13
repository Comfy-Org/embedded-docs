# Fish Audio Metinden Konuşmaya

Bu düğüm, Fish Audio metinden konuşmaya modellerini kullanarak yazılı metni konuşulan sese dönüştürür. Metne gömülü duygu ipuçlarını ([happy], [whispering] s2.1-pro'da; (happy) s1'de) ve birden çok ses bağlandığında @Voice1/@Voice2 etiketleriyle çok konuşmacılı diyaloğu destekler. İki model kullanılabilir: beşe kadar sesi ve çok konuşmacılı diyaloğu destekleyen s2.1-pro ve isteğe bağlı tek ses kullanan s1.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `metin` | Sese dönüştürülecek metin. İki veya daha fazla ses bağlandığında, konuşmacı değişikliklerini @Voice1, @Voice2, vb. ile işaretleyin. (varsayılan: boş) | STRING | Evet | Herhangi bir boş olmayan metin |
| `model` | Metinden konuşmaya dönüştürme için kullanılacak model. | DYNAMIC_COMBO | Evet | "s2.1-pro"<br>"s1" |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 - 2147483647 |

### s2.1-pro Girdileri

Bu girdiler s2.1-pro modeli seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `voices` | Büyütülebilir yuva: 0 ile 5 arasında ses öğesi bağlayın (`voice_1`, `voice_2`, ...). Sentez için sesler. Varsayılan ses için boş bırakın. İki veya daha fazla sesle, metindeki konuşmacı değişikliklerini @Voice1, @Voice2, vb. ile işaretleyin. | FISHAUDIO_VOICE | Hayır | 0 - 5 ses |
| `temperature` | İfade gücü. Yüksek değerler daha çeşitli, düşük değerler daha tutarlıdır. (varsayılan: 0.7) | FLOAT | Evet | 0.0 - 1.0 |
| `top_p` | Çekirdek örnekleme yoluyla çeşitlilik. (varsayılan: 0.7) | FLOAT | Evet | 0.01 - 1.0 |
| `speed` | Konuşma hızı. 1.0 normal, <1.0 daha yavaş, >1.0 daha hızlıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.5 - 2.0 |
| `volume` | Desibel cinsinden ses düzeyi ayarı. 0 değişiklik yok demektir. (varsayılan: 0.0) | FLOAT | Evet | -10.0 - 10.0 |
| `normalize` | İngilizce ve Çince için sayıları ve metni normalleştirir; sayılar ve tarihler için kararlılığı artırır. (varsayılan: true) | BOOLEAN | Evet | true / false |

### s1 Girdileri

Bu girdiler s1 modeli seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `voice` | Sentez için ses. Varsayılan ses için bağlantısız bırakın. | FISHAUDIO_VOICE | Hayır | İsteğe bağlı tek ses |
| `temperature` | İfade gücü. Yüksek değerler daha çeşitli, düşük değerler daha tutarlıdır. (varsayılan: 0.7) | FLOAT | Evet | 0.0 - 1.0 |
| `top_p` | Çekirdek örnekleme yoluyla çeşitlilik. (varsayılan: 0.7) | FLOAT | Evet | 0.01 - 1.0 |
| `speed` | Konuşma hızı. 1.0 normal, <1.0 daha yavaş, >1.0 daha hızlıdır. (varsayılan: 1.0) | FLOAT | Evet | 0.5 - 2.0 |
| `volume` | Desibel cinsinden ses düzeyi ayarı. 0 değişiklik yok demektir. (varsayılan: 0.0) | FLOAT | Evet | -10.0 - 10.0 |
| `normalize` | İngilizce ve Çince için sayıları ve metni normalleştirir; sayılar ve tarihler için kararlılığı artırır. (varsayılan: true) | BOOLEAN | Evet | true / false |

**Not:** `text` girdisi boş olmamalıdır. Konuşmacı etiketleri (@Voice1, @Voice2, vb.) büyük/küçük harfe duyarsızdır ve bağlı bir sesi göstermelidir; bağlı olmayan bir sesi etiketlemek hataya yol açar. İki veya daha fazla ses bağlandığında, metin bağlı her sese en az bir kez başvurmalıdır; aksi halde düğüm eksik etiketleri bildirir. s2.1-pro'da 0 ses bağlamak varsayılan sesi kullanır, 1 ses yalnızca o sesi kullanır ve 2 veya daha fazla ses çok konuşmacılı diyaloğu etkinleştirir. s1'de isteğe bağlı tek ses kullanılır ve bağlantısız bırakmak varsayılan sesi kullanır. Metne duygu ipuçları yerleştirilebilir: s2.1-pro'da [happy] ve [whispering], s1'de (happy).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `audio` | Oluşturulan konuşma, bir ses dosyası olarak. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioTextToSpeech/tr.md)

---
**Source fingerprint (SHA-256):** `6cc005ae76fc7b60d9399b1b0a3c5de40a6eff47cd6f0f0b73b4212c0270ae29`
