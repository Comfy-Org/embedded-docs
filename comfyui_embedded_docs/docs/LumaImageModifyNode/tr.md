## Genel Bakış

Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageModifyNode/en.md)

Bir metin istemi ve orijinal görüntünün en-boy oranına göre görüntüleri eşzamanlı olarak değiştirir. Bu düğüm, bir giriş görüntüsünü alır ve sağlanan isteme göre dönüştürür; orijinal görüntünün ne kadar değiştirileceğini kontrol etmek için yapılandırılabilir bir görüntü ağırlığı kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Değiştirilecek giriş görüntüsü | IMAGE | Evet | - |
| `istem` | Görüntü oluşturma için istem (varsayılan: "") | STRING | Evet | - |
| `görüntü_ağırlığı` | Görüntünün ağırlığı; 1.0'a yaklaştıkça görüntü daha az değiştirilir (varsayılan: 0.1). Dahili olarak bu değer tersine çevrilir (1.0 - image_weight) ve 0.0 ile 0.98 arasında sınırlandırılır. | FLOAT | Hayır | 0.0-0.98 |
| `model` | Görüntü değiştirme için kullanılacak Luma modeli. Farklı modellerin farklı maliyetleri vardır. | STRING | Evet | `"photon-flash-1"`<br>`"photon-1"`<br>`"photon"` |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Hayır | 0-18446744073709551615 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Luma modeli tarafından oluşturulan değiştirilmiş görüntü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageModifyNode/tr.md)

---
**Source fingerprint (SHA-256):** `078542bdba19945037c95fefa30d1b403ebf58e29270c8067dcb8ff21a99b7e0`
