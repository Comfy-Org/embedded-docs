# MinimaxHailuo03ContextIRNode

Bu düğüm, metin açıklamanızı ve eklenen medyayı analiz etmek için MiniMax H3 Context IR kullanır ve ardından daha güçlü, yapılandırılmış bir video promptu üretir. Döndürülen prompt, bir MiniMax H3 video düğümünün prompt girişine bağlanacak şekilde tasarlanmıştır; oraya medya eklerseniz, aynı medyayı aynı sırayla ekleyin, çünkü geliştirilmiş prompt medyaya konuma göre atıfta bulunur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Prompt geliştirme için kullanılacak model. | COMBO | Evet | `"MiniMax H3"` |
| `prompt` | Oluşturmayı düşündüğünüz videonun açıklaması. Boş olamaz. (varsayılan: `""`) | STRING | Evet | Herhangi bir metin |
| `duration` | Oluşturmayı düşündüğünüz videonun süresi, saniye cinsinden (4-15). (varsayılan: 5) | INT | Evet | 4 ila 15 |
| `ratio` | Oluşturmayı düşündüğünüz videonun en-boy oranı. `"adaptive"` en az bir görüntü, video veya ses girişi gerektirir. (varsayılan: `"adaptive"`) | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `reference_images` | Promptta bağlantı sırasıyla "Image 1".."Image 9" olarak atıfta bulunulan konu veya stil referans görüntüleri. En fazla 9 görüntü. | IMAGE | Hayır | 0 ila 9 görüntü |
| `reference_videos` | Promptta bağlantı sırasıyla "Video 1".."Video 3" olarak atıfta bulunulan hareket veya sahne referans videoları. En fazla 3 video, her biri 2-15 saniye, toplamda 15 saniye. | VIDEO | Hayır | 0 ila 3 video |
| `reference_audios` | Promptta bağlantı sırasıyla "Audio 1".."Audio 3" olarak atıfta bulunulan ses referansları. En fazla 3 klip, her biri 2-15 saniye, toplamda 15 saniye. Referans görüntü veya video olmadan kullanılamaz. | AUDIO | Hayır | 0 ila 3 klip |
| `first_frame` | Oluşturmayı düşündüğünüz videonun ilk karesi. Referans medyayla birleştirilemez. | IMAGE | Hayır | Tek görüntü |
| `last_frame` | Oluşturmayı düşündüğünüz videonun son karesi. Referans medyayla birleştirilemez. | IMAGE | Hayır | Tek görüntü |

### Parametre kısıtlamaları

- `prompt`, `duration`, `ratio`, `reference_images`, `reference_videos` ve `reference_audios` girişleri `model` seçenek grubunun parçasıdır.
- `first_frame` ve `last_frame` herhangi bir referans medyayla birleştirilemez.
- En az bir `reference_image` veya `reference_video` bağlanmadıkça `reference_audios` kullanılamaz.
- Hiçbir kare ve referans medya bağlanmadığında `ratio`, `"adaptive"` olarak ayarlanamaz.
- Referans videoların her biri yaklaşık 2-15 saniye olmalı ve toplam süre 15 saniyeyi geçmemelidir. Kare hızları 23,9 ile 60,5 FPS arasında olmalıdır.
- Referans seslerin her biri yaklaşık 2-15 saniye olmalı ve toplam süre 15 saniyeyi geçmemelidir.
- `first_frame`, `last_frame` ve her referans görüntü en az 256x256 piksel olmalı ve en-boy oranı 0,4 ile 2,5 arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `STRING` | MiniMax H3 Context IR tarafından oluşturulan geliştirilmiş, yapılandırılmış video promptu. Bir MiniMax H3 video oluşturma düğümünün prompt girişine bağlanabilir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ContextIRNode/tr.md)

---
**Source fingerprint (SHA-256):** `73015517f9c0f55f0aceeef935508a372e0d95668e4733d1c8100b53e4afa7e2`
