# Mesh Dokusunu Görüntüye Dönüştür

Bu düğüm, bir mesh'in pişirilmiş dokularını çıkarır ve bunları ayrı görüntüler olarak döndürür: temel renk, metalik, pürüzlülük, ortam örtmesi ve normal haritası. Pişirilmemiş doku kanalları nötr varsayılan değerlerle geri döner — ortam örtmesi için beyaz, normal haritası için düz mavi.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Pişirilmiş dokuları çıkarılacak mesh. Mesh'in bir temel renk dokusu olmalıdır; yalnızca vertex renklerine sahip olan mesh'ler (örneğin bir PaintMesh düğümünden sonra) doku içermez ve hataya neden olur. | MESH | Evet | — |

Not: Mesh'in pişirilmiş bir temel renk dokusu olmalıdır. Yoksa düğüm hata verir ve önce BakeTextureFromVoxel çalıştırmanızı önerir. Metalik-pürüzlülük dokusu eksik olduğunda `metallic` ve `roughness` çıktıları siyahtır (0). `occlusion` çıktısı, mesh pişirilmiş ortam örtmesi içermediği sürece beyazdır (mesh'in occlusion-in-metallic-roughness bayrağı ayarlanmış olduğunda). Hiç normal haritası pişirilmediğinde `normal_map` çıktısı düz nötr mavidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `base_color` | Mesh'in temel renk dokusu, görüntü olarak. | IMAGE |
| `metallic` | Mesh'in ortam örtmesi-pürüzlülük-metalik dokusundaki metalik kanalı, gri tonlamalı görüntü olarak. Siyah (0) metalik olmadığını, beyaz (1) tamamen metalik olduğunu gösterir. Doku eksik olduğunda siyahtır. | IMAGE |
| `roughness` | Mesh'in ortam örtmesi-pürüzlülük-metalik dokusundaki pürüzlülük kanalı, gri tonlamalı görüntü olarak. Doku eksik olduğunda siyahtır. | IMAGE |
| `occlusion` | Mesh'in ortam örtmesi-pürüzlülük-metalik dokusundaki ortam örtmesi kanalı, gri tonlamalı görüntü olarak. Ortam örtmesi pişirilmediğinde beyazdır (örtme yok). | IMAGE |
| `normal_map` | Mesh'in normal haritası dokusu. Hiç normal haritası pişirilmediğinde düz nötr bir normal haritasıdır (0.5, 0.5, 1.0; düz mavi görünür). | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshTextureToImage/tr.md)

---
**Source fingerprint (SHA-256):** `775fd50601ed9ebfc48abf1832c58acbac0f48b5faaebb5f7f46ae4a501278c4`
