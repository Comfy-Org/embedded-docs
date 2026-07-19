# Vidu Görselden Video Oluşturma

Vidu Görüntüden Videoya Dönüştürme düğümü, bir başlangıç görüntüsü ve isteğe bağlı bir metin açıklaması kullanarak kısa bir video oluşturur. Sağlanan görüntü karesinden devam eden video içeriği üretmek için bir yapay zeka modeli kullanır ve sonuçta oluşan videoyu döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Model adı (varsayılan: viduq1) | COMBO | Evet | `viduq1` |
| `görsel` | Oluşturulacak videonun başlangıç karesi olarak kullanılacak bir görüntü | IMAGE | Evet | - |
| `prompt` | Video oluşturma için metinsel açıklama (varsayılan: boş) | STRING | Hayır | - |
| `süre` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5, 5 saniyeye sabitlenmiştir) | INT | Hayır | 5-5 |
| `tohum` | Video oluşturma için tohum değeri (0 rastgele anlamına gelir) (varsayılan: 0) | INT | Hayır | 0-2147483647 |
| `çözünürlük` | Desteklenen değerler modele ve süreye göre değişiklik gösterebilir (varsayılan: 1080p) | COMBO | Hayır | `1080p` |
| `hareket_genliği` | Karedeki nesnelerin hareket genliği (varsayılan: auto) | COMBO | Hayır | `auto`<br>`small`<br>`medium`<br>`large` |

**Kısıtlamalar:**

- Yalnızca bir giriş görüntüsüne izin verilir (birden fazla görüntü işlenemez).
- Giriş görüntüsünün en-boy oranı 1:4 ile 4:1 arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video çıktısı | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `064b3efba8219770595e68a6607a6f8113d1be7c9f3863a4740ee5c3a146d91e`
