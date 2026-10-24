# VEED Lipsync 2.0

VEED Lipsync ile bir videodaki konuşmacının ağzını yeni bir konuşma parçasına yeniden senkronize edin. Orijinal görüntüyü koruyarak bir klibi dublajlamak veya diyaloğunu değiştirmek için kullanın. Çıktı, videonun çözünürlüğünü 25 fps'te korur ve video başına bir konuşmacı olacak şekilde sesle aynı uzunluktadır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak model. Bir model seçmek, ona özgü parametreleri gösterir: `video`, `audio` ve `seed`. | DYNAMIC_COMBO | Evet | `"lipsync-2.0"` |
| `video` | Tek bir önden bakan konuşmacının görüntüsü. Sesten kısaysa, ses bitene kadar ileri ve geri oynatılır. | VIDEO | Evet | - |
| `audio` | Yeni konuşma, 600 saniyeye kadar. Video uzunluğunu belirler. | AUDIO | Evet | 600 saniyeye kadar |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 |

Konuşma parçası 600 saniyeden uzunsa veya VEED işi başarısız olursa düğüm hata vererek durur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `VIDEO` | Yeniden senkronize edilmiş video: ağzın yeni konuşmayla eşleştirildiği orijinal görüntü. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedLipsyncNode/tr.md)

---
**Source fingerprint (SHA-256):** `1a1e854b6923b5bad0fd6f3a79e76c70231dee31a12e9cf0b22be6bdcc741168`
