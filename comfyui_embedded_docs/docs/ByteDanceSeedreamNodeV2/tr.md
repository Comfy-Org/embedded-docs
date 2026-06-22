# ByteDance Seedream 4.5 & 5.0

Bu düğüm, ByteDance'in Seedream modellerini (sürüm 4.0, 4.5 ve 5.0 Lite) kullanarak görseller oluşturur veya düzenler. Bir metin isteminden yeni görseller oluşturabilir veya referans görseller sağlayarak mevcut görselleri düzenleyebilir, 4K'ya kadar çözünürlükleri destekler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | Görsel oluşturma veya düzenleme için metin istemi. | STRING | Evet | Yok |
| `model` | Oluşturma için kullanılacak Seedream model sürümü. Her modelin farklı yetenekleri ve fiyatlandırması vardır. | COMBO | Evet | `"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` |
| `tohum` | Oluşturma için kullanılacak tohum değeri (varsayılan: 0). | INT | Hayır | 0 - 2147483647 |
| `filigran` | Görsele "AI tarafından oluşturuldu" filigranı eklenip eklenmeyeceği (varsayılan: False). | BOOLEAN | Hayır | True / False |

### Modele Özgü Parametreler

Bir model seçtiğinizde, ek parametreler kullanılabilir hale gelir:

- **Boyut Ön Ayarı**: Önceden tanımlanmış bir görsel çözünürlüğü seçmek için açılır menü (örneğin, "2048x2048", "1024x1024"). Kullanılabilir ön ayarlar seçilen modele bağlıdır.
- **Genişlik**: Oluşturulan görselin piksel cinsinden genişliği (varsayılan: 2048).
- **Yükseklik**: Oluşturulan görselin piksel cinsinden yüksekliği (varsayılan: 2048).
- **Maksimum Görsel**: Oluşturulacak maksimum görsel sayısı (varsayılan: 1). 1 olarak ayarlandığında, sıralı görsel oluşturma devre dışı bırakılır.
- **Referans Görseller**: Düzenleme için en fazla 10 (Seedream 4.0 ve 4.5 için) veya 14 (Seedream 5.0 Lite için) referans görsel. Görsellerin en-boy oranı 1:3 ile 3:1 arasında olmalıdır.
- **Kısmi Başarısızlıkta Hata Ver**: Etkinleştirilirse, istenen tüm görseller başarıyla oluşturulamazsa düğüm hata verecektir (varsayılan: False).

### Çözünürlük Kısıtlamaları

- **Seedream 5.0 Lite ve 4.5**: Minimum çözünürlük 3,68 megapikseldir (örneğin, 1920x1920).
- **Seedream 4.0**: Minimum çözünürlük 0,92 megapikseldir (örneğin, 960x960).
- **Tüm modeller**: Maksimum çözünürlük 16,78 megapikseldir (örneğin, 4096x4096).

### Görsel Sayısı Kısıtlamaları

- Referans görsellerin ve oluşturulan görsellerin toplam sayısı 15'i geçemez.
- Seedream 5.0 Lite için en fazla 14 referans görsel desteklenir.
- Seedream 4.0 ve 4.5 için en fazla 10 referans görsel desteklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Oluşturulan veya düzenlenen görsel, bir tensör olarak. Birden fazla görsel talep edildiyse, bunlar tek bir toplu iş halinde birleştirilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `1ceccfdb773807a993c32af22703da155367b67865338c78f153a8ccb02dcc8f`
