# BakeAmbientOcclusion

A high-poly mesh'ten düşük poly mesh'in UV yerleşimine bir ambient-occlusion haritası üretir. Çıktı, beyaz teksellerin açık ve koyu teksellerin çatlaklarda olduğu gri tonlamalı bir görüntüdür; Apply Texture To Mesh düğümünün occlusion girişi için tasarlanmıştır. UV açılımı yapılmış düşük poly mesh'i ve ondan sadeleştirilmiş yüksek poly mesh'i bağlayın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | İçine bake yapılacak UV açılımı yapılmış düşük poly mesh. UV koordinatlarına sahip olmalıdır; eksiklerse düğüm hata verir. | MESH | Evet | - |
| `high_poly` | Düşük poly mesh'in sadeleştirildiği yüksek poly mesh; occlusion için kaynak geometri olarak kullanılır. | MESH | Evet | - |
| `resolution` | Piksel cinsinden doku çözünürlüğü; her teksel bir occlusion değeri alır. Varsayılan: 1024. | INT | Evet | 64 ila 8192 (adım 64) |
| `samples` | Teksel başına ışın sayısı. Daha yüksek = daha pürüzsüz, daha yavaş. Grenli görünüyorsa artırın. Varsayılan: 64. | INT | Evet | 4 ila 1024 (adım 4) |
| `max_distance` | Işın uzunluğu, sınırlayıcı kutu köşegeninin bir kesri olarak. Daha küçük = daha sıkı, daha yerel occlusion. Varsayılan: 0.5. | FLOAT | Evet | 0.01 ila 2.0 (adım 0.01) |
| `strength` | Occlusion değerini ölçekler. >1 koyulaştırır, <1 açıklaştırır. Varsayılan: 1.0. | FLOAT | Evet | 0.0 ila 2.0 (adım 0.05) |
| `bias` | Işın başlangıç noktasının yüzeyden kaldırılması, sınırlayıcı kutu köşegeninin bir kesri olarak. Düz yüzeylerde bile koyu lekeler/delikler görünüyorsa artırın. Varsayılan: 0.01. | FLOAT | Evet | 0.0001 ila 0.2 (adım 0.0005) |

Not: `low_poly` UV koordinatlarına sahip olmalıdır — bu düğüm mesh'i asla UV açılımı yapmaz. `high_poly` yalnızca bir batch öğesi içeriyorsa, `low_poly`'nin her batch öğesi için yeniden kullanılır; yüzü olmayan `low_poly` batch öğeleri atlanır ve bir uyarı günlüğe kaydedilerek tamamen beyaz bir görüntüyle değiştirilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `occlusion` | [0,1] aralığında değerlere sahip gri tonlamalı ambient-occlusion görüntüsü (beyaz = açık, koyu = çatlaklar), `low_poly`'nin her batch öğesi için bir görüntü. Apply Texture To Mesh düğümünün occlusion girişi için tasarlanmıştır (ORM haritasına / occlusionTexture'a paketlenir). | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeAmbientOcclusion/tr.md)

---
**Source fingerprint (SHA-256):** `63ea6ce5289728d351fdd7d722e9a299ebb1283e1128262a817466ec6d23786a`
