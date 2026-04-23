> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/tr.md)

Bu düğüm, Wan 2.7 modelini kullanarak bir metin açıklamasından video oluşturur. İsteğinizi, istemi işleyen ve bir video dosyası döndüren harici bir API'ye gönderir. Videonun hareketini ve zamanlamasını etkilemek için isteğe bağlı olarak bir ses klibi sağlayabilirsiniz.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"wan2.7-t2v"` | Video oluşturma için kullanılacak belirli model. |
| `model.prompt` | STRING | Evet | - | Videoda istediğiniz öğelerin ve görsel özelliklerin açıklaması. İngilizce ve Çinceyi destekler. |
| `model.negative_prompt` | STRING | Hayır | - | Oluşturulan videoda kaçınmak istediğiniz öğelerin veya özelliklerin açıklaması. |
| `model.resolution` | COMBO | Evet | `"720P"`<br>`"1080P"` | Çıktı videosunun çözünürlüğü. |
| `model.ratio` | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | Çıktı videosunun en-boy oranı. |
| `model.duration` | INT | Evet | 2 ila 15 | Videonun saniye cinsinden uzunluğu (varsayılan: 5). |
| `audio` | AUDIO | Hayır | - | Dudak senkronizasyonu veya ritme uygun hareket gibi video oluşturmayı yönlendirmek için bir ses dosyası. Sağlanmazsa, model eşleşen bir arka plan müziği veya ses efektleri oluşturur. Ses süresi 3 ila 30 saniye arasında olmalıdır. |
| `seed` | INT | Hayır | 0 ila 2147483647 | Tekrarlanabilir sonuçlar sağlamak için oluşturmanın rastgeleliğini kontrol etmek için kullanılan bir sayı (varsayılan: 0). |
| `prompt_extend` | BOOLEAN | Hayır | - | Etkinleştirildiğinde, istem yapay zeka yardımıyla geliştirilir (varsayılan: True). |
| `watermark` | BOOLEAN | Hayır | - | Etkinleştirildiğinde, sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenir (varsayılan: False). |

**Not:** `audio` parametresi isteğe bağlıdır. Sağlanırsa, süresi 3 ila 30 saniye arasında olmalıdır. Atlanırsa, model otomatik olarak ses oluşturur.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası. |