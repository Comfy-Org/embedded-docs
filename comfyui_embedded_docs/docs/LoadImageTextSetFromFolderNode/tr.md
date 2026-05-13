> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextSetFromFolderNode/tr.md)

Belirtilen eğitim amaçlı dizinden bir grup görsel ve bunlara karşılık gelen metin açıklamalarını yükler. Düğüm, görsel dosyalarını ve ilişkili açıklama metin dosyalarını otomatik olarak arar, belirtilen yeniden boyutlandırma ayarlarına göre görselleri işler ve sağlanan CLIP modelini kullanarak açıklamaları kodlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | Evet | - | Görsellerin yükleneceği klasör. |
| `clip` | CLIP | Evet | - | Metni kodlamak için kullanılan CLIP modeli. |
| `resize_method` | COMBO | Hayır | "Yok"<br>"Uzat"<br>"Kırp"<br>"Doldur" | Görselleri yeniden boyutlandırmak için kullanılan yöntem (varsayılan: "Yok"). |
| `width` | INT | Hayır | -1 ila 10000 | Görsellerin yeniden boyutlandırılacağı genişlik. -1, orijinal genişliğin kullanılacağı anlamına gelir (varsayılan: -1). |
| `height` | INT | Hayır | -1 ila 10000 | Görsellerin yeniden boyutlandırılacağı yükseklik. -1, orijinal yüksekliğin kullanılacağı anlamına gelir (varsayılan: -1). |

**Not:** CLIP girdisi geçerli olmalıdır ve Yok (None) olamaz. CLIP modeli bir kontrol noktası yükleyici düğümünden geliyorsa, kontrol noktasının geçerli bir CLIP veya metin kodlayıcı modeli içerdiğinden emin olun.

**Klasör yapısı hakkında not:** Düğüm, kohya-ss/sd-scripts klasör yapısını destekler. Bir alt klasörün adı, ardından bir alt çizgi ile birlikte bir sayı ile başlıyorsa (örneğin, `5_myclass`), bu sayı bir tekrar sayısı olarak kullanılır ve o alt klasörün içindeki görseller bu sayı kadar yüklenir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Yüklenen ve işlenen görsel grubu. |
| `CONDITIONING` | CONDITIONING | Metin açıklamalarından kodlanmış koşullandırma verileri. |

---
**Source fingerprint (SHA-256):** `ffd6399783fc281a58bae811112d9ecacb51ab8ea3b512befa9b9fab2c6860de`
