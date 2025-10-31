> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FeatherMask/tr.md)

`FeatherMask` düğümü, verilen bir maskenin kenarlarına tüylendirme efekti uygular, her kenardan belirtilen mesafelere göre opaklıklarını ayarlayarak maskenin kenarlarını yumuşak bir şekilde geçiş yaptırır. Bu, daha yumuşak, daha harmanlanmış bir kenar efekti oluşturur.

## Girdiler

| Parametre | Veri Tipi | Açıklama |
|-----------|-----------|-------------|
| `mask`    | MASK      | Tüylendirme efektinin uygulanacağı maske. Tüylendirmenin etkileyeceği görüntü alanını belirler. |
| `left`    | INT       | Tüylendirme efektinin uygulanacağı sol kenardan itibaren olan mesafeyi belirtir. |
| `top`     | INT       | Tüylendirme efektinin uygulanacağı üst kenardan itibaren olan mesafeyi belirtir. |
| `right`   | INT       | Tüylendirme efektinin uygulanacağı sağ kenardan itibaren olan mesafeyi belirtir. |
| `bottom`  | INT       | Tüylendirme efektinin uygulanacağı alt kenardan itibaren olan mesafeyi belirtir. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-----------|-------------|
| `mask`    | MASK      | Çıktı, kenarlarına tüylendirme efekti uygulanmış, girdi maskesinin değiştirilmiş bir versiyonudur. |