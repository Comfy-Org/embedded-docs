> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/tr.md)

Bir başlangıç ve bitiş noktası arasında enterpolasyonlu güç değerlerine sahip bir kanca kare dizisi oluşturur. Bu düğüm, üretim sürecinin belirli bir yüzdelik aralığı boyunca güç parametresini sorunsuz bir şekilde geçiş yapacak şekilde, geçiş eğrisini kontrol etmek için çeşitli enterpolasyon yöntemlerini kullanarak birden fazla kare oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `başlangıç_gücü` | FLOAT | Evet | 0.0 - 10.0 | Enterpolasyon dizisi için başlangıç güç değeri (varsayılan: 1.0) |
| `bitiş_gücü` | FLOAT | Evet | 0.0 - 10.0 | Enterpolasyon dizisi için bitiş güç değeri (varsayılan: 1.0) |
| `enterpolasyon` | COMBO | Evet | Birden fazla seçenek mevcut | Güç değerleri arasında geçiş yapmak için kullanılan enterpolasyon yöntemi |
| `başlangıç_yüzdesi` | FLOAT | Evet | 0.0 - 1.0 | Üretim sürecindeki başlangıç yüzdelik konumu (varsayılan: 0.0) |
| `bitiş_yüzdesi` | FLOAT | Evet | 0.0 - 1.0 | Üretim sürecindeki bitiş yüzdelik konumu (varsayılan: 1.0) |
| `anahtar_kare_sayısı` | INT | Evet | 2 - 100 | Enterpolasyon dizisinde oluşturulacak kare sayısı (varsayılan: 5) |
| `anahtar_kareleri_yazdır` | BOOLEAN | Evet | Doğru/Yanlış | Oluşturulan kare bilgilerini günlüğe yazdırıp yazdırmayacağı (varsayılan: Yanlış) |
| `önceki_kanca_kf` | HOOK_KEYFRAMES | Hayır | - | Eklenecek isteğe bağlı önceki kanca kareleri grubu |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | Enterpolasyonlu diziyi içeren oluşturulmuş kanca kareleri grubu |