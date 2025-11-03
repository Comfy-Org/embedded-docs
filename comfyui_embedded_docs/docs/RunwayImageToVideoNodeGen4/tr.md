> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen4/tr.md)

Runway Image to Video (Gen4 Turbo) düğümü, Runway'nin Gen4 Turbo modelini kullanarak tek bir başlangıç karesinden bir video oluşturur. Bir metin istemi ve bir başlangıç görüntü karesi alır, ardından sağlanan süre ve en-boy oranı ayarlarına dayalı olarak bir video dizisi oluşturur. Düğüm, başlangıç karesini Runway'nin API'sine yüklemeyi halleder ve oluşturulan videoyu döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Oluşturma için metin istemi (varsayılan: boş dize) |
| `start_frame` | IMAGE | Evet | - | Video için kullanılacak başlangıç karesi |
| `duration` | COMBO | Evet | Birden fazla seçenek mevcut | Mevcut süre seçeneklerinden video süresi seçimi |
| `ratio` | COMBO | Evet | Birden fazla seçenek mevcut | Mevcut Gen4 Turbo en-boy oranı seçeneklerinden en-boy oranı seçimi |
| `seed` | INT | Hayır | 0 ile 4294967295 arası | Oluşturma için rastgele tohum değeri (varsayılan: 0) |

**Parametre Kısıtlamaları:**

- `start_frame` görüntüsünün boyutları 7999x7999 pikseli aşmamalıdır
- `start_frame` görüntüsünün en-boy oranı 0.5 ile 2.0 arasında olmalıdır
- `prompt` en az bir karakter içermelidir

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Girdi karesi ve isteme dayalı olarak oluşturulan video |