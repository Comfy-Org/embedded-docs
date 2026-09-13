# Flux.2 Görüntü

Flux.2 [pro] veya Flux.2 [max] modelini kullanarak bir metin isteminden ve isteğe bağlı referans görsellerden görsel üretin. Düğüm, isteği BFL API'sine gönderir, sonuç hazır olana kadar yoklar ve üretilen görseli döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak Flux.2 model sürümü. Bir model seçmek, genişlik, yükseklik ve isteğe bağlı referans görseller için ek parametrelerin kilidini açar. | DYNAMIC_COMBO | Evet | "Flux.2 [pro]"<br>"Flux.2 [max]" |
| `prompt` | Görsel üretimi veya düzenlemesi için istem (varsayılan: boş dize). | STRING | Evet | N/A |
| `seed` | Gürültüyü oluşturmak için kullanılan rastgele tohum (varsayılan: 0). Her çalıştırmadan sonra değeri rastgeleleştirmek için üretim sonrası kontrol seçeneğini destekler. | INT | Evet | 0 - 18446744073709551615 |

### Flux.2 [pro] ve Flux.2 [max] Girdileri

Her iki model tarafından paylaşılır — parametre kümeleri aynıdır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model.width` | Üretilen görselin piksel cinsinden genişliği (varsayılan: 1024). | INT | Evet | 256 - 2048 (adım 32) |
| `model.height` | Üretilen görselin piksel cinsinden yüksekliği (varsayılan: 768). | INT | Evet | 256 - 2048 (adım 32) |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model.images` | Görselden görsele üretim için isteğe bağlı referans görsel(ler). En fazla 8 görsel. Büyütülebilir yuva: 1..8 öğe bağlayın (`image_1`...`image_8`). | IMAGE | Hayır | 0 - 8 görsel |

**Not:**
- En fazla referans görsel sayısı 8'dir. 8'den fazla görsel sağlanırsa bir hata oluşur. Toplu görseller bu sınıra dahildir, çünkü bir toplu gruptaki her görsel ayrı ayrı sayılır.
- Referans görseller, API'ye gönderilmeden önce toplam piksel sayısı 2048 x 2048'i aşmayacak şekilde yeniden boyutlandırılır.
- `model.width` ve `model.height` değerleri üretim maliyetini etkiler. Maliyet ayrıca seçilen modele ve referans görsellerin sağlanıp sağlanmadığına bağlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | BFL API sonucundan indirilen, tensör biçimindeki üretilen görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `2994564757e1c66ac6da7b45d227b27ceb0020ac6fc9e8cbe2b53fe9f70bc195`
