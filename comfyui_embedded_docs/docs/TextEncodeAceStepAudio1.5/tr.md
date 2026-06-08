TextEncodeAceStepAudio1.5 düğümü, metin ve sesle ilgili meta verileri AceStepAudio 1.5 modeliyle kullanılmak üzere hazırlar. Tanımlayıcı etiketleri, şarkı sözlerini ve müzikal parametreleri alır, ardından bunları bir CLIP modeli kullanarak ses üretimine uygun bir koşullandırma formatına dönüştürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Giriş metnini tokenleştirmek ve kodlamak için kullanılan CLIP modeli. | CLIP | Evet | Yok |
| `tags` | Ses için tür, ruh hali veya enstrümanlar gibi tanımlayıcı etiketler. Çok satırlı girişi ve dinamik istemleri destekler. | STRING | Evet | Yok |
| `lyrics` | Ses parçası için şarkı sözleri. Çok satırlı girişi ve dinamik istemleri destekler. | STRING | Evet | Yok |
| `seed` | Tekrarlanabilir üretim için rastgele bir tohum değeri. `control_after_generate` widget'ına sahiptir. Varsayılan: 0. | INT | Hayır | 0 ile 18446744073709551615 arası |
| `bpm` | Üretilen ses için dakikadaki vuruş sayısı (BPM). Varsayılan: 120. | INT | Hayır | 10 ile 300 arası |
| `duration` | Sesin saniye cinsinden istenen süresi. Varsayılan: 120,0. | FLOAT | Hayır | 0,0 ile 2000,0 arası |
| `timesignature` | Müziksel zaman işareti. | COMBO | Hayır | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` |
| `language` | Giriş metninin dili. Varsayılan: "en". | COMBO | Hayır | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` |
| `keyscale` | Müziksel anahtar ve dizi (majör veya minör). | COMBO | Hayır | `"C major"`<br>`"C minor"`<br>`"C# major"`<br>`"C# minor"`<br>`"Db major"`<br>`"Db minor"`<br>`"D major"`<br>`"D minor"`<br>`"D# major"`<br>`"D# minor"`<br>`"Eb major"`<br>`"Eb minor"`<br>`"E major"`<br>`"E minor"`<br>`"F major"`<br>`"F minor"`<br>`"F# major"`<br>`"F# minor"`<br>`"Gb major"`<br>`"Gb minor"`<br>`"G major"`<br>`"G minor"`<br>`"G# major"`<br>`"G# minor"`<br>`"Ab major"`<br>`"Ab minor"`<br>`"A major"`<br>`"A minor"`<br>`"A# major"`<br>`"A# minor"`<br>`"Bb major"`<br>`"Bb minor"`<br>`"B major"`<br>`"B minor"` |
| `generate_audio_codes` | Ses kodlarını oluşturan LLM'yi etkinleştirir. Bu yavaş olabilir ancak üretilen sesin kalitesini artırır. Modele bir ses referansı veriyorsanız bunu kapatın. Varsayılan: True. | BOOLEAN | Hayır | Yok |
| `cfg_scale` | Sınıflandırıcısız yönlendirme ölçeği. Daha yüksek değerler, çıktının istemi daha yakından takip etmesini sağlar. Varsayılan: 2,0. | FLOAT | Hayır | 0,0 ile 100,0 arası |
| `temperature` | Bir örnekleme sıcaklığı. Daha düşük değerler çıktıyı daha deterministik hale getirir. Varsayılan: 0,85. | FLOAT | Hayır | 0,0 ile 2,0 arası |
| `top_p` | Çekirdek örnekleme olasılığı (top-p). Varsayılan: 0,9. | FLOAT | Hayır | 0,0 ile 2000,0 arası |
| `top_k` | Dikkate alınacak en yüksek olasılıklı token sayısı (top-k). Varsayılan: 0. | INT | Hayır | 0 ile 100 arası |
| `min_p` | Token örneklemesi için minimum olasılık eşiği (min-p). Varsayılan: 0,000. | FLOAT | Hayır | 0,0 ile 1,0 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | AceStepAudio 1.5 modeli için kodlanmış metin ve ses parametrelerini içeren koşullandırma verileri. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/tr.md)

---
**Source fingerprint (SHA-256):** `df70a55024812d8c77a3b618cbff6d3148a3f3f5fc4d17dd3c4282ce7f3cbc2c`
