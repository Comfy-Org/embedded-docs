# Recraft V4 Metinden Vektöre

Recraft V4 Text to Vector düğümü, Recraft V4 ve V4.1 modellerini kullanarak bir metin açıklamasından Ölçeklenebilir Vektör Grafikleri (SVG) çizimleri üretir. İsteminize göre bir veya daha fazla SVG dosyası oluşturmak için Recraft API'sine bağlanır ve mevcut bir vektör stilini uygulayabilir veya referans görsellerden yeni bir stil oluşturabilir — referans görseller kullanıldığında, oluşturulan stil yeniden kullanım için `style_id` olarak döndürülür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Üretim için kullanılacak model. recraftv4_styles modelleri stile tutarlı üretim için tasarlanmıştır ve her zaman bir style_id veya style_references gerektirir. Bir model seçildiğinde kullanılabilir `size` seçenekleri değişir. | DYNAMIC_COMBO | Evet | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"`<br>`"recraftv4_styles_vector"`<br>`"recraftv4_styles_pro_vector"` |
| `prompt` | Görsel üretimi için istem. En fazla 10.000 karakter. | STRING | Evet | N/A |
| `negative_prompt` | Bu girdi yok sayılır: negatif istem, Recraft V4 ve V4.1 modelleri tarafından desteklenmez. | STRING | Evet | N/A |
| `n` | Üretilecek görsel sayısı (varsayılan: 1). | INT | Evet | 1 - 6 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirlemek için tohum; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 - 18446744073709551615 |
| `recraft_controls` | Recraft Controls düğümü aracılığıyla üretim üzerinde isteğe bağlı ek kontroller. | CUSTOM | Hayır | N/A |
| `style_id` | Uygulanacak bir Recraft V4 vektör stilinin UUID'si; örneğin Recraft V4 Create Style düğümünden veya önceki bir çalıştırmanın style_id çıktısından. style_references ile birlikte kullanılamaz. | STRING | Hayır | N/A |
| `style_match` | Stile ne kadar yakından uyulacağı: precise, stili ayrıntılı olarak yeniden üretir; flexible, genel görünümü eşleştirir. Yalnızca bir stil sağlandığında kullanılır (varsayılan: "precise"). | COMBO | Hayır | `"precise"`<br>`"flexible"` |

### recraftv4_1_vector, recraftv4_1_utility_vector, recraftv4 ve recraftv4_styles_vector Girdileri

Bu modeller aynı `size` seçeneklerini paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Üretilen görselin boyutu. Varsayılan: `"1024x1024"`. | COMBO | Evet | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### recraftv4_1_pro_vector, recraftv4_1_utility_pro_vector, recraftv4_pro ve recraftv4_styles_pro_vector Girdileri

Bu modeller aynı `size` seçeneklerini paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Üretilen görselin boyutu. Varsayılan: `"2048x2048"`. | COMBO | Evet | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `style_references` | Anında bir vektör stili oluşturmak için referans görseller; üretime ek olarak faturalandırılır. Oluşturulan stil, yeniden kullanım için style_id olarak döndürülür. style_id ile birlikte kullanılamaz. | IMAGE | Hayır | Genişletilebilir yuva: 1..N referans görseli bağlayın (düğümün maksimumuna kadar) |

**Not:** `size` parametresi, kullanılabilir seçenekleri seçilen `model`e göre değişen dinamik bir girdidir. `seed` değeri, harici API'den tekrarlanabilir sonuçlar alınacağını garanti etmez. `recraftv4_styles_vector` ve `recraftv4_styles_pro_vector` modelleri her zaman bir stil gerektirir: bir `style_id` sağlayın veya en az bir `style_references` görseli bağlayın. `style_id` ve `style_references` birlikte kullanılamaz — her ikisinin de sağlanması hataya neden olur ve `style_id` geçerli bir UUID olmalıdır. Stil referans görsellerinin sayısı sınırlıdır ve toplam kodlanmış boyutları 10 MB'ı aşmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Üretilen Ölçeklenebilir Vektör Grafikleri (SVG) görseli/görselleri. | SVG |
| `style_id` | Recraft API tarafından döndürülen stil UUID'si. Referans görseller sağlandığında, oluşturulan stil yeniden kullanım için burada döndürülür; aksi halde boş bir dize. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/tr.md)

---
**Source fingerprint (SHA-256):** `182a40b206b164cf2e96c7344d23e4906b7d61b90e3000743a3fd31941e08539`
