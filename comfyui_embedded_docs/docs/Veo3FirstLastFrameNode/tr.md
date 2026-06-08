# Veo3FirstLastFrameNode

Veo3FirstLastFrameNode, Google'ın Veo 3 modelini kullanarak, video dizisinin başlangıcını ve sonunu tanımlayan sağlanan ilk ve son karelerle birlikte, bir metin istemine dayalı olarak video oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Videonun metin açıklaması (varsayılan: boş dize). | STRING | Evet | Yok |
| `negative_prompt` | Videoda kaçınılması gerekenleri yönlendiren olumsuz metin istemi (varsayılan: boş dize). | STRING | Hayır | Yok |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720p"`<br>`"1080p"`<br>`"4k"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı (varsayılan: "16:9"). | COMBO | Hayır | `"16:9"`<br>`"9:16"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 8). | INT | Hayır | 4 ila 8 |
| `seed` | Video oluşturma için tohum değeri (varsayılan: 0). | INT | Hayır | 0 ila 4294967295 |
| `first_frame` | Video için başlangıç karesi. | IMAGE | Evet | Yok |
| `last_frame` | Video için bitiş karesi. | IMAGE | Evet | Yok |
| `model` | Oluşturma için kullanılacak belirli Veo 3 modeli (varsayılan: "veo-3.1-generate"). | COMBO | Hayır | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"`<br>`"veo-3.1-lite"` |
| `generate_audio` | Video için ses oluşturma (varsayılan: Doğru). | BOOLEAN | Hayır | Yok |

**Not:** `veo-3.1-lite` modeli 4K çözünürlüğü desteklemez. `veo-3.1-lite` ve `4k` çözünürlüğü seçerseniz, bir hata oluşacaktır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `b486b22e71a305172700760bb3eff256b0e571bba75e68f27e23a1e1a1319b5a`
