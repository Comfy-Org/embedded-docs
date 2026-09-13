# Vidu Q3 Başlangıç/Bitiş Kareden Videoya Oluşturma

Bu düğüm, bir başlangıç karesi ile bir bitiş karesi arasında geçiş oluşturarak ve bir metin istemi rehberliğinde video üretir. İki görüntü arasında interpolasyon yapmak için Vidu Q3 modelini kullanır ve seçilen süre ile çözünürlükte bir video üretir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video üretimi için kullanılacak model. Bir seçenek seçildiğinde `resolution`, `duration` ve `audio` için ek yapılandırma parametreleri görünür. | DYNAMIC_COMBO | Evet | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `ilk kare` | Video dizisinin başlangıç görüntüsü. | IMAGE | Evet | - |
| `bitiş karesi` | Video dizisinin bitiş görüntüsü. | IMAGE | Evet | - |
| `komut istemi` | İstem açıklaması (en fazla 2000 karakter). | STRING | Evet | En fazla 2000 karakter |
| `tohum` | Üretimin rastgeleliğini kontrol etmek için kullanılan seed değeri. Üretim sonrası kontrol seçeneği vardır (varsayılan: 1). | INT | Evet | 0 - 2147483647 |

### viduq3-pro ve viduq3-turbo Girdileri

Aşağıdaki parametreler her iki model seçeneği (`viduq3-pro` ve `viduq3-turbo`) tarafından paylaşılır. Bir model seçildikten sonra görünürler.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 1 - 16 |
| `audio` | Etkinleştirildiğinde, sesli video (diyalog ve ses efektleri dahil) üretir (varsayılan: False). | BOOLEAN | Evet | `True`<br>`False` |

**Not:** `first_frame` ve `end_frame` görüntüleri benzer en-boy oranlarına sahip olmalıdır. İki görüntünün en-boy oranı birbirinin %80 ila %125'i arasında kalmalıdır (0.8 ile 1.25 arasında göreli yakınlık).

**Not:** `viduq3-turbo` için fiyat 720p'de saniye başına 0.06 USD, 1080p'de saniye başına 0.08 USD'dir. `viduq3-pro` için fiyat 720p'de saniye başına 0.15 USD, 1080p'de saniye başına 0.16 USD'dir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `c917867c5a7b68a1286f445025070f9a55d8d10091d9562960e0428cbedf25e4`
