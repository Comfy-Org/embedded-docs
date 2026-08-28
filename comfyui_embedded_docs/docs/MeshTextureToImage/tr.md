# MeshTextureToImage

Bu düğüm, bir mesh'in bake edilmiş dokularını çıkarır ve bunları ayrı görüntüler olarak döndürür: temel renk, metalik, pürüzlülük, occlusion ve normal haritası. Bake edilmemiş doku kanalları nötr varsayılan değerlerle döner — occlusion için beyaz ve normal haritası için düz mavi.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Bake edilmiş dokuları çıkarılacak mesh. Mesh, temel renk dokusuna sahip olmalıdır; yalnızca vertex renklerine sahip olan mesh'ler (örneğin bir PaintMesh düğümünden sonra) doku içermez ve hataya neden olur. | MESH | Evet | — |

Not: Mesh, bake edilmiş bir temel renk dokusuna sahip olmalıdır. Aksi takdirde düğüm hata verir ve önce BakeTextureFromVoxel çalıştırılmasını önerir. metallic-roughness dokusu eksik olduğunda `metallic` ve `roughness` çıktıları siyah (0) olur. `occlusion` çıktısı, mesh bake edilmiş ambient occlusion içermediği sürece beyazdır. `normal_map` çıktısı, normal haritası bake edilmediğinde düz nötr mavidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `base_color` | Mesh'in temel renk dokusunun görüntüsü. | IMAGE |
| `metallic` | Mesh'in occlusion-roughness-metallic dokusundan metalik kanalı; gri tonlamalı bir görüntü olarak. Siyah (0) metalik değil anlamına gelir, beyaz (1) tamamen metalik anlamına gelir. Doku eksik olduğunda siyahtır. | IMAGE |
| `roughness` | Mesh'in occlusion-roughness-metallic dokusundan pürüzlülük kanalı; gri tonlamalı bir görüntü olarak. Doku eksik olduğunda siyahtır. | IMAGE |
| `occlusion` | Mesh'in occlusion-roughness-metallic dokusundan ambient occlusion kanalı; gri tonlamalı bir görüntü olarak. Ambient occlusion bake edilmediğinde beyazdır (occlusion yok). | IMAGE |
| `normal_map` | Mesh'in normal haritası dokusu. Normal haritası bake edilmediğinde düz nötr normal haritası (0.5, 0.5, 1.0; düz mavi olarak görünür). | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshTextureToImage/tr.md)

---
**Source fingerprint (SHA-256):** `775fd50601ed9ebfc48abf1832c58acbac0f48b5faaebb5f7f46ae4a501278c4`
