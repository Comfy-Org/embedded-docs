# LumaRay32ImageToVideoNode

Luma'nın Ray 3.2 modelini kullanarak bir başlangıç ve/veya bitiş karesinden video oluşturun. Görüntü sabitlemeli üretimler her zaman 5 saniye sürelidir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|--------|
| `prompt` | Video oluşturma için metin istemi. | STRING | Evet | 1 ila 6000 karakter |
| `resolution` | Oluşturulan videonun çıktı çözünürlüğü (varsayılan: "720p"). | COMBO | Evet | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `loop` | Videonun kesintisiz döngüye girmesini sağlayın. Bir `end_frame` ayarlandığında kullanılamaz. | BOOLEAN | Evet | True<br>False |
| `seed` | Tekrarlanabilir oluşturma için tohum değeri. | INT | Evet | 0 ila 2147483647 |
| `start_frame` | Oluşturulan videonun ilk karesi. | IMAGE | Hayır | - |
| `end_frame` | Oluşturulan videonun son karesi. | IMAGE | Hayır | - |

**Not:** `start_frame` veya `end_frame` öğelerinden en az biri sağlanmalıdır. Her ikisi de sağlanırsa, oluşturulan video başlangıç karesinden bitiş karesine geçiş yapacaktır. Bir `end_frame` ayarlandığında `loop` seçeneği etkinleştirilemez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video çıktısı. | VIDEO |
| `generation_id` | Oluşturma isteği için benzersiz tanımlayıcı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `ff479c196f10153ffa09af6acfb4e286d1934aa28a5e9b413613097a2cfb5f2a`
