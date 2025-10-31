> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/tr.md)

Sağlanan açıklamaya dayanarak görselin arka planını değiştirir. Bu düğüm, ana nesneyi bozmadan arka planı tamamen dönüştürmenize olanak tanıyarak, metin açıklamanıza göre görselleriniz için yeni arka planlar oluşturmak üzere Recraft API'sini kullanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | İşlenecek girdi görseli |
| `prompt` | STRING | Evet | - | Görsel oluşturma için açıklama (varsayılan: boş) |
| `n` | INT | Evet | 1-6 | Oluşturulacak görsel sayısı (varsayılan: 1) |
| `seed` | INT | Evet | 0-18446744073709551615 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 0) |
| `recraft_style` | STYLEV3 | Hayır | - | Oluşturulan arka plan için isteğe bağlı stil seçimi |
| `negative_prompt` | STRING | Hayır | - | Bir görselde istenmeyen unsurların isteğe bağlı metin açıklaması (varsayılan: boş) |

**Not:** `seed` parametresi, düğümün ne zaman yeniden yürütüleceğini kontrol eder ancak harici API'nın doğası gereği deterministik sonuçları garanti etmez.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Arka planı değiştirilmiş olarak oluşturulan görsel(ler) |