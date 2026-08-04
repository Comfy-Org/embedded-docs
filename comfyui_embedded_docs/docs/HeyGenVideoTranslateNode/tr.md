# HeyGen Video Çeviri

Konuşulan bir videoyu ses klonlama ve dudak senkronizasyonu ile başka bir dile çevirin. Bu düğüm, orijinal konuşmacının sesini klonlar ve ağzı çevrilmiş konuşmaya uyacak şekilde yeniden canlandırır, doğal görünümlü bir sonuç üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Çevrilecek konuşma içeren video. | VIDEO | Evet | - |
| `output_language` | Çevrilen videonun hedef dili. | STRING | Evet | "Arabic"<br>"Bengali"<br>"Chinese"<br>"Danish"<br>"Dutch"<br>"English"<br>"French"<br>"German"<br>"Greek"<br>"Hindi"<br>"Indonesian"<br>"Italian"<br>"Japanese"<br>"Korean"<br>"Malay"<br>"Polish"<br>"Portuguese"<br>"Russian"<br>"Spanish"<br>"Swedish"<br>"Tamil"<br>"Telugu"<br>"Thai"<br>"Turkish"<br>"Ukrainian"<br>"Vietnamese" |
| `mode` | 'speed' daha hızlıdır; 'precision' iki kat fiyata daha yüksek kaliteli dudak senkronizasyonu üretir. (varsayılan: "speed") | STRING | Evet | "speed"<br>"precision" |
| `translate_audio_only` | Yalnızca ses parçasını değiştirir, orijinal ağız hareketlerini korur (dudak senkronizasyonu yok). (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `speaker_count` | Videodaki konuşmacı sayısı. 0 = otomatik algıla. 0'ın üzerindeki değerler API'ye konuşmacı sayısı olarak gönderilir. (varsayılan: 0) | INT | Hayır | 0 to 10 |
| `seed` | HeyGen'e gönderilmez; yeniden çalıştırmayı zorlamak için değiştirin. (varsayılan: 42) | INT | Hayır | 0 to 2147483647 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Ses klonlama ve dudak senkronizasyonu uygulanmış, çevrilmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVideoTranslateNode/tr.md)

---
**Source fingerprint (SHA-256):** `31056060b6309b8ec28b37b353322403e173fd2862b56021392dba24e7a15f69`
