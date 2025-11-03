> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/tr.md)

Google'un Veo 3 API'sini kullanarak metin istemlerinden video oluşturur. Bu düğüm, iki Veo 3 modelini destekler: veo-3.0-generate-001 ve veo-3.0-fast-generate-001. Ses oluşturma ve sabit 8 saniyelik süre gibi Veo 3'e özgü özelliklerle temel Veo düğümünü genişletir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Videoyu tanımlayan metin açıklaması (varsayılan: "") |
| `aspect_ratio` | COMBO | Evet | "16:9"<br>"9:16" | Çıktı videosunun en-boy oranı (varsayılan: "16:9") |
| `negative_prompt` | STRING | Hayır | - | Videoda nelerden kaçınılacağını yönlendirmek için kullanılan olumsuz metin istemi (varsayılan: "") |
| `duration_seconds` | INT | Hayır | 8-8 | Çıktı videosunun saniye cinsinden süresi (Veo 3 yalnızca 8 saniyeyi destekler) (varsayılan: 8) |
| `enhance_prompt` | BOOLEAN | Hayır | - | İstemin AI yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: True) |
| `person_generation` | COMBO | Hayır | "ALLOW"<br>"BLOCK" | Videoda insan oluşturulmasına izin verilip verilmeyeceği (varsayılan: "ALLOW") |
| `seed` | INT | Hayır | 0-4294967295 | Video oluşturma için tohum değeri (0 rastgele için) (varsayılan: 0) |
| `image` | IMAGE | Hayır | - | Video oluşturmayı yönlendirmek için isteğe bağlı referans görüntü |
| `model` | COMBO | Hayır | "veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" | Video oluşturma için kullanılacak Veo 3 modeli (varsayılan: "veo-3.0-generate-001") |
| `generate_audio` | BOOLEAN | Hayır | - | Video için ses oluştur. Tüm Veo 3 modelleri tarafından desteklenir. (varsayılan: False) |

**Not:** `duration_seconds` parametresi tüm Veo 3 modelleri için 8 saniyede sabitlenmiştir ve değiştirilemez.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası |