# Hunyuan3D: 3D Parça

Bu düğüm, Tencent Hunyuan3D API'sini kullanarak bir 3D modeli otomatik olarak analiz eder ve model yapısına göre bileşenlerini tanımlar veya oluşturur. Modeli işler ve yeni bir FBX dosyası döndürür.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | FBX formatında 3D model. Modelin 30000 yüzden az olması gerekir. | FILE3D | Evet | FBX, Any |
| `seed` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 arası |

**Not:** `model_3d` girdisi yalnızca FBX formatındaki dosyaları destekler. Farklı bir 3D dosya formatı sağlanırsa, düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-------------|-------------|-----------|
| `FBX` | İşlenmiş 3D model, FBX dosyası olarak döndürülür. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DPartNode/tr.md)

---
**Source fingerprint (SHA-256):** `827b42559f4b2c341f08c58f53778d27c1c6afce607c36c8d1eae7c208c6a738`
