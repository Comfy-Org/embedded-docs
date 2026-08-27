# Flux.2 Görüntü

Flux.2 Image

Flux.2 [pro] veya Flux.2 [max] modelini kullanarak bir metin isteminden ve isteğe bağlı referans görsellerinden görüntüler oluşturun. Bu düğüm isteğinizi BFL API'sine gönderir, sonucu yoklar ve oluşturulan görüntüyü bir tensor olarak döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak Flux.2 model sürümü. Bir model seçmek, genişlik, yükseklik ve isteğe bağlı referans görselleri için ek parametreleri etkinleştirir. | DYNAMIC_COMBO | Evet | "Flux.2 [pro]"<br>"Flux.2 [max]" |
| `istem` | Görüntü oluşturma veya düzenleme için istem (varsayılan: boş dize). | STRING | Evet | N/A |
| `tohum` | Gürültüyü oluşturmak için kullanılan rastgele tohum (seed). Her üretimden sonra rastgele olacak şekilde ayarlanabilir (varsayılan: 0). | INT | Evet | 0 ile 18446744073709551615 |

### Flux.2 [pro] ve Flux.2 [max] Girdileri

Her iki model tarafından paylaşılır — parametre setleri aynıdır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `genişlik` | Oluşturulan görüntünün piksel cinsinden genişliği (varsayılan: 1024). | INT | Evet | 256 ile 2048 (step 32) |
| `yükseklik` | Oluşturulan görüntünün piksel cinsinden yüksekliği (varsayılan: 768). | INT | Evet | 256 ile 2048 (step 32) |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model.images` | Görüntüden görüntüye üretim için isteğe bağlı referans görsel(ler)i. En fazla 8 görsel. Genişletilebilir yuva: 1..8 öğe bağlayın (`image_1`...`image_8`). | IMAGE | Hayır | 0 ile 8 images |

**Not:**
- Referans görsellerinin maksimum sayısı 8'dir. 8'den fazla görsel sağlanırsa bir hata oluşur.
- `model.width` ve `model.height` değerleri üretim maliyetini etkiler. Maliyet ayrıca seçilen modele ve referans görsellerinin sağlanıp sağlanmadığına bağlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | BFL API sonucundan indirilen, oluşturulan görüntü (tensor olarak). | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `2994564757e1c66ac6da7b45d227b27ceb0020ac6fc9e8cbe2b53fe9f70bc195`
