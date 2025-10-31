> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/tr.md)

Pika Image to Video düğümü, bir görüntüyü ve metin istemini Pika API sürüm 2.2'ye göndererek bir video oluşturur. Girdi olarak verilen görüntünüzü, sağlanan açıklama ve ayarlara dayanarak video formatına dönüştürür. Düğüm, API iletişimini yönetir ve oluşturulan videoyu çıktı olarak döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Videoya dönüştürülecek görüntü |
| `prompt_text` | STRING | Evet | - | Video oluşturmayı yönlendiren metin açıklaması |
| `negative_prompt` | STRING | Evet | - | Videoda nelerden kaçınılması gerektiğini açıklayan metin |
| `seed` | INT | Evet | - | Tekrarlanabilir sonuçlar için rastgele tohum değeri |
| `resolution` | STRING | Evet | - | Çıktı videosu çözünürlük ayarı |
| `duration` | INT | Evet | - | Oluşturulan videonun saniye cinsinden uzunluğu |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası |