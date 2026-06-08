Görüntüyü maske ve istem doğrultusunda yeniden boyar. Bu düğüm, Flux.1 modelini kullanarak görüntünün maskelenmiş alanlarını sağlanan metin açıklamasına göre doldurur ve çevreleyen görüntüyle uyumlu yeni içerik oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Yeniden boyanacak giriş görüntüsü | IMAGE | Evet | - |
| `maske` | Görüntünün hangi alanlarının doldurulacağını tanımlayan maske | MASK | Evet | - |
| `istem` | Görüntü oluşturma için istem (varsayılan: boş dize) | STRING | Hayır | - |
| `istem_yükseltme` | İstem üzerinde yukarı örnekleme yapılıp yapılmayacağı. Etkinleştirilirse, daha yaratıcı üretim için istemi otomatik olarak değiştirir, ancak sonuçlar deterministik değildir (aynı tohum aynı sonucu üretmez). (varsayılan: false) | BOOLEAN | Hayır | - |
| `rehberlik` | Görüntü oluşturma süreci için rehberlik gücü (varsayılan: 60) | FLOAT | Hayır | 1,5-100 |
| `adımlar` | Görüntü oluşturma süreci için adım sayısı (varsayılan: 50) | INT | Hayır | 15-50 |
| `tohum` | Gürültü oluşturmak için kullanılan rastgele tohum. (varsayılan: 0) | INT | Hayır | 0-18446744073709551615 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output_image` | Maskelenmiş alanların isteme göre doldurulduğu oluşturulan görüntü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/tr.md)

---
**Source fingerprint (SHA-256):** `ae2708d9e4b99ecb142fca0693c3973957c5677e8121eb5e34d30f872d7102c0`
