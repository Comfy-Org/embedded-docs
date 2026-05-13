> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2TextToVideoNode/tr.md)

Vidu2 Metinden Videoya Düğümü, bir metin açıklamasından video oluşturur. İsteğinize bağlı olarak video içeriği oluşturmak için harici bir API'ye bağlanır; böylece videonun uzunluğunu, görsel stilini ve formatını kontrol edebilirsiniz.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `model` | COMBO | Evet | `"viduq2"` | Video oluşturma için kullanılacak yapay zeka modeli. Şu anda yalnızca bir model mevcuttur. |
| `prompt` | STRING | Evet | - | Video oluşturma için metinsel açıklama. Maksimum 2000 karakter uzunluğundadır. |
| `duration` | INT | Hayır | 1 ile 10 | Oluşturulan videonun saniye cinsinden uzunluğu. Değer bir kaydırıcı kullanılarak ayarlanabilir (varsayılan: 5). |
| `seed` | INT | Hayır | 0 ile 2147483647 | Oluşturmanın rastgeleliğini kontrol etmek için kullanılan, tekrarlanabilir sonuçlar elde edilmesini sağlayan bir sayı. Oluşturma sonrasında kontrol edilebilir (varsayılan: 1). |
| `aspect_ratio` | COMBO | Hayır | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` | Videonun genişliği ile yüksekliği arasındaki oransal ilişki. |
| `resolution` | COMBO | Hayır | `"720p"`<br>`"1080p"` | Oluşturulan videonun piksel boyutları. Bu gelişmiş bir parametredir. |
| `background_music` | BOOLEAN | Hayır | - | Oluşturulan videoya arka plan müziği eklenip eklenmeyeceği (varsayılan: False). Bu gelişmiş bir parametredir. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `1e9e3629806e9b5a66d8f830d8ec33ef208a7a27b53caf43b44f7b746a85014b`
