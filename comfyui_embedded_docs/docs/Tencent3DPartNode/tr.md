# Hunyuan3D: 3D Parça

Bu düğüm, Tencent Hunyuan3D API'sini kullanarak 3D modelin bileşenlerini yapısına göre otomatik olarak tanımlar ve üretir. Bir FBX modeli kabul eder, işler ve yeni bir FBX dosyası döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | FBX formatında 3D model. Modelin 30000'den az yüzü olmalıdır. | FILE3D | Evet | FBX, Any |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Hayır | 0 ile 2147483647 |

**Not:** `model_3d` girdisi yalnızca FBX formatındaki dosyaları destekler. Farklı bir 3D dosya formatı sağlanırsa düğüm hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `FBX` | İşlenmiş 3D model, FBX dosyası olarak döndürülür. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DPartNode/tr.md)

---
**Source fingerprint (SHA-256):** `827b42559f4b2c341f08c58f53778d27c1c6afce607c36c8d1eae7c208c6a738`
