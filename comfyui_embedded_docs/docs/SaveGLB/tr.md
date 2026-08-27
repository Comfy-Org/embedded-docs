# GLB Kaydet

SaveGLB düğümü, 3B mesh verilerini veya 3B dosya girdilerini çıktı dizinine kaydeder. Mesh verilerini ve yaygın 3B dosya formatlarını (GLB, GLTF, OBJ, FBX, STL, USDZ, PLY, SPLAT, SPZ, KSPLAT) kabul eder ve belirtilen dosya adı önekiyle dışa aktarır. Mesh girdileri, toplu iş öğesi başına bir olacak şekilde GLB dosyaları olarak yazılırken, 3B dosya girdileri orijinal formatında kaydedilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ağ` | Kaydedilecek mesh veya 3B dosya | MESH veya FILE3D | Evet | Mesh data<br>GLB<br>GLTF<br>OBJ<br>FBX<br>STL<br>USDZ<br>PLY<br>SPLAT<br>SPZ<br>KSPLAT<br>Any splat format<br>Any point cloud format<br>Any 3D file format |
| `dosyaadı_öneki` | Çıktı dosya adı için önek (varsayılan: "3d/ComfyUI"). Önek bir alt klasör yolu içerebilir, bu nedenle dosyalar varsayılan olarak çıktı dizininin "3d" alt klasörüne kaydedilir | STRING | Hayır | - |

Not: `mesh` girdisi bir 3B dosya olduğunda, düğüm dosyayı orijinal format uzantısını kullanarak kaydeder (dosyanın formatı yoksa GLB kullanılır). Mesh verisi olduğunda, toplu işteki her öğe ayrı bir `.glb` dosyası olarak kaydedilir; boş öğeler (tepe noktası veya yüzü olmayanlar) bir uyarı ile atlanır. Çıktı dosya adları, artan bir sayaçla `{filename_prefix}_{counter:05}_.{ext}` desenini izler. Meta veri etkinleştirildiğinde, iş akışı meta verileri (istem ve ek PNG bilgisi) kaydedilen dosyalara gömülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `ui` | Kaydedilen 3B dosyaları, dosya adı, alt klasör ve tür bilgisiyle birlikte kullanıcı arayüzünde görüntüler | UI |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/tr.md)

---
**Source fingerprint (SHA-256):** `366b56c4fd6e3c2f7783222990792a982857b3419a2becfa27ddfa37853bb22c`
