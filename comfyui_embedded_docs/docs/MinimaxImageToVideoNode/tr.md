> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxImageToVideoNode/tr.md)

Bir görüntü, metin açıklaması ve isteğe bağlı parametreler kullanarak MiniMax'in API'si aracılığıyla senkronize bir şekilde video oluşturur. Bu düğüm, bir video dizisi oluşturmak için bir giriş görüntüsü ve metin açıklaması alır ve çeşitli model seçenekleri ve yapılandırma ayarları mevcuttur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | - | Video oluşturmanın ilk karesi olarak kullanılacak görüntü |
| `istem_metni` | STRING | Evet | - | Video oluşturmayı yönlendiren metin açıklaması (varsayılan: boş dize) |
| `model` | COMBO | Evet | "I2V-01-Director"<br>"I2V-01"<br>"I2V-01-live" | Video oluşturma için kullanılacak model (varsayılan: "I2V-01") |
| `tohum` | INT | Hayır | 0 ila 18446744073709551615 | Gürültü oluşturmak için kullanılan rastgele tohum değeri (varsayılan: 0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video çıktısı |