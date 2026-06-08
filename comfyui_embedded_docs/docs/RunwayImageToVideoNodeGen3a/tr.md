Runway Görüntüden Videoya (Gen3a Turbo) düğümü, Runway'in Gen3a Turbo modelini kullanarak tek bir başlangıç karesinden bir video oluşturur. Bir metin istemi ve başlangıç görüntü karesi alır, ardından belirtilen süre ve en boy oranına göre bir video dizisi oluşturur. Bu düğüm, oluşturmayı uzaktan işlemek için Runway'in API'sine bağlanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Oluşturma için metin istemi (varsayılan: "") | STRING | Evet | Yok |
| `başlangıç_karesi` | Video için kullanılacak başlangıç karesi | IMAGE | Evet | Yok |
| `süre` | Saniye cinsinden video süresi (varsayılan: "5") | COMBO | Evet | `"5"`<br>`"10"` |
| `oran` | Oluşturulan videonun en boy oranı (varsayılan: "1280x720") | COMBO | Evet | `"1280x720"`<br>`"720x1280"`<br>`"1920x1080"`<br>`"1080x1920"`<br>`"1080x1080"` |
| `tohum` | Oluşturma için rastgele tohum (varsayılan: 0) | INT | Hayır | 0 ila 4294967295 |

**Parametre Kısıtlamaları:**

- `start_frame` boyutları 7999x7999 pikseli geçmemelidir.
- `start_frame` en boy oranı 0,5 ile 2,0 arasında olmalıdır.
- `prompt` en az bir karakter içermelidir (boş olamaz).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dizisi | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/tr.md)

---
**Source fingerprint (SHA-256):** `4f3270ce070ce50580699292e21c5f9e3b1a56dd8ac981f67a9026ef6fc8ed76`
