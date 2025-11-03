> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/tr.md)

OpenAIVideoSora2 düğümü, OpenAI'nin Sora modellerini kullanarak video oluşturur. Metin istemlerine ve isteğe bağlı giriş görüntülerine dayalı olarak video içeriği oluşturur ve ardından oluşturulan video çıktısını döndürür. Düğüm, seçilen modele bağlı olarak farklı video süreleri ve çözünürlükleri destekler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | "sora-2"<br>"sora-2-pro" | Video oluşturma için kullanılacak OpenAI Sora modeli (varsayılan: "sora-2") |
| `prompt` | STRING | Evet | - | Yönlendirici metin; bir giriş görüntüsü mevcutsa boş olabilir (varsayılan: boş) |
| `size` | COMBO | Evet | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" | Oluşturulan video için çözünürlük (varsayılan: "1280x720") |
| `duration` | COMBO | Evet | 4<br>8<br>12 | Oluşturulan videonun saniye cinsinden süresi (varsayılan: 8) |
| `image` | IMAGE | Hayır | - | Video oluşturma için isteğe bağlı giriş görüntüsü |
| `seed` | INT | Hayır | 0 ile 2147483647 arası | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirlemek için kullanılan seed; gerçek sonuçlar seed değerinden bağımsız olarak belirsizdir (varsayılan: 0) |

**Kısıtlamalar ve Sınırlamalar:**

- "sora-2" modeli yalnızca "720x1280" ve "1280x720" çözünürlüklerini destekler
- image parametresi kullanılırken yalnızca bir giriş görüntüsü desteklenir
- Sonuçlar seed değerinden bağımsız olarak belirsizdir

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video çıktısı |