> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSubtract/tr.md)

CLIPSubtract düğümü, iki CLIP modeli arasında çıkarma işlemi gerçekleştirir. İlk CLIP modelini temel alır ve ikinci CLIP modelinden anahtar yamaları çıkarır, çıkarma işleminin gücünü kontrol etmek için isteğe bağlı bir çarpan kullanılır. Bu, bir modelden belirli özelliklerin başka bir model kullanılarak çıkarılması yoluyla hassas ayarlanmış model harmanlamaya olanak tanır.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `clip1` | CLIP | Gerekli | - | - | Değiştirilecek temel CLIP modeli |
| `clip2` | CLIP | Gerekli | - | - | Temel modelden çıkarılacak anahtar yamaları içeren CLIP modeli |
| `multiplier` | FLOAT | Gerekli | 1.0 | -10.0 - 10.0, adım 0.01 | Çıkarma işleminin gücünü kontrol eder |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Çıkarma işleminden sonra elde edilen CLIP modeli |