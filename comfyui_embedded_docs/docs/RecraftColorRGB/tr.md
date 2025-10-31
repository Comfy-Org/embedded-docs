> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/tr.md)

Belirli RGB değerlerini seçerek Recraft Rengi oluşturun. Bu düğüm, bireysel kırmızı, yeşil ve mavi değerlerini belirterek bir renk tanımlamanıza olanak tanır; bu değerler daha sonra diğer Recraft işlemlerinde kullanılabilecek bir Recraft renk formatına dönüştürülür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `k` | INT | Evet | 0-255 | Rengin kırmızı değeri (varsayılan: 0) |
| `y` | INT | Evet | 0-255 | Rengin yeşil değeri (varsayılan: 0) |
| `m` | INT | Evet | 0-255 | Rengin mavi değeri (varsayılan: 0) |
| `recraft_rengi` | COLOR | Hayır | - | Genişletmek için isteğe bağlı mevcut Recraft rengi |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `recraft_rengi` | COLOR | Belirtilen RGB değerlerini içeren oluşturulmuş Recraft renk nesnesi |