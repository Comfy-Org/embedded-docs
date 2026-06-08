Bu düğüm, bir 3B model üzerinde UV açılımı (UV unfolding) gerçekleştirmek için Tencent Hunyuan3D API'sini kullanır. Giriş olarak bir 3B model dosyası alır, işlenmek üzere API'ye gönderir ve işlenmiş modeli OBJ ve FBX formatlarında, ayrıca oluşturulan UV doku görüntüsüyle birlikte döndürür. Giriş modeli 30.000'den az yüze sahip olmalıdır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model_3d` | Giriş 3B modeli (GLB, OBJ veya FBX). Model 30000'den az yüze sahip olmalıdır. | FILE3D | Evet | GLB<br>OBJ<br>FBX |
| `tohum` | Bir tohum değeri (varsayılan: 1). Bu, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder, ancak tohum değerinden bağımsız olarak sonuçlar deterministik değildir. | INT | Hayır | 0 ile 2147483647 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `FBX` | OBJ formatında işlenmiş 3B model dosyası. | FILE3D |
| `uv_görüntüsü` | FBX formatında işlenmiş 3B model dosyası. | FILE3D |
| `uv_image` | Oluşturulan UV doku görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentModelTo3DUVNode/tr.md)

---
**Source fingerprint (SHA-256):** `16bf094cfc3146e9d302d73862d2080b94c5aa2d575221d3c8316a3cf69fc5e1`
