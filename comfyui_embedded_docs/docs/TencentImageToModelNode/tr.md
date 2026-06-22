# Hunyuan3D: Görsel(ler)den Modele (Pro)

Bu düğüm, Tencent'in Hunyuan3D Pro API'sini kullanarak bir veya daha fazla giriş görüntüsünden 3B model oluşturur. Görüntüleri işler, API'ye gönderir ve oluşturulan 3B model dosyalarını GLB ve OBJ formatlarında, isteğe bağlı doku haritalarıyla birlikte döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Hunyuan3D model sürümü. `3.1` modeli için LowPoly seçeneği kullanılamaz. | COMBO | Evet | `"3.0"`<br>`"3.1"` |
| `görsel` | 3B modeli oluşturmak için kullanılan birincil giriş görüntüsü. En az 128x128 piksel olmalıdır. | IMAGE | Evet | - |
| `sol görsel` | Çoklu görünüm oluşturma için nesnenin sol tarafının isteğe bağlı görüntüsü. En az 128x128 piksel olmalıdır. | IMAGE | Hayır | - |
| `sağ görsel` | Çoklu görünüm oluşturma için nesnenin sağ tarafının isteğe bağlı görüntüsü. En az 128x128 piksel olmalıdır. | IMAGE | Hayır | - |
| `arka görsel` | Çoklu görünüm oluşturma için nesnenin arka tarafının isteğe bağlı görüntüsü. En az 128x128 piksel olmalıdır. | IMAGE | Hayır | - |
| `yüz sayısı` | Oluşturulan 3B model için hedef yüz sayısı (varsayılan: 500000). | INT | Evet | 3000 - 1500000 |
| `oluşturma türü` | Oluşturulacak 3B model türü. Bir seçenek seçildiğinde ilgili ek parametreler görünür hale gelir. | DYNAMICCOMBO | Evet | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` |
| `generate_type.pbr` | Fiziksel Tabanlı Renderlama (PBR) malzeme oluşturmayı etkinleştirir. Bu parametre yalnızca `oluşturma türü` "Normal" veya "LowPoly" olarak ayarlandığında görünür (varsayılan: Yanlış). | BOOLEAN | Hayır | - |
| `generate_type.polygon_type` | Ağ için kullanılacak çokgen türü. Bu parametre yalnızca `oluşturma türü` "LowPoly" olarak ayarlandığında görünür. | COMBO | Hayır | `"triangle"`<br>`"quadrilateral"` |
| `tohum` | Oluşturma işlemi için bir tohum değeri. Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 - 2147483647 |

**Not:** Tüm giriş görüntüleri minimum 128 piksel genişliğe ve yüksekliğe sahip olmalıdır. Görüntüler, en uzun kenarları 4900 pikseli aşarsa otomatik olarak küçültülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `GLB` | Geriye dönük uyumluluk için eski bir çıktı. | STRING |
| `OBJ` | Oluşturulan 3B modelin GLB (İkili GL İletim Formatı) dosya formatındaki hali. | FILE3DGLB |
| `doku_görseli` | Oluşturulan 3B modelin OBJ (Wavefront) dosya formatındaki hali. | FILE3DOBJ |
| `isteğe_bağlı_metallic` | Oluşturulan 3B model için doku görüntüsü. | IMAGE |
| `isteğe_bağlı_normal` | PBR malzemeler için metalik haritası. Mevcut değilse siyah bir görüntü döndürür. | IMAGE |
| `isteğe_bağlı_roughness` | PBR malzemeler için normal haritası. Mevcut değilse siyah bir görüntü döndürür. | IMAGE |
| `optional_roughness` | PBR malzemeler için pürüzlülük haritası. Mevcut değilse siyah bir görüntü döndürür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentImageToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `56ac9e55bd9bb3a5c7c46c2de1ea06921cf41c0971471f6d0b64166722705e4d`
