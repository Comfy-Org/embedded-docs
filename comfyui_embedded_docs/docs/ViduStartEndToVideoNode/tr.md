> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduStartEndToVideoNode/tr.md)

Vidu Start End To Video Generation düğümü, bir başlangıç karesi ile bir bitiş karesi arasında kareler oluşturarak bir video yaratır. Video oluşturma sürecini yönlendirmek için bir metin istemi kullanır ve farklı çözünürlük ve hareket ayarlarına sahip çeşitli video modellerini destekler. Düğüm, işleme başlamadan önce başlangıç ve bitiş karelerinin uyumlu en-boy oranlarına sahip olduğunu doğrular.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"vidu_q1"`<br>[VideoModelName enum'ından diğer model değerleri] | Model adı (varsayılan: "vidu_q1") |
| `first_frame` | IMAGE | Evet | - | Başlangıç karesi |
| `end_frame` | IMAGE | Evet | - | Bitiş karesi |
| `prompt` | STRING | Hayır | - | Video oluşturma için metinsel açıklama |
| `duration` | INT | Hayır | 5-5 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5, 5 saniyede sabitlenmiştir) |
| `seed` | INT | Hayır | 0-2147483647 | Video oluşturma için tohum değeri (0 rastgele için) (varsayılan: 0) |
| `resolution` | COMBO | Hayır | `"1080p"`<br>[Resolution enum'ından diğer çözünürlük değerleri] | Desteklenen değerler modele ve süreye göre değişebilir (varsayılan: "1080p") |
| `movement_amplitude` | COMBO | Hayır | `"auto"`<br>[MovementAmplitude enum'ından diğer hareket genliği değerleri] | Karedeki nesnelerin hareket genliği (varsayılan: "auto") |

**Not:** Başlangıç ve bitiş kareleri uyumlu en-boy oranlarına sahip olmalıdır (min_rel=0.8, max_rel=1.25 oran toleransı ile doğrulanır).

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası |