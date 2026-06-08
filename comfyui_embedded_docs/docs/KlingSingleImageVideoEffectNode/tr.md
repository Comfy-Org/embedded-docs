Kling Tek Görsel Video Efekt Düğümü, tek bir referans görseline dayanarak farklı özel efektlerle videolar oluşturur. Statik görselleri dinamik video içeriğine dönüştürmek için çeşitli görsel efektler ve sahneler uygular. Düğüm, istenen görsel sonucu elde etmek için farklı efekt sahnelerini, model seçeneklerini ve video sürelerini destekler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Referans Görsel. URL veya Base64 kodlu dize (data:image ön eki olmadan). Dosya boyutu 10MB'ı geçemez, çözünürlük 300x300px'den az olamaz, en boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır | GÖRSEL | Evet | - |
| `efekt_sahnesi` | Video oluşturmaya uygulanacak özel efekt sahnesinin türü. Bazı efektler farklı fiyatlandırmaya sahip olabilir. | KOMBO | Evet | `"dizzydizzy"`<br>`"bloombloom"`<br>`"neon"`<br>`"cartoon"`<br>`"sketch"`<br>`"oil"`<br>`"watercolor"`<br>`"3d"` |
| `model_adı` | Video efektini oluşturmak için kullanılacak belirli model sürümü. | KOMBO | Evet | `"kling-v1-5"`<br>`"kling-v1-6"` |
| `süre` | Oluşturulan videonun saniye cinsinden uzunluğu. | KOMBO | Evet | `"5"`<br>`"10"` |

**Not:** `effect_scene` parametresi, düğümün fiyatlandırmasını etkiler. `dizzydizzy` ve `bloombloom` efektleri, oluşturma başına 0,49 ABD Doları tutarındayken, diğer tüm efektler oluşturma başına 0,28 ABD Doları tutarındadır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video_kimliği` | Uygulanan efektlerle oluşturulan video | VİDEO |
| `süre` | Oluşturulan video için benzersiz tanımlayıcı | METİN |
| `süre` | Oluşturulan videonun süresi | METİN |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/tr.md)

---
**Source fingerprint (SHA-256):** `519db2f7185f200140c746bdebf89383523e0342bbfb61538adac063295d365d`
