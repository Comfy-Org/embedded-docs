# LumaRay32TextToVideoNode

Bu düğüm, Luma'nın Ray 3.2 modelini kullanarak bir metin isteminden video oluşturur. İsteminizi ve video ayarlarınızı Luma API'sine gönderir ve oluşturulan videoyu bir oluşturma kimliğiyle birlikte döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `prompt` | Video oluşturma için metin istemi. | STRING | Evet | 1-6000 karakter |
| `en-boy oranı` | Oluşturulan videonun en-boy oranı. | STRING | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"` |
| `çözünürlük` | Videonun çıktı çözünürlüğü (varsayılan: "720p"). | STRING | Evet | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `süre` | Oluşturulan videonun süresi. | STRING | Evet | `"5s"`<br>`"10s"` |
| `döngü` | Videonun kesintisiz döngüye girmesini sağlar. Yalnızca 5 saniyelik süre ile kullanılabilir. | BOOLEAN | Hayır | Doğru/Yanlış (varsayılan: Yanlış) |
| `seed` | Tekrarlanabilir oluşturma için tohum değeri. | INT | Hayır | 0 ile 2147483647 arası |

**Not:** `loop` parametresi yalnızca `duration` "5s" olarak ayarlandığında etkinleştirilebilir. "10s" süresi seçip döngüyü etkinleştirirseniz, düğüm bir hata döndürecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `oluşturma_id` | Oluşturulan video dosyası. | VIDEO |
| `generation_id` | Video oluşturma isteği için benzersiz tanımlayıcı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `04358a872530e5a2622bf0f148a694f2c707ce8535586d8f860bdf9911e1fa6a`
