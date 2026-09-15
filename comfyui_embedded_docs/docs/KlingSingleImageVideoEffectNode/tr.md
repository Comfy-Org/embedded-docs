# KlingSingleImageVideoEffectNode

Kling Tek Görsel Video Efekti Düğümü, tek bir referans görsele dayalı olarak farklı özel efektlerle videolar oluşturur. Statik görselleri dinamik video içeriğine dönüştürmek için çeşitli görsel efektler ve sahneler uygular. Düğüm, istenen görsel sonucu elde etmek için farklı efekt sahnelerini, model seçeneklerini ve video sürelerini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Referans Görsel. URL veya Base64 kodlu dize (data:image öneki olmadan). Dosya boyutu 10 MB'ı aşamaz, çözünürlük 300x300 pikselden az olamaz, en-boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır | IMAGE | Evet | - |
| `effect_scene` | Video oluşturmaya uygulanacak özel efekt sahnesinin türü. Bazı efektlerin fiyatlandırması farklı olabilir. | COMBO | Evet | `"dizzydizzy"`<br>`"bloombloom"`<br>`"neon"`<br>`"cartoon"`<br>`"sketch"`<br>`"oil"`<br>`"watercolor"`<br>`"3d"` |
| `model_name` | Video efektini oluşturmak için kullanılacak belirli model sürümü. | COMBO | Evet | `"kling-v1-5"`<br>`"kling-v1-6"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu. | COMBO | Evet | `"5"`<br>`"10"` |

**Not:** `effect_scene` parametresi düğümün fiyatlandırmasını etkiler. `dizzydizzy` ve `bloombloom` efektleri oluşturma başına 0,49 ABD doları tutarındadır; diğer tüm efektler ise oluşturma başına 0,28 ABD doları tutarındadır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Uygulanan efektlerle oluşturulan video | VIDEO |
| `video_id` | Oluşturulan videonun benzersiz tanımlayıcısı | STRING |
| `duration` | Oluşturulan videonun süresi | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/tr.md)

---
**Source fingerprint (SHA-256):** `fb4a8b044daa99154a58d6926ff746bd2397b71ea32f1fafc851589f163ab51a`
