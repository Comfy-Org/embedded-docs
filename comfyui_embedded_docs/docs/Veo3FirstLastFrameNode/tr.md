> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/tr.md)

# Veo3FirstLastFrameNode

Veo3FirstLastFrameNode, Google'ın Veo 3 modelini kullanarak, video dizisinin başlangıcını ve sonunu tanımlayan sağlanan ilk ve son karelerle birlikte, bir metin istemine dayalı olarak video oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | Videonun metin açıklaması (varsayılan: boş dize). |
| `negative_prompt` | STRING | Hayır | Yok | Videoda kaçınılması gerekenleri yönlendiren olumsuz metin istemi (varsayılan: boş dize). |
| `resolution` | COMBO | Evet | `"720p"`<br>`"1080p"`<br>`"4k"` | Çıktı videosunun çözünürlüğü. |
| `aspect_ratio` | COMBO | Hayır | `"16:9"`<br>`"9:16"` | Çıktı videosunun en-boy oranı (varsayılan: "16:9"). |
| `duration` | INT | Hayır | 4 ila 8 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 8). |
| `seed` | INT | Hayır | 0 ila 4294967295 | Video oluşturma için tohum değeri (varsayılan: 0). |
| `first_frame` | IMAGE | Evet | Yok | Video için başlangıç karesi. |
| `last_frame` | IMAGE | Evet | Yok | Video için bitiş karesi. |
| `model` | COMBO | Hayır | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"`<br>`"veo-3.1-lite"` | Oluşturma için kullanılacak belirli Veo 3 modeli (varsayılan: "veo-3.1-generate"). |
| `generate_audio` | BOOLEAN | Hayır | Yok | Video için ses oluşturma (varsayılan: Doğru). |

**Not:** `veo-3.1-lite` modeli 4K çözünürlüğü desteklemez. `veo-3.1-lite` ve `4k` çözünürlüğü seçerseniz, bir hata oluşacaktır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `b486b22e71a305172700760bb3eff256b0e571bba75e68f27e23a1e1a1319b5a`
