> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxTextToVideoNode/tr.md)

Verilen metin istemine ve isteğe bağlı parametrelere dayanarak MiniMax'in API'sini kullanarak videoları senkronize bir şekilde oluşturur. Bu düğüm, MiniMax'in metinden videoya hizmetine bağlanarak metin açıklamalarından video içeriği oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | Evet | - | Video oluşturmayı yönlendiren metin istemi |
| `model` | COMBO | Hayır | "T2V-01"<br>"T2V-01-Director" | Video oluşturma için kullanılacak model (varsayılan: "T2V-01") |
| `seed` | INT | Hayır | 0 ila 18446744073709551615 | Gürültü oluşturmak için kullanılan rastgele tohum değeri (varsayılan: 0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Girdi istemine dayalı olarak oluşturulan video |