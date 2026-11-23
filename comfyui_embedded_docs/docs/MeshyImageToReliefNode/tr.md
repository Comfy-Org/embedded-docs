# Meshy: Image to Relief

Bu düğüm, bir fotoğrafı 3D baskı, lazer gravür ve CNC oyma için bas-rölyef modeline ve 16-bit derinlik haritasına dönüştürür. Açık arka plan üzerindeki koyu sanat eserleri yükseltilir, açık alanlar alçak kalır. Yalnızca bağladığınız çıktılar oluşturulur ve indirilir; bu nedenle hiçbir model çıktısı bağlı değilken görev yalnızca derinlik haritasını döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `image` | Rölyefe dönüştürülecek fotoğraf. Açık arka plan üzerindeki koyu sanat eserleri yükseltilir. Yüklemeden önce saydamlık atılır; bu nedenle saydam bir logoyu önce beyaz bir arka plan üzerine düzleştirin. | IMAGE | Evet | Tek görüntü |
| `relief_type` | Oyma ön ayarı. `"low"` lazer gravür, CNC işleri ve plaketler için sığ bir oymadır; `"high"` 3D baskılı parçalar için daha derindir. Ön ayar, `carving_depth_mm` değerini seçer. | DYNAMIC_COMBO | Evet | `"low"`<br>`"high"` |
| `carving_depth_mm` | Oymanın milimetre cinsinden derinliği. `relief_type` ayarlandığında kullanılabilir (varsayılan: `"low"` için 3.0, `"high"` için 6.0). | FLOAT | Evet | 0.1 ile 60.0 arası (adım: 0.1) |
| `size_mm` | Model üzerindeki fotoğrafın uzun kenarının milimetre cinsinden uzunluğu; herhangi bir bükmeden önce düz olarak ölçülür (varsayılan: 60.0). | FLOAT | Evet | 20.0 ile 250.0 arası (adım: 1.0) |
| `carving_mode` | `"emboss"` fotoğrafın daha yakın kısımlarını yükseltir, `"engrave"` ise onları içe doğru oyar. | COMBO | Evet | `"emboss"`<br>`"engrave"` |
| `base` | `"plate"` rölyefin altında bir taban plakası tutar, `"none"` arka planı kesip atar ve plaka oluşturmaz. Bir seçenek seçildiğinde ilgili parametresi görünür. | DYNAMIC_COMBO | Evet | `"plate"`<br>`"none"` |
| `base_thickness_mm` | Taban plakasının milimetre cinsinden kalınlığı. `base` `"plate"` olduğunda kullanılabilir (varsayılan: 1.0). | FLOAT | Evet | 0.1 ile 10.0 arası (adım: 0.1) |
| `removal_threshold` | 0 ile 1 arasındaki derinlik haritasında, arka planın kesilip atıldığı eşik derinliği. 0.3 bir büstü bütün olarak korur, 0.8 onu parçalara ayırır. `base` `"none"` olduğunda kullanılabilir (varsayılan: 0.01). | FLOAT | Evet | 0.01 ile 1.0 arası (adım: 0.01) |
| `bend` | `"convex"` ön yüzü dışa doğru şişirir, `"concave"` içe doğru kıvırır, `"off"` rölyefi düz tutar. Bir bükme seçildiğinde `bend_axis` ve `bend_angle` görünür. | DYNAMIC_COMBO | Evet | `"off"`<br>`"convex"`<br>`"concave"` |
| `bend_axis` | `"xz"` sol ve sağ kenarları kıvırır, `"yz"` üst ve alt kenarları. `bend` `"convex"` veya `"concave"` olduğunda kullanılabilir. | COMBO | Evet | `"xz"`<br>`"yz"` |
| `bend_angle` | Bükmenin derece cinsinden kapsadığı yay; 360, rölyefi silindir haline getirir. `bend` `"convex"` veya `"concave"` olduğunda kullanılabilir (varsayılan: 60.0). | FLOAT | Evet | 1.0 ile 360.0 arası (adım: 1.0) |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını kontrol eden tohum; sonuç, tohumdan bağımsız olarak deterministik değildir. Son çalıştırmadan sonra bağlanan bir çıktıyı istemek için değiştirin (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |
| `mesh_resolution` | Fotoğrafın uzun kenarı boyunca ağ noktaları. 1024'te GLB yaklaşık 50 MB, STL yaklaşık 105 MB; 2048'de yaklaşık 200 MB ve 420 MB olur; bir bükme bunları ikiye katlar. (varsayılan: 1024; gelişmiş seçenek) | INT | Evet | 512 ile 2048 arası |
| `color_mapping` | GLB, OBJ, FBX ve USDZ dosyalarını fotoğrafla renklendirir. STL ve 3MF beyaz kalır. (varsayılan: False; gelişmiş seçenek) | BOOLEAN | Evet | True / False |

**Not:** Bir model formatı yalnızca çıktısı bağlandığında oluşturulur ve indirilir. Hiçbir model çıktısı bağlı değilken görev yalnızca derinlik haritasını döndürür; yalnızca `preview` bağlıyken küçük resim için model yine oluşturulur ancak model dosyası döndürülmez. `depth_map` tam 16-bit aralığını korur; Save Image (Advanced) onu 16-bit PNG olarak yazar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `GLB` | GLB formatında indirilen rölyef modeli. | FILE3DGLB |
| `STL` | STL formatında indirilen rölyef modeli. | FILE3DSTL |
| `OBJ` | OBJ formatında indirilen rölyef modeli. | FILE3DOBJ |
| `FBX` | FBX formatında indirilen rölyef modeli. | FILE3DFBX |
| `USDZ` | USDZ formatında indirilen rölyef modeli. | FILE3DUSDZ |
| `3MF` | 3MF formatında indirilen rölyef modeli. | FILE3D |
| `depth_map` | Tam 16-bit aralığına sahip derinlik haritası; Save Image (Advanced) onu 16-bit PNG olarak yazar. | IMAGE |
| `preview` | Tamamlanan rölyef için Meshy tarafından oluşturulan küçük resim. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToReliefNode/tr.md)

---
**Source fingerprint (SHA-256):** `6f2f0eb49074281b99d7ee10daf3bcc5616c6596c1c4d8491c72739550395f52`
