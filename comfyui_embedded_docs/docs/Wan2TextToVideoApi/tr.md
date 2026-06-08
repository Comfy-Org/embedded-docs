Bu düğüm, Wan 2.7 modelini kullanarak bir metin açıklamasından video oluşturur. İsteğinizi, istemi işleyen ve bir video dosyası döndüren harici bir API'ye gönderir. Videonun hareketini ve zamanlamasını etkilemek için isteğe bağlı olarak bir ses klibi sağlayabilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak belirli model. | COMBO | Evet | `"wan2.7-t2v"` |
| `model.prompt` | Videoda istediğiniz öğelerin ve görsel özelliklerin açıklaması. İngilizce ve Çinceyi destekler. | STRING | Evet | - |
| `model.negative_prompt` | Oluşturulan videoda kaçınmak istediğiniz öğelerin veya özelliklerin açıklaması. | STRING | Hayır | - |
| `model.resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720P"`<br>`"1080P"` |
| `model.ratio` | Çıktı videosunun en-boy oranı. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `model.duration` | Videonun saniye cinsinden uzunluğu (varsayılan: 5). | INT | Evet | 2 ila 15 |
| `ses` | Dudak senkronizasyonu veya ritme uygun hareket gibi video oluşturmayı yönlendirmek için bir ses dosyası. Sağlanmazsa, model eşleşen bir arka plan müziği veya ses efektleri oluşturur. Ses süresi 1,5 ila 60 saniye arasında olmalıdır. | AUDIO | Hayır | - |
| `tohum` | Tekrarlanabilir sonuçlar sağlamak için oluşturmanın rastgeleliğini kontrol etmek için kullanılan bir sayı (varsayılan: 0). | INT | Hayır | 0 ila 2147483647 |
| `istem_genişlet` | Etkinleştirildiğinde, istem yapay zeka yardımıyla geliştirilecektir (varsayılan: True). | BOOLEAN | Hayır | - |
| `filigran` | Etkinleştirildiğinde, sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenir (varsayılan: False). | BOOLEAN | Hayır | - |

**Not:** `audio` parametresi isteğe bağlıdır. Sağlanırsa, süresi 1,5 ila 60 saniye arasında olmalıdır. Atlanırsa, model otomatik olarak ses oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `ce8a2f4e53b2bce879f143c66f6078fd81c6308e2822cb486b1cf8e178a6f58c`
