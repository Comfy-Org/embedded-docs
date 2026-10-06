# Vidu Metinden Video Oluşturma

Lütfen aşağıdaki belgeyi Türkçeye çevirin (belgenin başlangıç notunu dahil etmeyin):

Vidu Metinden Videoya Oluşturma düğümü, metin açıklamalarından videolar oluşturur. Metin istemlerinizi, süre, en boy oranı ve görsel stil için özelleştirilebilir ayarlarla video içeriğine dönüştürmek için Vidu video oluşturma modelini kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Model adı | COMBO | Evet | `viduq1` |
| `prompt` | Video oluşturma için metinsel açıklama | STRING | Evet | - |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5) | INT | Hayır | 5-5 |
| `seed` | Video oluşturma için tohum değeri (0 rastgele için) (varsayılan: 0) | INT | Hayır | 0-2147483647 |
| `aspect_ratio` | Çıktı videosunun en boy oranı | COMBO | Hayır | `16:9`<br>`9:16`<br>`1:1` |
| `resolution` | Desteklenen değerler modele ve süreye göre değişiklik gösterebilir | COMBO | Hayır | `1080p` |
| `movement_amplitude` | Karedeki nesnelerin hareket genliği | COMBO | Hayır | `auto`<br>`small`<br>`medium`<br>`large` |

**Not:** `prompt` alanı zorunludur ve boş olamaz. `duration` parametresi şu anda 5 saniye olarak sabitlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Metin istemine göre oluşturulan video | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `0d331d3eab8a4af9c90831f3f8fd8ae34aa0c393142cb6f89404edc94024d95f`
