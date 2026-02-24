> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/tr.md)

Video Slice düğümü, bir videodan belirli bir bölümü çıkarmanıza olanak tanır. Videoyu kırpmak için bir başlangıç zamanı ve süre tanımlayabilir veya yalnızca başlangıç karelerini atlayabilirsiniz. İstenen süre, videonun kalan kısmından daha uzunsa, düğüm mevcut olanı döndürebilir veya bir hata verebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Evet | - | Kırpılacak giriş videosu. |
| `start_time` | FLOAT | Hayır | -1e5 ila 1e5 | Dilimin başlayacağı saniye cinsinden başlangıç zamanı. Negatif bir değer, videonun başından kareler atlanmasını sağlar. (varsayılan: 0.0) |
| `duration` | FLOAT | Hayır | 0.0 ve üzeri | Dilimin saniye cinsinden uzunluğu. 0.0 değeri, düğümün başlangıç zamanından sonuna kadar tüm videoyu döndüreceği anlamına gelir. (varsayılan: 0.0) |
| `strict_duration` | BOOLEAN | Hayır | - | True olarak ayarlanırsa, istenen süre karşılanamazsa (örneğin, dilim videonun sonunu aşarsa) düğüm bir hata verir. False ise, sonuna kadar mevcut videoyu döndürür. (varsayılan: False) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Kırpılmış video bölümü. |