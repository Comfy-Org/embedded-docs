> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToImageApi/tr.md)

Wan Image to Image düğümü, bir veya iki giriş görseli ve bir metin isteminden yeni bir görsel oluşturur. Girdi görsellerinizi sağladığınız açıklamaya dayanarak dönüştürür ve orijinal girdinizin en-boy oranını koruyan yeni bir görsel meydana getirir. Çıktı görseli, girdi boyutundan bağımsız olarak sabit 1.6 megapikseldir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | "wan2.5-i2i-preview" | Kullanılacak model (varsayılan: "wan2.5-i2i-preview"). |
| `image` | IMAGE | Evet | - | Tek görsel düzenleme veya çoklu görsel füzyonu, maksimum 2 görsel. |
| `prompt` | STRING | Evet | - | Öğeleri ve görsel özellikleri tanımlamak için kullanılan istem, İngilizce/Çince destekler (varsayılan: boş). |
| `negative_prompt` | STRING | Hayır | - | Nelerden kaçınılacağını yönlendirmek için kullanılan olumsuz metin istemi (varsayılan: boş). |
| `seed` | INT | Hayır | 0 ile 2147483647 arası | Oluşturma için kullanılacak seed değeri (varsayılan: 0). |
| `watermark` | BOOLEAN | Hayır | - | Sonuca "AI generated" filigranı eklenip eklenmeyeceği (varsayılan: true). |

**Not:** Bu düğüm tam olarak 1 veya 2 giriş görseli kabul eder. 2'den fazla görsel sağlarsanız veya hiç görsel sağlamazsanız, düğüm bir hata döndürecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Girdi görselleri ve metin istemlerine dayalı olarak oluşturulan görsel. |