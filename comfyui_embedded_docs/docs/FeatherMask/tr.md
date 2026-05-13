> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FeatherMask/tr.md)

`FeatherMask` düğümü, belirtilen bir maskenin kenarlarına yumuşatma efekti uygulayarak, maskenin kenarlarını her bir kenardan belirtilen mesafelere göre opaklıklarını ayarlayarak kademeli olarak geçiş yapar. Bu, daha yumuşak ve daha harmanlanmış bir kenar efekti oluşturur.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|--------------|-------------|
| `mask`    | MASK         | Yumuşatma efektinin uygulanacağı maske. Yumuşatmadan etkilenecek görüntü alanını belirler. |
| `left`    | INT          | Yumuşatma efektinin uygulanacağı sol kenardan olan mesafeyi belirtir. |
| `top`     | INT          | Yumuşatma efektinin uygulanacağı üst kenardan olan mesafeyi belirtir. |
| `right`   | INT          | Yumuşatma efektinin uygulanacağı sağ kenardan olan mesafeyi belirtir. |
| `bottom`  | INT          | Yumuşatma efektinin uygulanacağı alt kenardan olan mesafeyi belirtir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|--------------|-------------|
| `mask`    | MASK         | Çıktı, kenarlarına yumuşatma efekti uygulanmış, giriş maskesinin değiştirilmiş bir sürümüdür. |