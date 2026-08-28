# Runway Görüntüden Videoya (Gen3a Turbo)

The Runway Image to Video (Gen3a Turbo) düğümü, Runway'in Gen3a Turbo modelini kullanarak tek bir başlangıç karesinden video oluşturur. Bir metin istemi ve başlangıç görüntü karesi alır, ardından belirtilen süreye ve en boy oranına göre bir video dizisi oluşturur. Bu düğüm, üretimi uzaktan işlemek için Runway'in API'sine bağlanır. Runway, üretim öncesinde en iyi uygulamalar rehberini incelemenizi önerir: https://help.runwayml.com/hc/en-us/articles/33927968552339-Creating-with-Act-One-on-Gen-3-Alpha-and-Turbo. Bu düğüm kullanımdan kaldırılmıştır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Üretim için metin istemi (varsayılan: "") | STRING | Evet | Yok |
| `başlangıç_karesi` | Video için kullanılacak başlangıç karesi | IMAGE | Evet | Yok |
| `süre` | Saniye cinsinden video süresi (varsayılan: "5") | COMBO | Evet | `"5"`<br>`"10"` |
| `oran` | Oluşturulan videonun en boy oranı (varsayılan: "768:1280") | COMBO | Evet | `"768:1280"`<br>`"1280:768"` |
| `tohum` | Üretim için rastgele tohum (varsayılan: 0) | INT | Evet | 0 ila 4294967295 |

**Parametre Kısıtlamaları:**

- `start_frame` boyutları 7999x7999 pikseli aşmamalıdır.
- `start_frame` en boy oranı 0.5 ile 2.0 arasında olmalıdır.
- `start_frame` yalnızca tek bir görüntü kabul eder (en fazla 1).
- `prompt` en az bir karakter içermelidir (boş olamaz).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dizisi | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/tr.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
