# TextEncodeAceStepAudio1.5

TextEncodeAceStepAudio1.5 düğümü, AceStepAudio 1.5 modeli ile kullanılmak üzere metin ve ses ile ilgili meta verileri hazırlar. Tanımlayıcı etiketleri, şarkı sözlerini ve müzik parametrelerini alır ve ardından bir CLIP modeli kullanarak bunları ses üretimi için uygun bir koşullama formatına dönüştürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Girdi metnini tokenize etmek ve kodlamak için kullanılan CLIP modeli. | CLIP | Evet | N/A |
| `tags` | Ses için tür, ruh hali veya enstrümanlar gibi tanımlayıcı etiketler. Çok satırlı girdi ve dinamik istemleri destekler. | STRING | Evet | N/A |
| `lyrics` | Ses parçası için şarkı sözleri. Çok satırlı girdi ve dinamik istemleri destekler. | STRING | Evet | N/A |
| `seed` | Tekrarlanabilir üretim için rastgele bir seed değeri. control_after_generate widget'ına sahiptir. Varsayılan: 0. | INT | Hayır | 0 ile 18446744073709551615 |
| `bpm` | Üretilen ses için dakikadaki vuruş sayısı (BPM). Varsayılan: 120. | INT | Hayır | 10 ile 300 |
| `duration` | Sesin saniye cinsinden istenen süresi. Varsayılan: 120.0. | FLOAT | Hayır | 0.0 ile 2000.0 |
| `timesignature` | Müzikal zaman işareti. | COMBO | Hayır | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` |
| `language` | Girdi metninin dili. Varsayılan: "en". | COMBO | Hayır | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` |
| `keyscale` | Müzikal ton ve gam (majör veya minör). | COMBO | Hayır | `"C major"`<br>`"C# major"`<br>`"Db major"`<br>`"D major"`<br>`"D# major"`<br>`"Eb major"`<br>`"E major"`<br>`"F major"`<br>`"F# major"`<br>`"Gb major"`<br>`"G major"`<br>`"G# major"`<br>`"Ab major"`<br>`"A major"`<br>`"A# major"`<br>`"Bb major"`<br>`"B major"`<br>`"C minor"`<br>`"C# minor"`<br>`"Db minor"`<br>`"D minor"`<br>`"D# minor"`<br>`"Eb minor"`<br>`"E minor"`<br>`"F minor"`<br>`"F# minor"`<br>`"Gb minor"`<br>`"G minor"`<br>`"G# minor"`<br>`"Ab minor"`<br>`"A minor"`<br>`"A# minor"`<br>`"Bb minor"`<br>`"B minor"` |
| `generate_audio_codes` | Ses kodları üreten LLM'yi etkinleştirir. Bu yavaş olabilir ancak üretilen sesin kalitesini artırır. Modele bir ses referansı veriyorsanız bunu kapatın. Varsayılan: True. | BOOLEAN | Hayır | N/A |
| `cfg_scale` | Sınıflandırıcısız yönlendirme ölçeği. Daha yüksek değerler çıktının istemi daha yakından takip etmesini sağlar. Varsayılan: 2.0. | FLOAT | Hayır | 0.0 ile 100.0 |
| `temperature` | Bir örnekleme sıcaklığı. Daha düşük değerler çıktının daha belirleyici olmasını sağlar. Varsayılan: 0.85. | FLOAT | Hayır | 0.0 ile 2.0 |
| `top_p` | Nükleus örnekleme olasılığı (top-p). Varsayılan: 0.9. | FLOAT | Hayır | 0.0 ile 2000.0 |
| `top_k` | Dikkate alınacak en yüksek olasılıklı token sayısı (top-k). Varsayılan: 0. | INT | Hayır | 0 ile 100 |
| `min_p` | Token örnekleme için minimum olasılık eşiği (min-p). Varsayılan: 0.000. | FLOAT | Hayır | 0.0 ile 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | AceStepAudio 1.5 modeli için kodlanmış metni ve ses parametrelerini içeren koşullama verisi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/tr.md)

---
**Source fingerprint (SHA-256):** `4bc97ec6220514b71fafde610339f2dca4ded26f68b541ed43ea492f127321f8`
