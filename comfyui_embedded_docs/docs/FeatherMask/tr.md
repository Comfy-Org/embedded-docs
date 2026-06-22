# Maskeyi Yumuşat

`FeatherMask` düğümü, belirtilen bir maskenin kenarlarına yumuşatma efekti uygulayarak, maskenin kenarlarını her bir kenardan belirtilen mesafelere göre opaklıklarını ayarlayarak kademeli olarak geçiş yapar. Bu, daha yumuşak ve daha harmanlanmış bir kenar efekti oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `maske` | Yumuşatma efektinin uygulanacağı maske. Yumuşatmadan etkilenecek görüntü alanını belirler. | MASK |
| `sol` | Yumuşatma efektinin uygulanacağı sol kenardan olan mesafeyi belirtir. | INT |
| `üst` | Yumuşatma efektinin uygulanacağı üst kenardan olan mesafeyi belirtir. | INT |
| `sağ` | Yumuşatma efektinin uygulanacağı sağ kenardan olan mesafeyi belirtir. | INT |
| `alt` | Yumuşatma efektinin uygulanacağı alt kenardan olan mesafeyi belirtir. | INT |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `maske` | Çıktı, kenarlarına yumuşatma efekti uygulanmış, giriş maskesinin değiştirilmiş bir sürümüdür. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FeatherMask/tr.md)
