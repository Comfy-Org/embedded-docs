> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxSubjectToVideoNode/tr.md)

Bir görüntü ve istek metni ile isteğe bağlı parametreleri kullanarak MiniMax'in API'si aracılığıyla senkronize video oluşturur. Bu düğüm, MiniMax'in video oluşturma hizmetini kullanarak bir video oluşturmak için bir konu görüntüsü ve metin açıklaması alır.

## Girdiler

| Parametre | Veri Tipi | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `subject` | IMAGE | Evet | - | Video oluşturma için referans alınacak konunun görüntüsü |
| `prompt_text` | STRING | Evet | - | Video oluşturmayı yönlendiren metin istemi (varsayılan: boş dize) |
| `model` | COMBO | Hayır | "S2V-01"<br> | Video oluşturma için kullanılacak model (varsayılan: "S2V-01") |
| `seed` | INT | Hayır | 0 ile 18446744073709551615 arası | Gürültü oluşturmak için kullanılan rastgele tohum (varsayılan: 0) |

## Çıktılar

| Çıktı Adı | Veri Tipi | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Girdi olarak verilen konu görüntüsü ve istek metnine dayalı olarak oluşturulan video |