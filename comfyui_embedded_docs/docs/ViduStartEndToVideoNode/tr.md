Vidu Başlangıç-Bitiş Video Oluşturma düğümü, bir başlangıç karesi ile bir bitiş karesi arasındaki kareleri oluşturarak bir video meydana getirir. Video oluşturma sürecini yönlendirmek için bir metin istemi kullanır ve farklı çözünürlük ile hareket ayarlarına sahip çeşitli video modellerini destekler. Düğüm, işleme başlamadan önce başlangıç ve bitiş karelerinin uyumlu en-boy oranlarına sahip olduğunu doğrular.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Model adı | COMBO | Evet | `"viduq1"` |
| `ilk_kare` | Başlangıç karesi | IMAGE | Evet | - |
| `bitiş_karesi` | Bitiş karesi | IMAGE | Evet | - |
| `istem` | Video oluşturma için metinsel açıklama | STRING | Hayır | - |
| `süre` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5, 5 saniyeye sabitlenmiştir) | INT | Hayır | 5-5 |
| `tohum` | Video oluşturma için tohum değeri (0: rastgele) (varsayılan: 0) | INT | Hayır | 0-2147483647 |
| `çözünürlük` | Desteklenen değerler modele ve süreye göre değişiklik gösterebilir (varsayılan: "1080p") | COMBO | Hayır | `"1080p"` |
| `hareket genliği` | Karedeki nesnelerin hareket genliği (varsayılan: "auto") | COMBO | Hayır | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Not:** Başlangıç ve bitiş kareleri uyumlu en-boy oranlarına sahip olmalıdır (min_rel=0.8, max_rel=1.25 oran toleransı ile doğrulanır).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduStartEndToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `d859d67b3ff73977b95e3903b461509f933f9652fedc016e1cd362f6bef1b8dc`
