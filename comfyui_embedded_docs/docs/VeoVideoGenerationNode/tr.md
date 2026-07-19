# Google Veo2 Video Oluşturma

Google'ın Veo 2 API'sini kullanarak metin istemlerinden videolar oluşturur. Bu düğüm, metin açıklamalarından ve isteğe bağlı görsel girdilerinden, en boy oranı, süre ve daha fazlası gibi parametreler üzerinde kontrole sahip videolar oluşturabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | Videonun metin açıklaması (varsayılan: boş) | STRING | Evet | - |
| `en_boy_oranı` | Çıktı videosunun en boy oranı (varsayılan: "16:9") | COMBO | Evet | "16:9"<br>"9:16" |
| `negatif_istem` | Videoda nelerden kaçınılması gerektiğini belirten olumsuz metin istemi (varsayılan: boş) | STRING | Hayır | - |
| `süre_saniye` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5) | INT | Hayır | 5-8 |
| `istemi_geliştir` | İstemin yapay zeka yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: True). Bu gelişmiş bir parametredir. | BOOLEAN | Hayır | - |
| `kişi_oluşturma` | Videoda kişi oluşturmaya izin verilip verilmeyeceği (varsayılan: "ALLOW"). Bu gelişmiş bir parametredir. | COMBO | Hayır | "ALLOW"<br>"BLOCK" |
| `tohum` | Video oluşturma için tohum değeri (0 rastgele anlamına gelir) (varsayılan: 0). Bu gelişmiş bir parametredir. | INT | Hayır | 0-4294967295 |
| `görüntü` | Video oluşturmayı yönlendirmek için isteğe bağlı referans görseli | IMAGE | Hayır | - |
| `model` | Video oluşturma için kullanılacak Veo 2 modeli (varsayılan: "veo-2.0-generate-001") | COMBO | Hayır | "veo-2.0-generate-001" |

**Not:** `generate_audio` parametresi yalnızca Veo 3.0 modelleri için kullanılabilir ve seçilen modele göre düğüm tarafından otomatik olarak işlenir. Veo 3.0 modelleri kullanılırken `enhance_prompt` parametresi True olmaya zorlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeoVideoGenerationNode/tr.md)

---
**Source fingerprint (SHA-256):** `1a8b8ffe82fce32566815248f4a2434a1b865b5e5651935ccb3b92c7e38adee9`
