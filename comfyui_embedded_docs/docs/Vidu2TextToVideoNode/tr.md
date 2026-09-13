# Vidu2 Metinden Videoya Üretim

Vidu2 Metinden Videoya Üretim düğümü, bir metin açıklamasından video oluşturur. İstemcinize dayalı video içeriği üretmek için harici bir API'ye bağlanır; videonun uzunluğunu, görsel stilini ve biçimini kontrol etmenizi sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video üretimi için kullanılacak AI modeli. Şu anda yalnızca bir model mevcuttur. | COMBO | Evet | `"viduq2"` |
| `komut_istemi` | Video üretimi için metinsel açıklama; en fazla 2000 karakter uzunluğundadır. | STRING | Evet | - |
| `süre` | Üretilen videonun saniye cinsinden uzunluğu. Değer bir kaydırıcı kullanılarak ayarlanabilir (varsayılan: 5). | INT | Hayır | 1 ila 10 |
| `tohum` | Üretimin rastgeleliğini kontrol etmek için kullanılan ve yeniden üretilebilir sonuçlara olanak tanıyan sayı. Üretimden sonra kontrol edilebilir (varsayılan: 1). | INT | Hayır | 0 ila 2147483647 |
| `en-boy_oranı` | Videonun genişliği ile yüksekliği arasındaki oransal ilişki. | COMBO | Hayır | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `çözünürlük` | Üretilen videonun piksel boyutları. Bu gelişmiş bir parametredir. | COMBO | Hayır | `"720p"`<br>`"1080p"` |
| `arka_plan_müziği` | Üretilen videoya arka plan müziği eklenip eklenmeyeceği (varsayılan: False). Bu gelişmiş bir parametredir. | BOOLEAN | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Üretilen video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `27b7c05ae1b3b23d07e775f67474ecef1ffc0bd8240f4aa2219e15949d854f27`
