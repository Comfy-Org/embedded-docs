> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageModifyNode/tr.md)

## Genel Bakış

Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageModifyNode/en.md)

Bir metin istemi ve orijinal görüntünün en-boy oranına göre görüntüleri eşzamanlı olarak değiştirir. Bu düğüm, bir giriş görüntüsünü alır ve sağlanan isteme göre dönüştürür; orijinal görüntünün ne kadar değiştirileceğini kontrol etmek için yapılandırılabilir bir görüntü ağırlığı kullanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Değiştirilecek giriş görüntüsü |
| `prompt` | STRING | Evet | - | Görüntü oluşturma için istem (varsayılan: "") |
| `image_weight` | FLOAT | Hayır | 0.0-0.98 | Görüntünün ağırlığı; 1.0'a yaklaştıkça görüntü daha az değiştirilir (varsayılan: 0.1). Dahili olarak bu değer tersine çevrilir (1.0 - image_weight) ve 0.0 ile 0.98 arasında sınırlandırılır. |
| `model` | STRING | Evet | `"photon-flash-1"`<br>`"photon-1"`<br>`"photon"` | Görüntü değiştirme için kullanılacak Luma modeli. Farklı modellerin farklı maliyetleri vardır. |
| `seed` | INT | Hayır | 0-18446744073709551615 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Luma modeli tarafından oluşturulan değiştirilmiş görüntü |

---
**Source fingerprint (SHA-256):** `078542bdba19945037c95fefa30d1b403ebf58e29270c8067dcb8ff21a99b7e0`
