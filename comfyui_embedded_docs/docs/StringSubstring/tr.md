> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringSubstring/tr.md)

StringSubstring düğümü, daha büyük bir metin dizisinden bir bölüm çıkarır. Çıkarmak istediğiniz bölümü tanımlamak için bir başlangıç pozisyonu ve bitiş pozisyonu alır, ardından bu iki pozisyon arasındaki metni döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Evet | - | Çıkarma işlemi yapılacak giriş metin dizisi |
| `start` | INT | Evet | - | Alt dizi için başlangıç pozisyon indeksi |
| `end` | INT | Evet | - | Alt dizi için bitiş pozisyon indeksi |

## Çıktılar

| Çıktı Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Giriş metninden çıkarılan alt dizi |