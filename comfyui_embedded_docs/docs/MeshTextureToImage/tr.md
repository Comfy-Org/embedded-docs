# MeshTextureToImage

Bu düğüm, bir ağın pişirilmiş dokularını çıkarır ve bunları ayrı görüntüler olarak döndürür: temel renk, metalik, pürüzlülük, oklüzyon ve normal haritası. Pişirilmemiş doku kanalları nötr varsayılan değerler olarak gelir — oklüzyon için beyaz ve normal haritası için düz mavi.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Pişirilmiş dokuları çıkarılan ağ. Ağın bir temel renk dokusuna sahip olması gerekir; yalnızca köşe noktası renklerine sahip ağlar (örneğin bir PaintMesh düğümünden sonra) doku içermez ve hataya neden olur. | MESH | Evet | — |

Not: Ağın pişirilmiş bir temel renk dokusuna sahip olması gerekir. Eğer yoksa, düğüm bir hata verir ve önce BakeTextureFromVoxel çalıştırmayı önerir. Metalik-pürüzlülük dokusu eksik olduğunda, `metallic` ve `roughness` çıktıları siyah (0) olur. `occlusion` çıktısı, ağ pişirilmiş ortam oklüzyonu içermediği sürece beyazdır. `normal_map` çıktısı, normal haritası pişirilmediğinde düz nötr mavidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `base_color` | Ağın temel renk dokusu, görüntü olarak. | IMAGE |
| `metallic` | Ağın oklüzyon-pürüzlülük-metalik dokusundaki metalik kanalı, gri tonlamalı görüntü olarak. Siyah (0) metalik olmadığını, beyaz (1) tamamen metalik olduğunu gösterir. Doku eksik olduğunda siyah. | IMAGE |
| `roughness` | Ağın oklüzyon-pürüzlülük-metalik dokusundaki pürüzlülük kanalı, gri tonlamalı görüntü olarak. Doku eksik olduğunda siyah. | IMAGE |
| `occlusion` | Ağın oklüzyon-pürüzlülük-metalik dokusundaki ortam oklüzyonu kanalı, gri tonlamalı görüntü olarak. Ortam oklüzyonu pişirilmediğinde beyaz (oklüzyon yok). | IMAGE |
| `normal_map` | Ağın normal haritası dokusu. Normal haritası pişirilmediğinde düz nötr normal haritası (0.5, 0.5, 1.0, düz mavi olarak görünür). | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshTextureToImage/tr.md)

---
**Source fingerprint (SHA-256):** `775fd50601ed9ebfc48abf1832c58acbac0f48b5faaebb5f7f46ae4a501278c4`
