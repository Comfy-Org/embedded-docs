> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentModelTo3DUVNode/tr.md)

Bu düğüm, Tencent Hunyuan3D API'sini kullanarak bir 3B model üzerinde UV açma işlemi gerçekleştirir. Bir 3B model dosyasını girdi olarak alır, işlenmek üzere API'ye gönderir ve işlenmiş modeli OBJ ve FBX formatlarında, oluşturulmuş bir UV doku görüntüsüyle birlikte döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | Evet | GLB<br>OBJ<br>FBX | Girdi 3B model (GLB, OBJ veya FBX). Modelin 30000'den az yüzü olmalıdır. |
| `seed` | INT | Hayır | 0 ile 2147483647 arası | Bir tohum değeri (varsayılan: 1). Bu, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder, ancak sonuçlar tohum değerinden bağımsız olarak deterministik değildir. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `OBJ` | FILE3D | İşlenmiş 3B model dosyası, OBJ formatında. |
| `FBX` | FILE3D | İşlenmiş 3B model dosyası, FBX formatında. |
| `Image` | IMAGE | Oluşturulan UV doku görüntüsü. |