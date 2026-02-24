> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/tr.md)

Kling Text to Video with Audio düğümü, bir metin açıklamasından kısa bir video oluşturur. Kling AI servisine bir istek gönderir; servis, prompt'u işler ve bir video dosyası döndürür. Düğüm ayrıca, metne dayalı olarak videoya eşlik eden bir ses de oluşturabilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Evet | `"kling-v2-6"` | Video oluşturma için kullanılacak belirli AI modeli. |
| `prompt` | STRING | Evet | - | Pozitif metin prompt'u. Videoyu oluşturmak için kullanılan açıklama. 1 ile 2500 karakter arasında olmalıdır. |
| `mode` | COMBO | Evet | `"pro"` | Video oluşturma için operasyonel mod. |
| `aspect_ratio` | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Oluşturulacak video için istenen genişlik-yükseklik oranı. |
| `duration` | COMBO | Evet | `5`<br>`10` | Videoyun saniye cinsinden uzunluğu. |
| `generate_audio` | BOOLEAN | Hayır | - | Video için ses oluşturulup oluşturulmayacağını kontrol eder. Etkinleştirildiğinde, AI prompt'a dayalı olarak ses oluşturacaktır. (varsayılan: `True`) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası. |
