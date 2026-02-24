> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/tr.md)

Kling Image(First Frame) to Video with Audio düğümü, Kling AI modelini kullanarak tek bir başlangıç görselinden ve bir metin isteminden kısa bir video oluşturur. Sağlanan görsel ile başlayan bir video dizisi oluşturur ve isteğe bağlı olarak görüntülere eşlik etmesi için yapay zeka tarafından üretilen sesi içerebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Evet | `"kling-v2-6"` | Video oluşturma için kullanılacak Kling AI modelinin belirli sürümü. |
| `start_frame` | IMAGE | Evet | - | Oluşturulan videonun ilk karesi olarak kullanılacak görsel. Görsel en az 300x300 piksel olmalı ve en boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır. |
| `prompt` | STRING | Evet | - | Olumlu metin istemi. Oluşturmak istediğiniz video içeriğini tanımlar. İstem 1 ile 2500 karakter uzunluğunda olmalıdır. |
| `mode` | COMBO | Evet | `"pro"` | Video oluşturma için işletim modu. |
| `duration` | COMBO | Evet | `5`<br>`10` | Oluşturulacak videonun uzunluğu, saniye cinsinden. |
| `generate_audio` | BOOLEAN | Hayır | - | Etkinleştirildiğinde, düğüm videoya eşlik edecek ses oluşturacaktır. Devre dışı bırakıldığında, video sessiz olacaktır. (varsayılan: True) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Oluşturulan video dosyası. `generate_audio` girişine bağlı olarak ses içerebilir. |
