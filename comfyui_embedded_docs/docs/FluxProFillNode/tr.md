> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/tr.md)

Görüntüyü maske ve prompt temelinde boyar. Bu düğüm, Flux.1 modelini kullanarak bir görüntünün maskelenmiş alanlarını sağlanan metin açıklamasına göre doldurur ve çevreleyen görüntüyle eşleşen yeni içerik üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | - | Boyanacak giriş görüntüsü |
| `maske` | MASK | Evet | - | Görüntünün hangi alanlarının doldurulacağını tanımlayan maske |
| `istem` | STRING | Hayır | - | Görüntü oluşturma için prompt (varsayılan: boş string) |
| `istem_yükseltme` | BOOLEAN | Hayır | - | Prompt üzerinde yukarı örnekleme yapılıp yapılmayacağı. Aktifse, prompt'u daha yaratıcı oluşturum için otomatik olarak değiştirir, ancak sonuçlar belirsizdir (aynı seed tam olarak aynı sonucu üretmez). (varsayılan: false) |
| `rehberlik` | FLOAT | Hayır | 1.5-100 | Görüntü oluşturma süreci için kılavuzluk gücü (varsayılan: 60) |
| `adımlar` | INT | Hayır | 15-50 | Görüntü oluşturma süreci için adım sayısı (varsayılan: 50) |
| `tohum` | INT | Hayır | 0-18446744073709551615 | Gürültüyü oluşturmak için kullanılan rastgele seed. (varsayılan: 0) |

## Çıkışlar

| Çıkış Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `output_image` | IMAGE | Maskelenmiş alanları prompt'a göre doldurulmuş olarak oluşturulan görüntü |