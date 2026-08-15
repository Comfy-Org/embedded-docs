# Vidu Çok Kareli Video Üretimi

Bu düğüm, birden çok ana kare arasında geçişler oluşturarak video üretir. Bir başlangıç görüntüsünden başlar ve kullanıcı tarafından tanımlanan bir dizi bitiş görüntüsü ve istemi aracılığıyla animasyon oluşturarak çıktı olarak tek bir video dosyası üretir.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video üretimi için kullanılacak Vidu modeli. | COMBO | Evet | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `start_image` | Başlangıç karesi görüntüsü. En boy oranı 1:4 ile 4:1 arasında olmalıdır. | IMAGE | Evet | En boy oranı 1:4 ila 4:1 |
| `seed` | Tekrarlanabilir sonuçlar elde etmek için rastgele sayı üretiminde kullanılan tohum değeri (varsayılan: 1). | INT | Evet | 0 ila 2147483647 |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `frames` | Ana kare geçiş sayısı (2-9). Bir değer seçmek, her kare için gereken girdileri dinamik olarak ortaya çıkarır. | DYNAMIC COMBO | Evet | `"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"` |

### Kare Girdileri (tüm kare sayısı seçeneklerinde ortak)

`frames` bir sayıya ayarlandığında, 1'den bu sayıya kadar her `i` karesi için aşağıdaki üç girdi gösterilir. Örneğin, `"3"` seçildiğinde `prompt1` / `end_image1` / `duration1`, `prompt2` / `end_image2` / `duration2` ve `prompt3` / `end_image3` / `duration3` eklenir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt{i}` | {i}. kare geçişi için metin istemi. Çok satırlı metin alanı. Maksimum 2000 karakter. | STRING | Evet | En fazla 2000 karakter |
| `end_image{i}` | {i}. bölüm için bitiş karesi görüntüsü. En boy oranı 1:4 ile 4:1 arasında olmalıdır. | IMAGE | Evet | En boy oranı 1:4 ila 4:1 |
| `duration{i}` | {i}. bölümün saniye cinsinden süresi. | INT | Evet | 2 ila 7 (varsayılan: 4) |

**Notlar:**

- Tüm girdiler zorunludur. `seed` varsayılan bir değere sahiptir ancak yine de zorunlu bir girdidir.
- `start_image` ve her `end_image{i}` 1:4 ile 4:1 arasında bir en boy oranına sahip olmalıdır.
- Her `prompt{i}` maksimum 2000 karakter uzunluğunda olmalıdır.
- Her `duration{i}` 2 ile 7 saniye arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Tüm animasyonlu geçişleri içeren oluşturulmuş video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `ad877532ba27444938b7b2e4634ac7f8a47db0f7fb53967d874ad38b44336dcf`
