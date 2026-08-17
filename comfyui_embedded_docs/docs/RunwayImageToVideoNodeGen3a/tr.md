# Runway Görüntüden Videoya (Gen3a Turbo)

Runway Image to Video (Gen3a Turbo) düğümü, Runway'in Gen3a Turbo modelini kullanarak tek bir başlangıç karesinden video oluşturur. Bir metin istemi ve başlangıç görüntü karesi alır, ardından belirtilen süreye ve en boy oranına göre bir video dizisi oluşturur. Bu düğüm, üretimi uzaktan işlemek için Runway'in API'sine bağlanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturma için metin istemi (varsayılan: "") | STRING | Evet | N/A |
| `start_frame` | Video için kullanılacak başlangıç karesi | IMAGE | Evet | N/A |
| `duration` | Video süresi (saniye cinsinden) (varsayılan: "5") | COMBO | Evet | `"5"`<br>`"10"` |
| `ratio` | Oluşturulan videonun en boy oranı (varsayılan: "768:1280") | COMBO | Evet | `"768:1280"`<br>`"1280:768"` |
| `seed` | Üretim için rastgele tohum (varsayılan: 0) | INT | Hayır | 0 ile 4294967295 arası |

**Parametre Kısıtlamaları:**

- `start_frame` boyutları 7999x7999 pikseli aşmamalıdır.
- `start_frame` 0,5 ile 2,0 arasında bir en boy oranına sahip olmalıdır.
- `prompt` en az bir karakter içermelidir (boş olamaz).

**Notlar:**

- Bu düğüm kullanımdan kaldırılmıştır.
- Üretimden önce Runway, en iyi uygulamalar rehberini incelemenizi önerir: https://help.runwayml.com/hc/en-us/articles/33927968552339-Creating-with-Act-One-on-Gen-3-Alpha-and-Turbo

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dizisi | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/tr.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
