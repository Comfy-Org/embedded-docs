> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoExtendNode/tr.md)

Kling Video Extend Node, diğer Kling düğümleri tarafından oluşturulan videoları genişletmenize olanak tanır. Video ID'si ile tanımlanan mevcut bir videoyu alır ve metin prompt'larınıza dayalı olarak ek içerik oluşturur. Düğüm, genişletme isteğinizi Kling API'sine göndererek genişletilmiş videoyu ve yeni ID'si ile süresini döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Hayır | - | Video genişletmeyi yönlendirmek için olumlu metin prompt'u |
| `negative_prompt` | STRING | Hayır | - | Genişletilmiş videoda kaçınılacak öğeler için olumsuz metin prompt'u |
| `cfg_scale` | FLOAT | Hayır | 0.0 - 1.0 | Prompt rehberliğinin gücünü kontrol eder (varsayılan: 0.5) |
| `video_id` | STRING | Evet | - | Genişletilecek videonun ID'si. Metinden videoya, görüntüden videoya ve önceki video genişletme işlemleri tarafından oluşturulan videoları destekler. Genişletmeden sonra toplam süre 3 dakikayı aşamaz. |

**Not:** `video_id` parametresi, diğer Kling düğümleri tarafından oluşturulmuş bir videoyu referans almalıdır ve genişletmeden sonraki toplam süre 3 dakikayı aşamaz.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Kling API'si tarafından oluşturulan genişletilmiş video |
| `video_id` | STRING | Genişletilmiş video için benzersiz tanımlayıcı |
| `duration` | STRING | Genişletilmiş videonun süresi |