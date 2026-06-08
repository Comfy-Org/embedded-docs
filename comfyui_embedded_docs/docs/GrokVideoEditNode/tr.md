Bu düğüm, mevcut bir videoyu metin istemine göre düzenlemek için Grok API'sini kullanır. Videonuzu yükler, yapay zeka modeline açıklamanıza göre videoyu değiştirmesi için bir istek gönderir ve yeni oluşturulan videoyu döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video düzenleme için kullanılacak yapay zeka modeli (varsayılan: `"grok-imagine-video"`). | COMBO | Evet | `"grok-imagine-video"`<br>`"grok-imagine-video-beta"` |
| `istem` | İstenen videonun metin açıklaması. | STRING | Evet | Yok |
| `video` | Düzenlenecek giriş videosu. Desteklenen maksimum süre 8,7 saniye ve dosya boyutu 50MB'dır. | VIDEO | Evet | Yok |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen bir tohum değeri. Tohum değerinden bağımsız olarak gerçek sonuçlar deterministik değildir (varsayılan: 0). | INT | Hayır | 0 ile 2147483647 arası |

**Kısıtlamalar:**

* Giriş `video` süresi 1 ila 8,7 saniye arasında olmalıdır.
* Giriş `video` dosya boyutu 50MB'ı geçmemelidir.
* `prompt` boş olmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Yapay zeka modeli tarafından oluşturulan düzenlenmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `dfe52a089f7bfe7abc7f40ef113c44aef2dded828221d9d1acf0ddb6a167c33f`
