# Vidu2 Metinden Videoya Üretim

Vidu2 Metinden Videoya Düğümü, bir metin açıklamasından video oluşturur. İsteğinize bağlı olarak video içeriği oluşturmak için harici bir API'ye bağlanır; böylece videonun uzunluğunu, görsel stilini ve formatını kontrol edebilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak yapay zeka modeli. Şu anda yalnızca bir model mevcuttur. | COMBO | Evet | `"viduq2"` |
| `komut_istemi` | Video oluşturma için metinsel açıklama. Maksimum 2000 karakter uzunluğundadır. | STRING | Evet | - |
| `süre` | Oluşturulan videonun saniye cinsinden uzunluğu. Değer bir kaydırıcı kullanılarak ayarlanabilir (varsayılan: 5). | INT | Hayır | 1 ile 10 |
| `tohum` | Oluşturmanın rastgeleliğini kontrol etmek için kullanılan, tekrarlanabilir sonuçlar elde edilmesini sağlayan bir sayı. Oluşturma sonrasında kontrol edilebilir (varsayılan: 1). | INT | Hayır | 0 ile 2147483647 |
| `en-boy_oranı` | Videonun genişliği ile yüksekliği arasındaki oransal ilişki. | COMBO | Hayır | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `çözünürlük` | Oluşturulan videonun piksel boyutları. Bu gelişmiş bir parametredir. | COMBO | Hayır | `"720p"`<br>`"1080p"` |
| `arka_plan_müziği` | Oluşturulan videoya arka plan müziği eklenip eklenmeyeceği (varsayılan: False). Bu gelişmiş bir parametredir. | BOOLEAN | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `1e9e3629806e9b5a66d8f830d8ec33ef208a7a27b53caf43b44f7b746a85014b`
