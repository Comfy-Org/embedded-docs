> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProImageNode/tr.md)

Görüntüleri eşzamanlı olarak prompt ve çözünürlük temelinde oluşturur. Bu düğüm, Flux 1.1 Pro modelini kullanarak API uç noktasına istek gönderip tam yanıtı bekleyerek oluşturulan görüntüyü döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Görüntü oluşturma için prompt (varsayılan: boş string) |
| `prompt_upsampling` | BOOLEAN | Evet | - | Prompt üzerinde yukarı örnekleme yapılıp yapılmayacağı. Aktifse, prompt'u otomatik olarak daha yaratıcı oluşturum için değiştirir, ancak sonuçlar belirleyici değildir (aynı seed tam olarak aynı sonucu üretmez). (varsayılan: False) |
| `width` | INT | Evet | 256-1440 | Görüntü genişliği piksel cinsinden (varsayılan: 1024, adım: 32) |
| `height` | INT | Evet | 256-1440 | Görüntü yüksekliği piksel cinsinden (varsayılan: 768, adım: 32) |
| `seed` | INT | Evet | 0-18446744073709551615 | Gürültü oluşturmak için kullanılan rastgele seed. (varsayılan: 0) |
| `image_prompt` | IMAGE | Hayır | - | Oluşturumu yönlendirmek için isteğe bağlı referans görüntü |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | API'den döndürülen oluşturulmuş görüntü |