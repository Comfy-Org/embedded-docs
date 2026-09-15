# Recraft V4 Metinden Görsele

Recraft V4 ve V4.1 modellerini kullanarak metin istemlerinden görüntüler üretir. İstem ve seçilen ayarları Recraft API'sine gönderir ve üretilen görüntüyü veya görüntüleri döndürür. Stil referans görüntüleri kullanılırsa, oluşturulan stil kimliği de döndürülür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Üretim için kullanılacak model. recraftv4_styles modelleri stil tutarlı üretim için tasarlanmıştır ve her zaman bir style_id veya style_references gerektirir. | DYNAMIC_COMBO | Evet | "recraftv4_1"<br>"recraftv4_1_utility"<br>"recraftv4_1_pro"<br>"recraftv4_1_utility_pro"<br>"recraftv4"<br>"recraftv4_pro"<br>"recraftv4_styles"<br>"recraftv4_styles_pro" |
| `prompt` | Görüntü üretimi için istem. En fazla 10.000 karakter. | STRING | Evet | 1 - 10000 karakter |
| `negative_prompt` | Bu girdi yok sayılır: negatif istem, Recraft V4 ve V4.1 modelleri tarafından desteklenmez. | STRING | Evet | N/A |
| `n` | Üretilecek görüntü sayısı (varsayılan: 1). | INT | Evet | 1 - 6 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 - 18446744073709551615 |
| `recraft_controls` | Recraft Controls düğümü aracılığıyla üretim üzerinde isteğe bağlı ek kontroller. | CUSTOM | Hayır | N/A |
| `style_id` | Uygulanacak bir Recraft V4 stilinin UUID'si; örn. Recraft V4 Create Style düğümünden veya önceki bir çalıştırmanın style_id çıktısından alınabilir. style_references ile birlikte kullanılamaz (varsayılan: boş). | STRING | Hayır | Geçerli UUID dizesi |
| `style_match` | Stilin ne kadar yakından izleneceği: precise stili ayrıntılı olarak yeniden üretir, flexible genel görünümü eşleştirir. Yalnızca bir stil sağlandığında kullanılır (varsayılan: "precise"). | COMBO | Hayır | "precise"<br>"flexible" |

### recraftv4_1, recraftv4_1_utility, recraftv4 ve recraftv4_styles Girdileri

Bu modeller aynı `size` parametresini paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Üretilen görüntünün boyutu (varsayılan: "1024x1024"). | COMBO | Evet | Kullanılabilir birden çok seçenek (standart Recraft V4 boyutları; "1024x1024" içerir) |

### recraftv4_1_pro, recraftv4_1_utility_pro, recraftv4_pro ve recraftv4_styles_pro Girdileri

Bu modeller aynı `size` parametresini paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Üretilen görüntünün boyutu (varsayılan: "2048x2048"). | COMBO | Evet | Kullanılabilir birden çok seçenek (pro Recraft V4 boyutları; "2048x2048" içerir) |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `style_references` | Anında stil oluşturmak için referans görüntüler; üretime ek olarak faturalandırılır. Oluşturulan stil, yeniden kullanım için style_id olarak döndürülür. style_id ile birlikte kullanılamaz. Genişletilebilir yuva: 1..N görüntü bağlayın (style_reference_1, style_reference_2, ...). | IMAGE | Hayır | 0 - Recraft API'sinin izin verdiği maksimum referans görüntü sayısı; toplam kodlanmış boyut 10 MB'ı aşmamalıdır |

**Not:** `size` parametresi, kullanılabilir seçenekleri seçilen `model`e göre değişen dinamik bir girdidir. `recraftv4_styles` ve `recraftv4_styles_pro` modelleri her zaman bir stil gerektirir: stil referans görüntülerini bağlayın veya bir `style_id` sağlayın. `style_id` ve `style_references` girdileri birbirini dışlar — yalnızca birini sağlayın. Bir `style_id` geçerli bir UUID olmalıdır. `style_match` girdisi yalnızca bir stil sağlandığında kullanılır. Stil referans görüntüleri üretime ek olarak faturalandırılır ve toplam kodlanmış boyutları 10 MB'ı aşmamalıdır. `seed` değeri, yeniden üretilebilir görüntü çıktılarını garanti etmez. Infinite Style Library'den bir stil kimliği kullanırsanız, bunun bir Vector art stili olmadığından emin olun; çünkü bu, görüntü yerine SVG verisi döndürebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Üretilen görüntü veya görüntü grubu. | IMAGE |
| `style_id` | Bu üretim tarafından kullanılan veya oluşturulan stil kimliği. Stil referans görüntüleri sağlandığında, oluşturulan stil yeniden kullanım için burada döndürülür; hiçbir stil kullanılmadığında boş dize. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `af5c1f68e59ca282cdca7c32cd50f0438b743fdda27d9d22e59b2d1343f45e26`
