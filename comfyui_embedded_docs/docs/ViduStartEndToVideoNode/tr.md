> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduStartEndToVideoNode/tr.md)

Vidu Başlangıç-Bitiş Video Oluşturma düğümü, bir başlangıç karesi ile bir bitiş karesi arasındaki kareleri oluşturarak bir video meydana getirir. Video oluşturma sürecini yönlendirmek için bir metin istemi kullanır ve farklı çözünürlük ile hareket ayarlarına sahip çeşitli video modellerini destekler. Düğüm, işleme başlamadan önce başlangıç ve bitiş karelerinin uyumlu en-boy oranlarına sahip olduğunu doğrular.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"viduq1"` | Model adı |
| `ilk_kare` | IMAGE | Evet | - | Başlangıç karesi |
| `bitiş_karesi` | IMAGE | Evet | - | Bitiş karesi |
| `istem` | STRING | Hayır | - | Video oluşturma için metinsel açıklama |
| `süre` | INT | Hayır | 5-5 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5, 5 saniyeye sabitlenmiştir) |
| `tohum` | INT | Hayır | 0-2147483647 | Video oluşturma için tohum değeri (0: rastgele) (varsayılan: 0) |
| `çözünürlük` | COMBO | Hayır | `"1080p"` | Desteklenen değerler modele ve süreye göre değişiklik gösterebilir (varsayılan: "1080p") |
| `hareket genliği` | COMBO | Hayır | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` | Karedeki nesnelerin hareket genliği (varsayılan: "auto") |

**Not:** Başlangıç ve bitiş kareleri uyumlu en-boy oranlarına sahip olmalıdır (min_rel=0.8, max_rel=1.25 oran toleransı ile doğrulanır).

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası |

---
**Source fingerprint (SHA-256):** `d859d67b3ff73977b95e3903b461509f933f9652fedc016e1cd362f6bef1b8dc`
