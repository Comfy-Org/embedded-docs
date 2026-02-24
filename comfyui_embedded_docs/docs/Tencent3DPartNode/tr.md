> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DPartNode/tr.md)

Bu düğüm, Tencent Hunyuan3D API'sini kullanarak bir 3B modeli otomatik olarak analiz eder ve yapısına dayalı olarak bileşenlerini oluşturur veya tanımlar. Modeli işler ve yeni bir FBX dosyası döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | Evet | FBX, Herhangi | İşlenecek 3B model. Model FBX formatında olmalı ve 30000'den az yüze sahip olmalıdır. |
| `seed` | INT | Hayır | 0 ile 2147483647 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol etmek için bir başlangıç değeri. Sonuçlar, başlangıç değerinden bağımsız olarak deterministik değildir. (varsayılan: 0) |

**Not:** `model_3d` girişi yalnızca FBX formatındaki dosyaları destekler. Farklı bir 3B dosya formatı sağlanırsa, düğüm bir hata verecektir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `FBX` | FILE3DFBX | İşlenmiş 3B model, bir FBX dosyası olarak döndürülür. |