# HeyGen Video Çeviri

Konuşulan bir videoyu ses klonlama ve dudak senkronizasyonu ile başka bir dile çevirin. Bu düğüm, orijinal konuşmacının sesini klonlar ve ağzı çevrilen konuşmayla eşleşecek şekilde yeniden canlandırarak doğal görünümlü bir sonuç üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Çevrilecek konuşmayı içeren video. | VIDEO | Evet | - |
| `output_language` | Çevrilen video için hedef dil. | COMBO | Evet | "Arabic"<br>"Bengali"<br>"Chinese"<br>"Danish"<br>"Dutch"<br>"English"<br>"French"<br>"German"<br>"Greek"<br>"Hindi"<br>"Indonesian"<br>"Italian"<br>"Japanese"<br>"Korean"<br>"Malay"<br>"Polish"<br>"Portuguese"<br>"Russian"<br>"Spanish"<br>"Swedish"<br>"Tamil"<br>"Telugu"<br>"Thai"<br>"Turkish"<br>"Ukrainian"<br>"Vietnamese" |
| `mode` | 'speed' daha hızlıdır; 'precision' daha yüksek kaliteli dudak senkronizasyonu üretir, ancak daha yüksek maliyetlidir. (varsayılan: "speed") | COMBO | Evet | "speed"<br>"precision" |
| `translate_audio_only` | Yalnızca ses parçasını değiştirir, orijinal ağız hareketlerini korur (dudak senkronizasyonu yok). (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `speaker_count` | Videodaki konuşmacı sayısı. 0 = otomatik algıla. 0'dan büyük değerler API'ye konuşmacı sayısı olarak gönderilir. (varsayılan: 0) | INT | Hayır | 0 ile 10 arası |
| `seed` | HeyGen'e gönderilmez; yeniden çalıştırmayı zorlamak için değiştirin. (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Ses klonlama ve dudak senkronizasyonu uygulanmış çevrilmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVideoTranslateNode/tr.md)

---
**Source fingerprint (SHA-256):** `709438c0c713d6db750643cc48f75352c6f293ae1ff2fd82c1bacb03b2581923`
