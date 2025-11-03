> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/tr.md)

Bu düğüm, mevcut bir görseli metin istemi ve güç parametresine dayanarak değiştirir. Recraft API'sini kullanarak, giriş görselini sağlanan açıklamaya göre dönüştürür ve güç ayarına bağlı olarak orijinal görsele olan benzerliğin bir kısmını korur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | - | Değiştirilecek giriş görseli |
| `istem` | STRING | Evet | - | Görsel oluşturma için istem (varsayılan: "") |
| `n` | INT | Evet | 1-6 | Oluşturulacak görsel sayısı (varsayılan: 1) |
| `güç` | FLOAT | Evet | 0.0-1.0 | Orijinal görselden farkı tanımlar, [0, 1] aralığında olmalıdır; 0 neredeyse aynı, 1 ise çok az benzerlik anlamına gelir (varsayılan: 0.5) |
| `tohum` | INT | Evet | 0-18446744073709551615 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak belirleyici değildir (varsayılan: 0) |
| `recraft_stili` | STYLEV3 | Hayır | - | Görsel oluşturma için isteğe bağlı stil seçimi |
| `negatif_istem` | STRING | Hayır | - | Bir görselde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: "") |
| `recraft_kontrolleri` | CONTROLS | Hayır | - | Recraft Kontroller düğümü aracılığıyla oluşturma üzerinde isteğe bağlı ek kontroller |

**Not:** `seed` parametresi yalnızca düğümün yeniden yürütülmesini tetikler ancak belirleyici sonuçları garanti etmez. Güç parametresi dahili olarak 2 ondalık basamağa yuvarlanır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `görüntü` | IMAGE | Giriş görseli ve isteme dayalı olarak oluşturulan görsel(ler) |