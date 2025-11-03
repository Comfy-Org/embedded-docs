> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduImageToVideoNode/tr.md)

Vidu Image To Video Generation düğümü, bir başlangıç görüntüsünden ve isteğe bağlı bir metin açıklamasından video oluşturur. Sağlanan görüntü karesinden genişleyen video içeriği üretmek için AI modellerini kullanır. Düğüm, görüntüyü ve parametreleri harici bir servise gönderir ve oluşturulan videoyu döndürür.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `vidu_q1`<br>*Diğer VideoModelName seçenekleri* | Model adı (varsayılan: vidu_q1) |
| `image` | IMAGE | Evet | - | Oluşturulan videonun başlangıç karesi olarak kullanılacak bir görüntü |
| `prompt` | STRING | Hayır | - | Video oluşturma için metinsel açıklama (varsayılan: boş) |
| `duration` | INT | Hayır | 5-5 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5, 5 saniyede sabit) |
| `seed` | INT | Hayır | 0-2147483647 | Video oluşturma için seed değeri (0 rastgele için) (varsayılan: 0) |
| `resolution` | COMBO | Hayır | `r_1080p`<br>*Diğer Resolution seçenekleri* | Desteklenen değerler modele ve süreye göre değişebilir (varsayılan: r_1080p) |
| `movement_amplitude` | COMBO | Hayır | `auto`<br>*Diğer MovementAmplitude seçenekleri* | Karedeki nesnelerin hareket genliği (varsayılan: auto) |

**Kısıtlamalar:**

- Yalnızca bir giriş görüntüsüne izin verilir (birden fazla görüntü işlenemez)
- Giriş görüntüsünün en-boy oranı 1:4 ile 4:1 arasında olmalıdır

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video çıktısı |