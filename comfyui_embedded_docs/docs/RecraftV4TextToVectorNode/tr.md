# Recraft V4 Metinden Vektöre

Recraft V4 Text to Vector düğümü, Recraft V4 ve V4.1 modellerini kullanarak bir metin açıklamasından Ölçeklenebilir Vektör Grafikleri (SVG) illüstrasyonları üretir. Recraft API'sine bağlanarak promptunuza göre bir veya daha fazla SVG dosyası oluşturur; mevcut bir vektör stilini uygulayabilir veya referans görüntülerden yeni bir stil oluşturabilir — referans görüntüler kullanıldığında, oluşturulan stil yeniden kullanılmak üzere bir `style_id` olarak döndürülür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Üretim için kullanılacak model. recraftv4_styles modelleri stil tutarlılığı sağlayan üretim için tasarlanmıştır ve her zaman bir style_id veya style_references gerektirir. Bir model seçmek, kullanılabilir `size` seçeneklerini değiştirir. | DYNAMIC_COMBO | Evet | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"`<br>`"recraftv4_styles_vector"`<br>`"recraftv4_styles_pro_vector"` |
| `prompt` | Görüntü üretimi için prompt. En fazla 10.000 karakter. | STRING | Evet | N/A |
| `negative_prompt` | Bu girdi yok sayılır: negative prompt, Recraft V4 ve V4.1 modelleri tarafından desteklenmez. | STRING | Evet | N/A |
| `n` | Oluşturulacak görüntü sayısı (varsayılan: 1). | INT | Evet | 1 ila 6 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar seed değerinden bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 ila 18446744073709551615 |
| `recraft_controls` | Recraft Controls düğümü aracılığıyla üretim üzerinde isteğe bağlı ek kontroller. | CUSTOM | Hayır | N/A |
| `style_id` | Uygulanacak bir Recraft V4 vektör stilinin UUID değeri; örn. Recraft V4 Create Style düğümünden veya önceki bir çalıştırmanın style_id çıktısından alınabilir. style_references ile birlikte kullanılamaz. | STRING | Hayır | N/A |
| `style_match` | Stilin ne kadar yakından takip edileceği: precise stili ayrıntılarıyla birebir kopyalar, flexible genel görünümü eşleştirir. Yalnızca bir stil sağlandığında kullanılır (varsayılan: "precise"). | COMBO | Hayır | `"precise"`<br>`"flexible"` |

### recraftv4_1_vector, recraftv4_1_utility_vector, recraftv4 ve recraftv4_styles_vector Girdileri

Bu modeller aynı `size` seçeneklerini paylaşır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Oluşturulan görüntünün boyutu. Varsayılan: `"1024x1024"`. | COMBO | Evet | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### recraftv4_1_pro_vector, recraftv4_1_utility_pro_vector, recraftv4_pro ve recraftv4_styles_pro_vector Girdileri

Bu modeller aynı `size` seçeneklerini paylaşır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Oluşturulan görüntünün boyutu. Varsayılan: `"2048x2048"`. | COMBO | Evet | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `style_references` | Anında bir vektör stili oluşturmak için kullanılan referans görüntüler; bu işlem üretim ücretine ek olarak faturalandırılır. Oluşturulan stil, yeniden kullanım için style_id olarak döndürülür. style_id ile birlikte kullanılamaz. | IMAGE | Hayır | Genişletilebilir yuva: 1..N referans görüntüsü bağlayın (düğümün maksimumuna kadar) |

**Not:** `size` parametresi, seçilen `model`e bağlı olarak kullanılabilir seçenekleri değişen dinamik bir girdidir. `seed` değeri, harici API'den tekrarlanabilir sonuçlar garanti etmez. `recraftv4_styles_vector` ve `recraftv4_styles_pro_vector` modelleri her zaman bir stil gerektirir: bir `style_id` sağlayın veya en az bir `style_references` görüntüsü bağlayın. `style_id` ve `style_references` birlikte kullanılamaz — ikisinin birden sağlanması hata oluşturur ve `style_id` geçerli bir UUID olmalıdır. Referans görüntülerin sayısı sınırlıdır ve toplam kodlanmış boyutları 10 MB'ı aşmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan Ölçeklenebilir Vektör Grafikleri (SVG) görüntüleri. | SVG |
| `style_id` | Recraft API tarafından döndürülen stil UUID değeri. Referans görüntüler sağlandığında, oluşturulan stil yeniden kullanım için burada döndürülür; aksi takdirde boş dizedir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/tr.md)

---
**Source fingerprint (SHA-256):** `182a40b206b164cf2e96c7344d23e4906b7d61b90e3000743a3fd31941e08539`
