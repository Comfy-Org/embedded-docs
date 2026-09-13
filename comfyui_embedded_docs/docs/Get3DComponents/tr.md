# 3D Bileşenlerini Al

Get3DComponents, bir 3D model dosyasını (GLB, GLTF, OBJ veya STL) decimate, remesh, UV unwrap ve bake gibi mesh işleme düğümleri tarafından kullanılabilen düzenlenebilir bir mesh'e ayrıştırır. Tüm sahne düğümleri ve ilkelleri, dönüşümleri uygulanmış olarak tek bir mesh'te birleştirilir; dokular ve materyal ayarları ilk materyalden alınır. MeshToFile3D düğümünün karşılığıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Load 3D veya başka bir 3D düğümünden 3D model dosyası. FBX/USDZ desteklenmez - önce GLB'ye dönüştürün. | File3DGLB<br>File3DGLTF<br>File3DOBJ<br>File3DSTL<br>File3DAny | Evet | GLB<br>GLTF<br>OBJ<br>STL |

Not: FBX ve USDZ dosyaları desteklenmez ve hata oluşturur; önce bunları GLB veya GLTF'ye dönüştürün. Dosya biçimi GLB, GLTF, OBJ veya STL olarak tanınamazsa, düğüm desteklenen biçimleri listeleyen bir hata verir. glTF sahnesi hiç üçgen geometri içermiyorsa veya dosya, vertex listesinin dışına işaret eden yüz indeksleri içeriyorsa (bozuk bir dosya işareti), düğüm bir hata verir. 3D dosyası birden fazla materyal içeriyorsa, yalnızca ilk materyalin dokuları ve materyal faktörleri korunur (bir uyarı günlüğe kaydedilir). Tüm sahne ilkelleri, dönüşümleri uygulanmış olarak tek bir mesh'te birleştirilir. Bu düğüm deneyseldir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Dosyadan alınan materyal bilgileriyle (doku, metalik-pürüzlülük, normal haritası, emissive renk, unlit bayrağı, metalik-pürüzlülük içinde occlusion bayrağı ve materyal verisi) birlikte vertex'ler, yüzler, UV'ler, vertex renkleri, normaller ve teğetleri içeren düzenlenebilir mesh. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Get3DComponents/tr.md)

---
**Source fingerprint (SHA-256):** `f2cdc9767a50503988484f09d2b3d110caf086b8cd84f65034a4a1e17a94405e`
