> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/tr.md)

Prompt ve output_size değerlerine dayalı olarak video oluşturur. Bu düğüm, PixVerse API'sini kullanarak iki giriş görüntüsü arasında geçiş videoları oluşturur ve video kalitesi, süresi, hareket stili ve oluşturma parametrelerini belirtmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `first_frame` | IMAGE | Evet | - | Video geçişi için başlangıç görüntüsü |
| `last_frame` | IMAGE | Evet | - | Video geçişi için bitiş görüntüsü |
| `prompt` | STRING | Evet | - | Video oluşturma için prompt (varsayılan: boş string) |
| `quality` | COMBO | Evet | PixVerseQuality enum'undan mevcut kalite seçenekleri<br>Varsayılan: res_540p | Video kalite ayarı |
| `duration_seconds` | COMBO | Evet | PixVerseDuration enum'undan mevcut süre seçenekleri | Video süresi saniye cinsinden |
| `motion_mode` | COMBO | Evet | PixVerseMotionMode enum'undan mevcut hareket modu seçenekleri | Geçiş için hareket stili |
| `seed` | INT | Evet | 0 ile 2147483647 arası | Video oluşturma için seed değeri (varsayılan: 0) |
| `negative_prompt` | STRING | Hayır | - | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş string) |

**Not:** 1080p kalite kullanıldığında, hareket modu otomatik olarak normal olarak ayarlanır ve süre 5 saniye ile sınırlandırılır. 5 saniye olmayan süreler için hareket modu da otomatik olarak normal olarak ayarlanır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan geçiş videosu |