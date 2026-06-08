Vidu Referans Video Düğümü, birden fazla referans görseli ve bir metin istemi kullanarak videolar oluşturur. Sağlanan görsellere ve açıklamaya dayanarak tutarlı video içeriği üretmek için yapay zeka modellerini kullanır. Düğüm, süre, en boy oranı, çözünürlük ve hareket kontrolü dahil olmak üzere çeşitli video ayarlarını destekler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için model adı (varsayılan: "viduq1") | COMBO | Evet | `"viduq1"` |
| `görseller` | Tutarlı özneler içeren bir video oluşturmak için referans olarak kullanılacak görseller (en fazla 7 görsel) | IMAGE | Evet | - |
| `prompt` | Video oluşturma için metinsel bir açıklama | STRING | Evet | - |
| `süre` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5) | INT | Hayır | 5-5 |
| `tohum` | Video oluşturma için tohum değeri (0 rastgele için) (varsayılan: 0) | INT | Hayır | 0-2147483647 |
| `en-boy oranı` | Çıktı videosunun en boy oranı (varsayılan: "16:9") | COMBO | Hayır | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `çözünürlük` | Desteklenen değerler modele ve süreye göre değişebilir (varsayılan: "1080p") | COMBO | Hayır | `"1080p"` |
| `hareket genliği` | Karedeki nesnelerin hareket genliği (varsayılan: "auto") | COMBO | Hayır | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Kısıtlamalar ve Sınırlamalar:**

- `prompt` alanı zorunludur ve boş olamaz
- Referans için en fazla 7 görsele izin verilir
- Her görselin en boy oranı 1:4 ile 4:1 arasında olmalıdır
- Her görselin minimum boyutları 128x128 piksel olmalıdır
- Süre 5 saniye olarak sabitlenmiştir

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Referans görsellere ve isteme dayalı olarak oluşturulan video | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `11a7de2f50658467f63d284ef6b95d91dcdd39b4e6e5cea3b8d2f2a5d63a3020`
