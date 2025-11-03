> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/tr.md)

Vidu Metinden Videoya Oluşturma düğümü, metin açıklamalarından video oluşturur. Metin ifadelerinizi, süre, en-boy oranı ve görsel stil için özelleştirilebilir ayarlarla video içeriğine dönüştürmek üzere çeşitli video oluşturma modellerini kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `vidu_q1`<br>*Diğer VideoModelName seçenekleri* | Model adı (varsayılan: vidu_q1) |
| `prompt` | STRING | Evet | - | Video oluşturma için metinsel açıklama |
| `duration` | INT | Hayır | 5-5 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5) |
| `seed` | INT | Hayır | 0-2147483647 | Video oluşturma için tohum değeri (0 rastgele için) (varsayılan: 0) |
| `aspect_ratio` | COMBO | Hayır | `r_16_9`<br>*Diğer AspectRatio seçenekleri* | Çıktı videosunun en-boy oranı (varsayılan: r_16_9) |
| `resolution` | COMBO | Hayır | `r_1080p`<br>*Diğer Resolution seçenekleri* | Desteklenen değerler modele ve süreye göre değişiklik gösterebilir (varsayılan: r_1080p) |
| `movement_amplitude` | COMBO | Hayır | `auto`<br>*Diğer MovementAmplitude seçenekleri* | Karedeki nesnelerin hareket genliği (varsayılan: auto) |

**Not:** `prompt` alanı zorunludur ve boş bırakılamaz. `duration` parametresi şu anda 5 saniyede sabitlenmiştir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Metin ifadesine dayalı olarak oluşturulan video |