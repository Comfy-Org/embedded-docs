> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FeatherMask/tr.md)

`FeatherMask` düğümü, belirtilen bir maskenin kenarlarına yumuşatma efekti uygulayarak, maskenin kenarlarını her bir kenardan belirtilen mesafelere göre opaklıklarını ayarlayarak kademeli olarak geçiş yapar. Bu, daha yumuşak ve daha harmanlanmış bir kenar efekti oluşturur.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|--------------|-------------|
| `maske`    | MASK         | Yumuşatma efektinin uygulanacağı maske. Yumuşatmadan etkilenecek görüntü alanını belirler. |
| `sol`    | INT          | Yumuşatma efektinin uygulanacağı sol kenardan olan mesafeyi belirtir. |
| `üst`     | INT          | Yumuşatma efektinin uygulanacağı üst kenardan olan mesafeyi belirtir. |
| `sağ`   | INT          | Yumuşatma efektinin uygulanacağı sağ kenardan olan mesafeyi belirtir. |
| `alt`  | INT          | Yumuşatma efektinin uygulanacağı alt kenardan olan mesafeyi belirtir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|--------------|-------------|
| `maske`    | MASK         | Çıktı, kenarlarına yumuşatma efekti uygulanmış, giriş maskesinin değiştirilmiş bir sürümüdür. |