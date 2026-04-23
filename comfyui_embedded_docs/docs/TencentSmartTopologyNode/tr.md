> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/tr.md)

Bu belge, yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/en.md)

Bu düğüm, bir 3B model üzerinde akıllı yeniden topoloji (retopoloji) işlemi gerçekleştirir. Bu işlem, daha düşük poligon sayısına sahip, yeni ve daha temiz bir ağın (mesh) otomatik olarak oluşturulmasıdır. Modeli işlemek için bir Tencent Hunyuan 3D API'sine bağlanır ve GLB ile OBJ dosya formatlarını destekler. Düğüm, işlenmiş modeli bir OBJ dosyası olarak döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | Evet | - | Giriş 3B modeli (GLB veya OBJ). Dosya GLB veya OBJ formatında olmalı ve 200MB'ı geçmemelidir. |
| `polygon_type` | STRING | Evet | `"triangle"`<br>`"quadrilateral"` | Yüzey bileşim türü. |
| `face_level` | STRING | Evet | `"medium"`<br>`"high"`<br>`"low"` | Poligon azaltma seviyesi. |
| `seed` | INT | Hayır | 0 ile 2147483647 arası | Tohum (seed), düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; tohumdan bağımsız olarak sonuçlar deterministik değildir. (varsayılan: 0) |

**Not:** `seed` parametresi düğümün yeniden çalıştırılmasını tetiklemek için kullanılır, ancak aynı tohum değeri için nihai çıktının aynı olacağı garanti edilmez.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `OBJ` | FILE3D | Optimize edilmiş topolojiye sahip, OBJ formatında döndürülen işlenmiş 3B model. |