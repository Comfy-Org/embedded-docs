> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen4/tr.md)

Runway Görüntüden Videoya (Gen4 Turbo) düğümü, Runway'in Gen4 Turbo modelini kullanarak tek bir başlangıç karesinden bir video oluşturur. Bir metin istemi ve bir başlangıç görüntü karesi alır, ardından belirtilen süre ve en boy oranı ayarlarına göre bir video dizisi oluşturur. Düğüm, başlangıç karesini Runway'in API'sine yüklemeyi yönetir ve oluşturulan videoyu döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Oluşturma için metin istemi (varsayılan: boş dize) |
| `start_frame` | IMAGE | Evet | - | Video için kullanılacak başlangıç karesi |
| `duration` | COMBO | Evet | `"5"`<br>`"10"` | Video süresi saniye cinsinden (varsayılan: "5") |
| `ratio` | COMBO | Evet | `"1024:1024"`<br>`"1280:720"`<br>`"720:1280"`<br>`"1920:1080"`<br>`"1080:1920"`<br>`"2048:1080"`<br>`"1080:2048"` | Oluşturulan video için en boy oranı (varsayılan: "1024:1024") |
| `seed` | INT | Hayır | 0 ile 4294967295 arası | Oluşturma için rastgele tohum değeri (varsayılan: 0) |

**Parametre Kısıtlamaları:**

- `start_frame` görüntüsünün boyutları 7999x7999 pikseli geçmemelidir
- `start_frame` görüntüsünün en boy oranı 0,5 ile 2,0 arasında olmalıdır
- `prompt` en az bir karakter içermelidir

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Giriş karesi ve istemine göre oluşturulan video |

---
**Source fingerprint (SHA-256):** `ebb5f1cd5e6bf6e0fcfb4910c774c087980daf9a1987900ad966120608b924e7`
