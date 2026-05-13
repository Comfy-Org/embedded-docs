> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageToVideoNode/tr.md)

Bir metin istemi ve isteğe bağlı başlangıç/bitiş görsellerine dayanarak eşzamanlı olarak videolar oluşturur. Bu düğüm, video içeriğini bir istem aracılığıyla tanımlamanıza ve isteğe bağlı olarak videonun yapısını kontrol etmek için ilk ve/veya son kareyi belirtmenize olanak tanıyan Luma API'sini kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `istem` | STRING | Evet | - | Video oluşturma için istem (varsayılan: "") |
| `model` | COMBO | Evet | Birden çok seçenek mevcut | Mevcut Luma modelleri arasından video oluşturma modelini seçer |
| `çözünürlük` | COMBO | Evet | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` | Oluşturulan video için çıktı çözünürlüğü (varsayılan: "540p"). Bu parametre `ray-1-6` modeli kullanılırken dikkate alınmaz. |
| `süre` | COMBO | Evet | `"5s"`<br>`"9s"` | Oluşturulan videonun süresi. Bu parametre `ray-1-6` modeli kullanılırken dikkate alınmaz. |
| `döngü` | BOOLEAN | Evet | - | Oluşturulan videonun döngüye girip girmeyeceği (varsayılan: False) |
| `tohum` | INT | Evet | 0 ile 18446744073709551615 arası | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir. (varsayılan: 0) |
| `ilk_görüntü` | IMAGE | Hayır | - | Oluşturulan videonun ilk karesi. (isteğe bağlı) |
| `son_görüntü` | IMAGE | Hayır | - | Oluşturulan videonun son karesi. (isteğe bağlı) |
| `luma_kavramları` | CUSTOM | Hayır | - | Luma Concepts düğümü aracılığıyla kamera hareketini belirlemek için isteğe bağlı Kamera Kavramları. (isteğe bağlı) |

**Not:** `first_image` veya `last_image` öğelerinden en az biri sağlanmalıdır. Her ikisi de eksikse düğüm bir istisna oluşturacaktır. `model` `ray-1-6` olarak ayarlandığında `resolution` ve `duration` parametreleri dikkate alınmaz.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | VIDEO | Oluşturulan video dosyası |

---
**Source fingerprint (SHA-256):** `210286ad38cecc5b3b0689f470ff473e996abfd251f88a45bcac936751ae2674`
