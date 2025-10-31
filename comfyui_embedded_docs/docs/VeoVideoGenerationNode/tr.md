> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeoVideoGenerationNode/tr.md)

Metin açıklamalarını kullanarak Google'ın Veo API'si aracılığıyla video oluşturur. Bu düğüm, metin açıklamalarından ve isteğe bağlı görüntü girdilerinden video oluşturabilir; en-boy oranı, süre ve daha fazlası gibi parametreler üzerinde kontrol sağlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Videoyu tanımlayan metin açıklaması (varsayılan: boş) |
| `en_boy_oranı` | COMBO | Evet | "16:9"<br>"9:16" | Çıktı videosunun en-boy oranı (varsayılan: "16:9") |
| `negatif_istem` | STRING | Hayır | - | Videoda nelerden kaçınılacağını yönlendirmek için kullanılan olumsuz metin istemi (varsayılan: boş) |
| `süre_saniye` | INT | Hayır | 5-8 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5) |
| `istemi_geliştir` | BOOLEAN | Hayır | - | İstemin AI yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: True) |
| `kişi_oluşturma` | COMBO | Hayır | "ALLOW"<br>"BLOCK" | Videoda insan oluşturulmasına izin verilip verilmeyeceği (varsayılan: "ALLOW") |
| `tohum` | INT | Hayır | 0-4294967295 | Video oluşturma için tohum değeri (0 rastgele için) (varsayılan: 0) |
| `görüntü` | IMAGE | Hayır | - | Video oluşturmayı yönlendirmek için isteğe bağlı referans görüntüsü |
| `model` | COMBO | Hayır | "veo-2.0-generate-001" | Video oluşturma için kullanılacak Veo 2 modeli (varsayılan: "veo-2.0-generate-001") |

**Not:** `generate_audio` parametresi yalnızca Veo 3.0 modelleri için kullanılabilir ve seçilen modele göre düğüm tarafından otomatik olarak işlenir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası |