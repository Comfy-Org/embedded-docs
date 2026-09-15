# Runway Görüntüden Videoya (Gen3a Turbo)

Runway Image to Video (Gen3a Turbo) düğümü, Runway'in Gen3a Turbo modelini kullanarak tek bir başlangıç karesinden video üretir. Bir metin istemi ve bir başlangıç görsel karesi alır, ardından belirtilen süre ve en-boy oranına göre bir video dizisi oluşturur. Üretim, Runway API'si aracılığıyla uzaktan işlenir. Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Üretim için metin istemi (varsayılan: "") | STRING | Evet | N/A |
| `başlangıç_karesi` | Video için kullanılacak başlangıç karesi | IMAGE | Evet | N/A |
| `süre` | Üretilen videonun saniye cinsinden süresi (varsayılan: "5") | COMBO | Evet | `"5"`<br>`"10"` |
| `oran` | Üretilen videonun en-boy oranı (varsayılan: "768:1280") | COMBO | Evet | `"768:1280"`<br>`"1280:768"` |
| `tohum` | Üretim için rastgele tohum (varsayılan: 0) | INT | Evet | 0 ile 4294967295 arası |

**Parametre Kısıtlamaları:**

- `prompt` en az bir karakter içermelidir (boş olamaz).
- `start_frame` tek bir görsel kabul eder (en fazla 1).
- `start_frame` boyutları 7999 x 7999 pikseli aşmamalıdır.
- `start_frame` 1:2 ile 2:1 arasında bir en-boy oranına sahip olmalıdır (0.5 ile 2.0).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Üretilen video dizisi | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/tr.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
