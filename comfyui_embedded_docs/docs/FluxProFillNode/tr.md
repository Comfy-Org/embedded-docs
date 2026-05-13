> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/tr.md)

Görüntüyü maske ve istem doğrultusunda yeniden boyar. Bu düğüm, Flux.1 modelini kullanarak görüntünün maskelenmiş alanlarını sağlanan metin açıklamasına göre doldurur ve çevreleyen görüntüyle uyumlu yeni içerik oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Yeniden boyanacak giriş görüntüsü |
| `mask` | MASK | Evet | - | Görüntünün hangi alanlarının doldurulacağını tanımlayan maske |
| `prompt` | STRING | Hayır | - | Görüntü oluşturma için istem (varsayılan: boş dize) |
| `prompt_upsampling` | BOOLEAN | Hayır | - | İstem üzerinde yukarı örnekleme yapılıp yapılmayacağı. Etkinleştirilirse, daha yaratıcı üretim için istemi otomatik olarak değiştirir, ancak sonuçlar deterministik değildir (aynı tohum aynı sonucu üretmez). (varsayılan: false) |
| `guidance` | FLOAT | Hayır | 1,5-100 | Görüntü oluşturma süreci için rehberlik gücü (varsayılan: 60) |
| `steps` | INT | Hayır | 15-50 | Görüntü oluşturma süreci için adım sayısı (varsayılan: 50) |
| `seed` | INT | Hayır | 0-18446744073709551615 | Gürültü oluşturmak için kullanılan rastgele tohum. (varsayılan: 0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output_image` | IMAGE | Maskelenmiş alanların isteme göre doldurulduğu oluşturulan görüntü |

---
**Source fingerprint (SHA-256):** `ae2708d9e4b99ecb142fca0693c3973957c5677e8121eb5e34d30f872d7102c0`
