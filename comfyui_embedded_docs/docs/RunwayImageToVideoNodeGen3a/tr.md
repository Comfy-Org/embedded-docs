> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/tr.md)

Runway Image to Video (Gen3a Turbo) düğümü, Runway'nin Gen3a Turbo modelini kullanarak tek bir başlangıç karesinden video oluşturur. Bir metin istemi ve bir başlangıç görüntü karesi alır, ardından belirtilen süre ve en-boy oranına dayalı olarak bir video dizisi oluşturur. Bu düğüm, işlemi uzaktan gerçekleştirmek için Runway'nin API'sına bağlanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | Oluşturma için metin istemi (varsayılan: "") |
| `start_frame` | IMAGE | Evet | Yok | Video için kullanılacak başlangıç karesi |
| `duration` | COMBO | Evet | Birden fazla seçenek mevcut | Mevcut seçeneklerden video süresi seçimi |
| `ratio` | COMBO | Evet | Birden fazla seçenek mevcut | Mevcut seçeneklerden en-boy oranı seçimi |
| `seed` | INT | Hayır | 0-4294967295 | Oluşturma için rastgele tohum (varsayılan: 0) |

**Parametre Kısıtlamaları:**

- `start_frame` boyutları 7999x7999 pikseli aşmamalıdır
- `start_frame` en-boy oranı 0.5 ile 2.0 arasında olmalıdır
- `prompt` en az bir karakter içermelidir (boş olamaz)

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dizisi |