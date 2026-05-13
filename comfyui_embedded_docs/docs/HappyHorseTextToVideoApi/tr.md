> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/tr.md)

## Genel Bakış

HappyHorse modelini kullanarak bir metin istemine dayalı video oluşturur. Bu düğüm, isteminizi ve ayarlarınızı HappyHorse API'sine gönderir, videonun oluşturulmasını bekler ve ardından sonucu indirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | DICT | Evet | Açıklamaya Bakın | Model seçimini ve ilişkili parametrelerini içeren bir sözlük. Model `"happyhorse-1.0-t2v"` olmalıdır. Bu sözlük aşağıdaki alt parametreleri içerir:<br><br>**`prompt`** (STRING): Oluşturmak istediğiniz videonun metin açıklaması. İngilizce ve Çinceyi destekler. (varsayılan: "").<br>**`resolution`** (COMBO): Çıktı videosunun çözünürlüğü. Seçenekler: `"720P"`, `"1080P"`.<br>**`ratio`** (COMBO): Çıktı videosunun en-boy oranı. Seçenekler: `"16:9"`, `"9:16"`, `"1:1"`, `"4:3"`, `"3:4"`.<br>**`duration`** (INT): Videonun saniye cinsinden uzunluğu. (varsayılan: 5, min: 3, maks: 15, adım: 1). |
| `seed` | INT | Evet | 0 ile 2147483647 arası | Oluşturma için kullanılacak tohum değeri. Aynı girdilerle aynı tohum değerini kullanmak aynı sonucu üretecektir. (varsayılan: 0). |
| `watermark` | BOOLEAN | Hayır | True / False | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği. (varsayılan: False). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `VIDEO` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `8c6a7c0c2b10bbc65ca54abc991e1f12e8846b31701ed65b49c5d71f1b2a63ec`
