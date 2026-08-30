# Recraft V4 Metinden Görsele

Recraft V4 Metinden Görüntüye

Bu düğüm, Recraft V4 ve V4.1 yapay zeka modellerini kullanarak metin açıklamalarından görseller üretir. İsteminizi harici bir API'ye gönderir ve üretilen görselleri döndürür. Çıktıyı; modeli, görsel boyutunu, görsel sayısını ve isteğe bağlı bir stili (kaydedilmiş bir stil kimliği veya referans görselleri aracılığıyla) belirterek kontrol edebilirsiniz.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Üretim için kullanılacak model. recraftv4_styles modelleri, stil tutarlı üretim için tasarlanmıştır ve her zaman bir style_id veya style_references gerektirir. | DYNAMIC_COMBO | Evet | "recraftv4_1"<br>"recraftv4_1_utility"<br>"recraftv4_1_pro"<br>"recraftv4_1_utility_pro"<br>"recraftv4"<br>"recraftv4_pro"<br>"recraftv4_styles"<br>"recraftv4_styles_pro" |
| `prompt` | Görsel üretimi için istem (prompt). En fazla 10.000 karakter. | STRING | Evet | 1 ile 10000 karakter arası |
| `negative_prompt` | Bu girdi yok sayılır: Recraft V4 ve V4.1 modelleri negatif istemi (negative prompt) desteklemez. | STRING | Evet | Uygulanamaz |
| `n` | Üretilecek görsel sayısı (varsayılan: 1). | INT | Evet | 1 ile 6 arası |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen seed değeri; gerçek sonuçlar seed değerinden bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 ile 18446744073709551615 arası |
| `recraft_controls` | Recraft Controls düğümü aracılığıyla üretim üzerinde isteğe bağlı ek kontroller. | CUSTOM | Hayır | Uygulanamaz |
| `style_id` | Uygulanacak Recraft V4 stilinin UUID değeri; örn. Recraft V4 Create Style düğümünden veya önceki bir çalıştırmanın style_id çıktısından alınır. style_references ile birlikte kullanılamaz (varsayılan: boş). | STRING | Hayır | Geçerli UUID dizesi |
| `style_match` | Stilin ne kadar yakından takip edileceği: precise (kesin) seçeneği stili ayrıntılı olarak birebir üretir, flexible (esnek) seçeneği genel görünümü eşleştirir. Yalnızca bir stil sağlandığında kullanılır (varsayılan: "precise"). | COMBO | Hayır | "precise"<br>"flexible" |

### recraftv4_1, recraftv4_1_utility, recraftv4 ve recraftv4_styles Girdileri

Bu modeller aynı `size` parametresini paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Üretilen görselin boyutu (varsayılan: "1024x1024"). | COMBO | Evet | Birden fazla seçenek mevcuttur (standart Recraft V4 boyutları, "1024x1024" dahil). |

### recraftv4_1_pro, recraftv4_1_utility_pro, recraftv4_pro ve recraftv4_styles_pro Girdileri

Bu modeller aynı `size` parametresini paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Üretilen görselin boyutu (varsayılan: "2048x2048"). | COMBO | Evet | Birden fazla seçenek mevcuttur (pro Recraft V4 boyutları, "2048x2048" dahil). |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `style_references` | Anında bir stil oluşturmak için kullanılan referans görselleri; üretim ücretine ek olarak faturalandırılır. Oluşturulan stil, yeniden kullanım için style_id olarak döndürülür. style_id ile birlikte kullanılamaz. Genişletilebilir yuva: 1..N görsel bağlayın (style_reference_1, style_reference_2, ...). | IMAGE | Hayır | 0 ile Recraft API tarafından izin verilen maksimum referans görseli sayısı arasında; toplam kodlanmış boyut 10 MB'ı aşmamalıdır. |

**Not:** `size` parametresi dinamik bir girdidir; kullanılabilir seçenekler seçili `model`'e göre değişir. `recraftv4_styles` ve `recraftv4_styles_pro` modelleri her zaman bir stil gerektirir: stil referans görselleri bağlayın veya bir `style_id` sağlayın. `style_id` ve `style_references` girdileri birbirini dışlar; yalnızca birini sağlayın. Bir `style_id` geçerli bir UUID olmalıdır. `style_match` girdisi yalnızca bir stil sağlandığında kullanılır. Stil referans görselleri, üretim ücretine ek olarak faturalandırılır ve toplam kodlanmış boyutları 10 MB'ı aşmamalıdır. `seed` değeri, tekrarlanabilir görsel çıktıları garanti etmez. Infinite Style Library'den bir stil kimliği kullanıyorsanız, bunun bir Vector art stili olmadığından emin olun; aksi takdirde görsel yerine SVG verisi dönebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Üretilen görsel veya görsel grubu. | IMAGE |
| `style_id` | Bu üretimde kullanılan veya oluşturulan stil kimliği. Stil referans görselleri sağlandığında, oluşturulan stil yeniden kullanım için burada döndürülür; hiçbir stil kullanılmadığında boş dize. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `af5c1f68e59ca282cdca7c32cd50f0438b743fdda27d9d22e59b2d1343f45e26`
