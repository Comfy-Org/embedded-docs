> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/tr.md)

Bu düğüm, bir metin istemi ve en fazla yedi referans görseline dayanarak video oluşturmak için Kling AI modelini kullanır. Videonun en-boy oranını, süresini, çözünürlüğünü kontrol etmenize ve isteğe bağlı olarak storyboard'lar kullanmanıza veya ses oluşturmanıza olanak tanır. Düğüm, isteği harici bir API'ye gönderir ve oluşturulan videoyu döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Evet | `"kling-v3-omni"`<br>`"kling-video-o1"` | Video oluşturma için kullanılacak belirli Kling modeli (varsayılan: "kling-v3-omni"). |
| `prompt` | STRING | Evet | - | Video içeriğini tanımlayan bir metin istemi. Bu, hem olumlu hem de olumsuz açıklamalar içerebilir. Metin otomatik olarak normalleştirilir ve 1 ile 2500 karakter arasında olmalıdır. Storyboard'lar etkinleştirildiğinde yok sayılır. |
| `aspect_ratio` | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Oluşturulan video için istenen en-boy oranı. |
| `duration` | INT | Evet | 3 ila 15 | Videonun saniye cinsinden uzunluğu. Değer bir kaydırıcı ile ayarlanabilir (varsayılan: 5). |
| `reference_images` | IMAGE | Evet | - | En fazla 7 referans görseli. Her görsel en az 300x300 piksel olmalı ve en-boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. |
| `resolution` | COMBO | Hayır | `"4k"`<br>`"1080p"`<br>`"720p"` | Videonun çıktı çözünürlüğü. Bu parametre isteğe bağlıdır (varsayılan: "1080p"). |
| `hikaye_tahtaları` | DYNAMIC_COMBO | Hayır | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` | Bireysel istemler ve sürelerle bir dizi video segmenti oluşturun. Yalnızca `kling-v3-omni` için desteklenir. Etkinleştirildiğinde, genel `prompt` yok sayılır ve tüm storyboard segmentlerinin toplam süresi genel `duration` değerine eşit olmalıdır. |
| `ses_oluştur` | BOOLEAN | Hayır | `true`<br>`false` | Video için ses oluşturun. Yalnızca `kling-v3-omni` için desteklenir (varsayılan: false). |
| `seed` | INT | Hayır | 0 ila 2147483647 | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). |

**Not:** `reference_images` girişi en fazla 7 görsel kabul eder. Daha fazlası sağlanırsa, düğüm bir hata verecektir. Her görsel, minimum boyutlar ve en-boy oranı için doğrulanır.

**Modele özgü kısıtlamalar:**
- `kling-video-o1`, 10 saniyeden uzun süreleri desteklemez.
- `kling-video-o1`, ses oluşturmayı desteklemez.
- `kling-video-o1`, 4k çözünürlüğü desteklemez.
- `kling-video-o1`, storyboard'ları desteklemez.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `80f4568be81b23c75bfff2bd3f21a61b242563c3c9fb1985a03e76ace24dceb2`
