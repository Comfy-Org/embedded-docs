# Runway İlk-Son-Kare'den Videoya

Runway First-Last-Frame to Video düğümü, bir başlangıç karesi, bir bitiş karesi ve bir metin istemi kullanarak bir video oluşturur. Runway'in gen3a_turbo modelini kullanarak sağlanan iki ana kare arasında yumuşak bir geçiş oluşturur. Bitiş karesinin başlangıç karesinden tamamen farklı olduğu karmaşık geçişler için özellikle kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturma için metin istemi (varsayılan: boş dize) | STRING | Evet | N/A |
| `başlangıç_karesi` | Video için kullanılacak başlangıç karesi | IMAGE | Evet | N/A |
| `bitiş_karesi` | Video için kullanılacak bitiş karesi. Yalnızca gen3a_turbo için desteklenir. | IMAGE | Evet | N/A |
| `süre` | Oluşturulan videonun saniye cinsinden süresi. Daha uzun olan 10s süre, oluşturma işlemine başlangıç ve bitiş kareleri arasında yumuşak geçiş için daha fazla zaman tanır (varsayılan: "5"). | COMBO | Evet | `"5"`<br>`"10"` |
| `oran` | Oluşturulan video için en-boy oranı (varsayılan: "768:1280") | COMBO | Evet | `"768:1280"`<br>`"1280:768"` |
| `tohum` | Oluşturma için rastgele tohum (seed). Rastgele tohum için 0 olarak ayarlayın (varsayılan: 0). | INT | Hayır | 0 ile 4294967295 |

**Parametre Kısıtlamaları:**

- `prompt` en az 1 karakter içermelidir
- Hem `start_frame` hem de `end_frame` maksimum 7999x7999 piksel boyutlarına sahip olmalıdır
- Hem `start_frame` hem de `end_frame`, 0.5 ile 2.0 arasında en-boy oranına sahip olmalıdır
- `end_frame` parametresi yalnızca gen3a_turbo modeli kullanıldığında desteklenir

**Notlar:**

- Oluşturma maliyeti seçilen süreye göre hesaplanır: saniye başına USD 0.0715 (5 saniye için USD 0.3575, 10 saniye için USD 0.715)
- Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Başlangıç ve bitiş kareleri arasında geçiş yapan oluşturulan video | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `1d8720aba833348583d2aa37e13a1ad43d9055b0201c9cb6ad9c95dada7e5056`
