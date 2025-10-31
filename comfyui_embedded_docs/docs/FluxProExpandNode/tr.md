> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProExpandNode/tr.md)

Görüntüyü prompt'a dayalı olarak dış boyama yapar. Bu düğüm, bir görüntüyü üst, alt, sol ve sağ taraflarına pikseller ekleyerek genişletirken, sağlanan metin açıklamasıyla eşleşen yeni içerik oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Genişletilecek giriş görüntüsü |
| `prompt` | STRING | Hayır | - | Görüntü oluşturma için prompt (varsayılan: "") |
| `prompt_upsampling` | BOOLEAN | Hayır | - | Prompt üzerinde yukarı örnekleme yapılıp yapılmayacağı. Aktifse, prompt'u daha yaratıcı oluşturum için otomatik olarak değiştirir, ancak sonuçlar belirsizdir (aynı seed tam olarak aynı sonucu üretmez). (varsayılan: False) |
| `top` | INT | Hayır | 0-2048 | Görüntünün üst kısmında genişletilecek piksel sayısı (varsayılan: 0) |
| `bottom` | INT | Hayır | 0-2048 | Görüntünün alt kısmında genişletilecek piksel sayısı (varsayılan: 0) |
| `left` | INT | Hayır | 0-2048 | Görüntünün sol kısmında genişletilecek piksel sayısı (varsayılan: 0) |
| `right` | INT | Hayır | 0-2048 | Görüntünün sağ kısmında genişletilecek piksel sayısı (varsayılan: 0) |
| `guidance` | FLOAT | Hayır | 1.5-100 | Görüntü oluşturma süreci için kılavuzluk gücü (varsayılan: 60) |
| `steps` | INT | Hayır | 15-50 | Görüntü oluşturma süreci için adım sayısı (varsayılan: 50) |
| `seed` | INT | Hayır | 0-18446744073709551615 | Gürültü oluşturmak için kullanılan rastgele seed. (varsayılan: 0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Genişletilmiş çıktı görüntüsü |