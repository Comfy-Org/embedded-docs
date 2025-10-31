> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/tr.md)

PikaFrames v2.2 Düğümü, ilk ve son karelerinizi birleştirerek videolar oluşturur. Başlangıç ve bitiş noktalarını tanımlamak için iki resim yüklersiniz ve AI, tam bir video oluşturmak için bunlar arasında sorunsuz bir geçiş oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `başlangıç_görüntüsü` | IMAGE | Evet | - | Birleştirilecek ilk resim. |
| `bitiş_görüntüsü` | IMAGE | Evet | - | Birleştirilecek son resim. |
| `istem_metni` | STRING | Evet | - | İstenen video içeriğini tanımlayan metin istemi. |
| `negatif_istem` | STRING | Evet | - | Videoda nelerden kaçınılması gerektiğini açıklayan metin. |
| `tohum` | INT | Evet | - | Üretim tutarlılığı için rastgele tohum değeri. |
| `çözünürlük` | STRING | Evet | - | Çıktı videosunun çözünürlüğü. |
| `süre` | INT | Evet | - | Oluşturulan videonun süresi. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Başlangıç ve bitiş karelerini AI geçişleriyle birleştirerek oluşturulan video. |