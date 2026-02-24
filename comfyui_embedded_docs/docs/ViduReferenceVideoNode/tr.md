> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/tr.md)

Vidu Referans Video Düğümü, birden fazla referans görselinden ve bir metin isteminden videolar oluşturur. Sağlanan görseller ve açıklamaya dayalı olarak tutarlı video içeriği oluşturmak için AI modellerini kullanır. Düğüm, süre, en-boy oranı, çözünürlük ve hareket kontrolü dahil olmak üzere çeşitli video ayarlarını destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"vidu_q1"` | Video oluşturma için model adı (varsayılan: "vidu_q1") |
| `images` | IMAGE | Evet | - | Tutarlı özneler içeren bir video oluşturmak için referans olarak kullanılacak görseller (maksimum 7 görsel) |
| `prompt` | STRING | Evet | - | Video oluşturma için metinsel açıklama |
| `duration` | INT | Hayır | 5-5 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5) |
| `seed` | INT | Hayır | 0-2147483647 | Video oluşturma için tohum değeri (0 rastgele için) (varsayılan: 0) |
| `aspect_ratio` | COMBO | Hayır | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` | Çıktı videosunun en-boy oranı (varsayılan: "16:9") |
| `resolution` | COMBO | Hayır | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"1440p"`<br>`"2160p"` | Desteklenen değerler modele ve süreye göre değişiklik gösterebilir (varsayılan: "1080p") |
| `movement_amplitude` | COMBO | Hayır | `"auto"`<br>`"low"`<br>`"medium"`<br>`"high"` | Kare içindeki nesnelerin hareket genliği (varsayılan: "auto") |

**Kısıtlamalar ve Sınırlamalar:**

- `prompt` alanı zorunludur ve boş olamaz
- Referans için maksimum 7 görsele izin verilir
- Her görselin en-boy oranı 1:4 ile 4:1 arasında olmalıdır
- Her görselin minimum boyutları 128x128 piksel olmalıdır
- Süre 5 saniye olarak sabitlenmiştir

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Referans görselleri ve isteme dayalı olarak oluşturulan video |
