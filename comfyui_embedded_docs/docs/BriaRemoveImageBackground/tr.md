# Bria Görsel Arka Planı Kaldır

Bu düğüm, Bria RMBG 2.0 hizmetini kullanarak bir görselden arka planı kaldırır. Görseli işlenmek üzere harici bir API'ye gönderir ve arka planı kaldırılmış sonucu döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görsel` | Arka planı kaldırılacak giriş görseli. | IMAGE | Evet | - |
| `moderasyon` | Denetleme ayarları. `"true"` olarak ayarlandığında ek denetleme seçenekleri kullanılabilir hale gelir. | COMBO | Hayır | `"false"`<br>`"true"` |
| `visual_input_moderation` | Giriş görselinde görsel içerik denetimini etkinleştirir. Bu parametre yalnızca `moderasyon` `"true"` olarak ayarlandığında kullanılabilir. Varsayılan: `False`. | BOOLEAN | Hayır | - |
| `visual_output_moderation` | Çıkış görselinde görsel içerik denetimini etkinleştirir. Bu parametre yalnızca `moderasyon` `"true"` olarak ayarlandığında kullanılabilir. Varsayılan: `True`. | BOOLEAN | Hayır | - |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eden bir tohum değeri. Tohum değerinden bağımsız olarak sonuçlar deterministik değildir. Varsayılan: `0`. | INT | Hayır | 0 ile 2147483647 arası |

**Not:** `visual_input_moderation` ve `visual_output_moderation` parametreleri `moderation` parametresine bağlıdır. Bu parametreler yalnızca `moderation` `"true"` olarak ayarlandığında etkin ve zorunludur.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görsel` | Arka planı kaldırılmış işlenmiş görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/tr.md)

---
**Source fingerprint (SHA-256):** `2b2dd3ca0d026af1a2bf3f7222165928527b05b65817073b50230ff18d39bc6c`
