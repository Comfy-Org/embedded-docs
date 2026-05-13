> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DPartNode/tr.md)

Bu düğüm, Tencent Hunyuan3D API'sini kullanarak bir 3B modeli otomatik olarak analiz eder ve yapısına göre bileşenlerini oluşturur veya tanımlar. Modeli işler ve yeni bir FBX dosyası döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model_3d` | FILE3D | Evet | FBX, Herhangi | İşlenecek 3B model. Model FBX formatında olmalı ve 30000'den az yüze sahip olmalıdır. |
| `seed` | INT | Hayır | 0 ile 2147483647 arası | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eden bir tohum değeri. Tohum değerinden bağımsız olarak sonuçlar deterministik değildir. (varsayılan: 0) |

**Not:** `model_3d` girdisi yalnızca FBX formatındaki dosyaları destekler. Farklı bir 3B dosya formatı sağlanırsa, düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `FBX` | FILE3DFBX | İşlenmiş 3B model, bir FBX dosyası olarak döndürülür. |

---
**Source fingerprint (SHA-256):** `eae7d0197d4391af1f5f24f120c64f1045649182108affad10b9a00f329310fe`
