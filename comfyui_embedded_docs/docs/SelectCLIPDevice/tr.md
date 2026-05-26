> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectCLIPDevice/tr.md)

## Genel Bakış

Select CLIP Device düğümü, CLIP metin kodlayıcısının hangi cihazda (CPU veya belirli bir GPU) çalışacağını seçmenizi sağlar. Varsayılan olarak cihaz, model yükleyici tarafından atanır; ancak siz bunu geçersiz kılarak CPU veya belirli bir GPU kullanabilirsiniz. İstenen cihaz sisteminizde mevcut değilse, düğüm herhangi bir hata oluşturmak yerine CLIP'i değiştirmeden geçirir ve bir mesaj kaydeder.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | | Belirli bir cihaza atanacak CLIP metin kodlayıcısı. |
| `device` | COMBO | Evet | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>`"gpu:2"`<br>`"gpu:3"`<br>`"gpu:4"`<br>`"gpu:5"`<br>`"gpu:6"`<br>`"gpu:7"` | CLIP metin kodlayıcısının yerleştirileceği cihaz. `"default"`, yükleyici tarafından atanan cihazı geri yükler. `"cpu"`, hem yükleme hem de boşaltma cihazını CPU'ya sabitler. `"gpu:N"`, yükleme cihazını N. kullanılabilir GPU'ya sabitler (varsayılan: `"default"`). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `clip` | CLIP | Seçilen cihaza atanmış CLIP metin kodlayıcısı veya istenen cihaz mevcut değilse değiştirilmeden geçirilen orijinal CLIP. |

---
**Source fingerprint (SHA-256):** `92af94d9f5eea27095cc008debdf7339d26888a0e2cc8bd71ae9c9ba8718eb01`
