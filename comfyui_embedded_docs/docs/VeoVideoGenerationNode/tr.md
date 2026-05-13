> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeoVideoGenerationNode/tr.md)

Google'ın Veo 2 API'sini kullanarak metin istemlerinden videolar oluşturur. Bu düğüm, metin açıklamalarından ve isteğe bağlı görsel girdilerinden, en boy oranı, süre ve daha fazlası gibi parametreler üzerinde kontrole sahip videolar oluşturabilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Videonun metin açıklaması (varsayılan: boş) |
| `aspect_ratio` | COMBO | Evet | "16:9"<br>"9:16" | Çıktı videosunun en boy oranı (varsayılan: "16:9") |
| `negative_prompt` | STRING | Hayır | - | Videoda nelerden kaçınılması gerektiğini belirten olumsuz metin istemi (varsayılan: boş) |
| `duration_seconds` | INT | Hayır | 5-8 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5) |
| `enhance_prompt` | BOOLEAN | Hayır | - | İstemin yapay zeka yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: True). Bu gelişmiş bir parametredir. |
| `person_generation` | COMBO | Hayır | "ALLOW"<br>"BLOCK" | Videoda kişi oluşturmaya izin verilip verilmeyeceği (varsayılan: "ALLOW"). Bu gelişmiş bir parametredir. |
| `seed` | INT | Hayır | 0-4294967295 | Video oluşturma için tohum değeri (0 rastgele anlamına gelir) (varsayılan: 0). Bu gelişmiş bir parametredir. |
| `image` | IMAGE | Hayır | - | Video oluşturmayı yönlendirmek için isteğe bağlı referans görseli |
| `model` | COMBO | Hayır | "veo-2.0-generate-001" | Video oluşturma için kullanılacak Veo 2 modeli (varsayılan: "veo-2.0-generate-001") |

**Not:** `generate_audio` parametresi yalnızca Veo 3.0 modelleri için kullanılabilir ve seçilen modele göre düğüm tarafından otomatik olarak işlenir. Veo 3.0 modelleri kullanılırken `enhance_prompt` parametresi True olmaya zorlanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası |

---
**Source fingerprint (SHA-256):** `1a8b8ffe82fce32566815248f4a2434a1b865b5e5651935ccb3b92c7e38adee9`
