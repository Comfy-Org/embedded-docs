> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextSetFromFolderNode/tr.md)

Belirtilen bir dizinden eğitim amacıyla bir grup görüntüyü ve bunlara karşılık gelen metin açıklamalarını yükler. Bu düğüm, görüntü dosyalarını ve bunlarla ilişkili metin açıklama dosyalarını otomatik olarak arar, görüntüleri belirtilen yeniden boyutlandırma ayarlarına göre işler ve açıklamaları sağlanan CLIP modelini kullanarak kodlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | Evet | - | Görüntülerin yükleneceği klasör. |
| `clip` | CLIP | Evet | - | Metni kodlamak için kullanılan CLIP modeli. |
| `resize_method` | COMBO | Hayır | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | Görüntüleri yeniden boyutlandırmak için kullanılan yöntem (varsayılan: "None"). |
| `width` | INT | Hayır | -1 - 10000 | Görüntülerin yeniden boyutlandırılacağı genişlik. -1, orijinal genişliği kullan anlamına gelir (varsayılan: -1). |
| `height` | INT | Hayır | -1 - 10000 | Görüntülerin yeniden boyutlandırılacağı yükseklik. -1, orijinal yüksekliği kullan anlamına gelir (varsayılan: -1). |

**Not:** CLIP girişi geçerli olmalıdır ve None olamaz. CLIP modeli bir kontrol noktası yükleyici düğümünden geliyorsa, kontrol noktasının geçerli bir CLIP veya metin kodlayıcı modeli içerdiğinden emin olun.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Yüklenen ve işlenen görüntülerin grubu. |
| `CONDITIONING` | CONDITIONING | Metin açıklamalarından elde edilen kodlanmış koşullandırma verileri. |