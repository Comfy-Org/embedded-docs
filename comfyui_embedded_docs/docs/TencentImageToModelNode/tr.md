> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentImageToModelNode/tr.md)

Bu düğüm, Tencent'in Hunyuan3D Pro API'sini kullanarak bir veya daha fazla giriş görüntüsünden 3B model oluşturur. Görüntüleri işler, API'ye gönderir ve oluşturulan 3B model dosyalarını GLB ve OBJ formatlarında, isteğe bağlı doku haritalarıyla birlikte döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"3.0"`<br>`"3.1"` | Kullanılacak Hunyuan3D model sürümü. `3.1` modeli için LowPoly seçeneği kullanılamaz. |
| `image` | IMAGE | Evet | - | 3B modeli oluşturmak için kullanılan birincil giriş görüntüsü. En az 128x128 piksel olmalıdır. |
| `image_left` | IMAGE | Hayır | - | Çoklu görünüm oluşturma için nesnenin sol tarafının isteğe bağlı görüntüsü. En az 128x128 piksel olmalıdır. |
| `image_right` | IMAGE | Hayır | - | Çoklu görünüm oluşturma için nesnenin sağ tarafının isteğe bağlı görüntüsü. En az 128x128 piksel olmalıdır. |
| `image_back` | IMAGE | Hayır | - | Çoklu görünüm oluşturma için nesnenin arka tarafının isteğe bağlı görüntüsü. En az 128x128 piksel olmalıdır. |
| `face_count` | INT | Evet | 3000 - 1500000 | Oluşturulan 3B model için hedef yüz sayısı (varsayılan: 500000). |
| `generate_type` | DYNAMICCOMBO | Evet | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` | Oluşturulacak 3B model türü. Bir seçenek seçildiğinde ilgili ek parametreler görünür hale gelir. |
| `generate_type.pbr` | BOOLEAN | Hayır | - | Fiziksel Tabanlı Renderlama (PBR) malzeme oluşturmayı etkinleştirir. Bu parametre yalnızca `generate_type` "Normal" veya "LowPoly" olarak ayarlandığında görünür (varsayılan: Yanlış). |
| `generate_type.polygon_type` | COMBO | Hayır | `"triangle"`<br>`"quadrilateral"` | Ağ için kullanılacak çokgen türü. Bu parametre yalnızca `generate_type` "LowPoly" olarak ayarlandığında görünür. |
| `seed` | INT | Evet | 0 - 2147483647 | Oluşturma işlemi için bir tohum değeri. Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). |

**Not:** Tüm giriş görüntüleri minimum 128 piksel genişliğe ve yüksekliğe sahip olmalıdır. Görüntüler, en uzun kenarları 4900 pikseli aşarsa otomatik olarak küçültülür.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_file` | STRING | Geriye dönük uyumluluk için eski bir çıktı. |
| `GLB` | FILE3DGLB | Oluşturulan 3B modelin GLB (İkili GL İletim Formatı) dosya formatındaki hali. |
| `OBJ` | FILE3DOBJ | Oluşturulan 3B modelin OBJ (Wavefront) dosya formatındaki hali. |
| `texture_image` | IMAGE | Oluşturulan 3B model için doku görüntüsü. |
| `optional_metallic` | IMAGE | PBR malzemeler için metalik haritası. Mevcut değilse siyah bir görüntü döndürür. |
| `optional_normal` | IMAGE | PBR malzemeler için normal haritası. Mevcut değilse siyah bir görüntü döndürür. |
| `optional_roughness` | IMAGE | PBR malzemeler için pürüzlülük haritası. Mevcut değilse siyah bir görüntü döndürür. |

---
**Source fingerprint (SHA-256):** `56ac9e55bd9bb3a5c7c46c2de1ea06921cf41c0971471f6d0b64166722705e4d`
