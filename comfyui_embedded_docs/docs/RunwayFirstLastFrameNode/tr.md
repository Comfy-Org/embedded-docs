> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/tr.md)

Runway First-Last-Frame to Video düğümü, birinci ve son anahtar kareleri bir metin istemiyle birlikte yükleyerek videolar oluşturur. Runway'in Gen-3 modelini kullanarak sağlanan başlangıç ve bitiş kareleri arasında sorunsuz geçişler yaratır. Bu, özellikle bitiş karesinin başlangıç karesinden önemli ölçüde farklı olduğu karmaşık geçişler için kullanışlıdır.

## Girişler

| Parametre | Veri Tipi | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | Oluşturma için metin istemi (varsayılan: boş dize) |
| `start_frame` | IMAGE | Evet | Yok | Video için kullanılacak başlangıç karesi |
| `end_frame` | IMAGE | Evet | Yok | Video için kullanılacak bitiş karesi. Sadece gen3a_turbo için desteklenir. |
| `duration` | COMBO | Evet | Birden fazla seçenek mevcut | Mevcut Süre seçeneklerinden video süresi seçimi |
| `ratio` | COMBO | Evet | Birden fazla seçenek mevcut | Mevcut RunwayGen3aAspectRatio seçeneklerinden en-boy oranı seçimi |
| `seed` | INT | Hayır | 0-4294967295 | Oluşturma için rastgele tohum değeri (varsayılan: 0) |

**Parametre Kısıtlamaları:**

- `prompt` en az 1 karakter içermelidir
- Hem `start_frame` hem de `end_frame` maksimum 7999x7999 piksel boyutlarına sahip olmalıdır
- Hem `start_frame` hem de `end_frame` 0.5 ile 2.0 arasında en-boy oranına sahip olmalıdır
- `end_frame` parametresi sadece gen3a_turbo modeli kullanılırken desteklenir

## Çıkışlar

| Çıkış Adı | Veri Tipi | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Başlangıç ve bitiş kareleri arasında geçiş yapan oluşturulmuş video |