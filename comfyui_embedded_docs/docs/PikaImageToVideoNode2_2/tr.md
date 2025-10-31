> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/tr.md)

Pika Image to Video düğümü, bir görüntüyü ve metin istemini Pika API sürüm 2.2'ye göndererek bir video oluşturur. Girdi olarak verilen görüntünüzü, sağlanan açıklama ve ayarlara dayanarak video formatına dönüştürür. Düğüm, API iletişimini yönetir ve oluşturulan videoyu çıktı olarak döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | - | Videoya dönüştürülecek görüntü |
| `istem_metni` | STRING | Evet | - | Video oluşturmayı yönlendiren metin açıklaması |
| `negatif_istem` | STRING | Evet | - | Videoda nelerden kaçınılması gerektiğini açıklayan metin |
| `tohum` | INT | Evet | - | Tekrarlanabilir sonuçlar için rastgele tohum değeri |
| `çözünürlük` | STRING | Evet | - | Çıktı videosu çözünürlük ayarı |
| `süre` | INT | Evet | - | Oluşturulan videonun saniye cinsinden uzunluğu |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası |