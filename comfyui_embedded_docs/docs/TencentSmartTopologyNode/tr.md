# Hunyuan3D: Akıllı Topoloji

Bu düğüm, bir 3B model üzerinde akıllı yeniden topoloji gerçekleştirerek optimize edilmiş çokgen sayısına sahip yeni, daha temiz bir ağ otomatik olarak oluşturur. Modeli işlemek için bir Tencent Hunyuan 3D API'sine bağlanır ve 200MB'a kadar GLB ve OBJ dosya formatlarını destekler. Düğüm, işlenmiş modeli bir OBJ dosyası olarak döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model_3d` | Giriş 3B modeli (GLB veya OBJ). Dosya GLB veya OBJ formatında olmalı ve 200MB'ı geçemez. | FILE3D | Evet | - |
| `poligon_tipi` | Yüzey bileşim türü. | STRING | Evet | `"triangle"`<br>`"quadrilateral"` |
| `yüz seviyesi` | Çokgen azaltma seviyesi. | STRING | Evet | `"medium"`<br>`"high"`<br>`"low"` |
| `tohum` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 arası |

**Not:** `seed` parametresi düğümün yeniden çalıştırılmasını tetiklemek için kullanılır, ancak nihai çıktının aynı tohum değeri için aynı olacağı garanti edilmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `OBJ` | Optimize edilmiş topolojiye sahip, OBJ formatında döndürülen işlenmiş 3B model. | FILE3D |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/tr.md)

---
**Source fingerprint (SHA-256):** `13c2dce5f5fbc46a505d0366d8da1c4e762d3a64d11fae1bcceebd510b273f62`
