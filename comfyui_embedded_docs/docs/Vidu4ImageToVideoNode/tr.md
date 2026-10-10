# Vidu Q4 Image-to-Video Generation

Bir başlangıç karesinden ve isteğe bağlı bir istemden Vidu Q4 modeliyle video oluşturun. Çıktı, giriş görüntüsünün en-boy oranını korur.

Bir `model` seçmek, o modele özgü parametreleri gösterir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Oluşturulan videonun başlangıç karesi. En-boy oranı 1:5 ile 5:1 arasında olmalıdır. | IMAGE | Evet | N/A |
| `model` | Video oluşturmak için kullanılacak model. Bir model seçmek, ona özgü parametreleri gösterir: `prompt`, `resolution`, `duration`, `audio` ve `seed`. | DYNAMIC_COMBO | Evet | `"Vidu Q4 Preview"` |
| `prompt` | Video oluşturma için isteğe bağlı metin istemi, en fazla 5000 karakter (varsayılan: boş). | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: `"720p"`). | COMBO | Evet | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 3 - 16 |
| `audio` | Etkinleştirildiğinde, diyalog ve ses efektleri dahil olmak üzere sesli video çıkarır (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Bu parametre "oluşturma sonrası kontrol" işlevine sahiptir (varsayılan: 42). | INT | Evet | 1 - 2147483647 |

**Not:** `image` en-boy oranı 1:5 ile 5:1 arasında kalmalıdır ve `prompt` 5000 karakteri aşamaz. Sonuç, giriş görüntüsünün en-boy oranını korur, bu nedenle çıktı boyutu `resolution` ayarını yalnızca bu oran içinde takip eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu4ImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `8778696edbdfb821afaa99dcba09cbebff57fd4cd2378273e82ad9fb18600b62`
