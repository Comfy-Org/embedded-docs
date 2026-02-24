> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/tr.md)

Bu düğüm, Bria RMBG 2.0 servisini kullanarak bir görselin arka planını kaldırır. Görseli işlem için harici bir API'ye gönderir ve arka planı kaldırılmış sonucu döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Arka planının kaldırılacağı giriş görseli. |
| `moderation` | COMBO | Hayır | `"false"`<br>`"true"` | Denetim ayarları. `"true"` olarak ayarlandığında, ek denetim seçenekleri kullanılabilir hale gelir. |
| `visual_input_moderation` | BOOLEAN | Hayır | - | Giriş görseli üzerinde görsel içerik denetimini etkinleştirir. Bu parametre yalnızca `moderation` `"true"` olarak ayarlandığında kullanılabilir. Varsayılan: `False`. |
| `visual_output_moderation` | BOOLEAN | Hayır | - | Çıkış görseli üzerinde görsel içerik denetimini etkinleştirir. Bu parametre yalnızca `moderation` `"true"` olarak ayarlandığında kullanılabilir. Varsayılan: `True`. |
| `seed` | INT | Hayır | 0 - 2147483647 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eden bir seed değeri. Seed değerinden bağımsız olarak sonuçlar deterministik değildir. Varsayılan: `0`. |

**Not:** `visual_input_moderation` ve `visual_output_moderation` parametreleri `moderation` parametresine bağlıdır. Yalnızca `moderation` `"true"` olarak ayarlandığında etkin ve gerekli hale gelirler.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Arka planı kaldırılmış işlenmiş görsel. |