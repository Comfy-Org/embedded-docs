# Runway Görüntüden Videoya (Gen4 Turbo)

Runway Görüntüden Videoya (Gen4 Turbo) düğümü, Runway'in Gen4 Turbo modelini kullanarak tek bir başlangıç karesinden bir video oluşturur. Bir metin istemi ve bir başlangıç görüntü karesi alır, ardından belirtilen süre ve en boy oranı ayarlarına göre bir video dizisi oluşturur. Düğüm, başlangıç karesini Runway'in API'sine yüklemeyi yönetir ve oluşturulan videoyu döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Oluşturma için metin istemi (varsayılan: boş dize) | STRING | Evet | - |
| `başlangıç_karesi` | Video için kullanılacak başlangıç karesi | IMAGE | Evet | - |
| `süre` | Video süresi saniye cinsinden (varsayılan: "5") | COMBO | Evet | `"5"`<br>`"10"` |
| `oran` | Oluşturulan video için en boy oranı (varsayılan: "1024:1024") | COMBO | Evet | `"1024:1024"`<br>`"1280:720"`<br>`"720:1280"`<br>`"1920:1080"`<br>`"1080:1920"`<br>`"2048:1080"`<br>`"1080:2048"` |
| `tohum` | Oluşturma için rastgele tohum değeri (varsayılan: 0) | INT | Hayır | 0 ile 4294967295 arası |

**Parametre Kısıtlamaları:**

- `start_frame` görüntüsünün boyutları 7999x7999 pikseli geçmemelidir
- `start_frame` görüntüsünün en boy oranı 0,5 ile 2,0 arasında olmalıdır
- `prompt` en az bir karakter içermelidir

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Giriş karesi ve istemine göre oluşturulan video | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen4/tr.md)

---
**Source fingerprint (SHA-256):** `ebb5f1cd5e6bf6e0fcfb4910c774c087980daf9a1987900ad966120608b924e7`
