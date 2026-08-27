# BakeAmbientOcclusion

Yüksek çözünürlüklü (high-poly) bir ağdan, düşük çözünürlüklü (low-poly) bir ağın UV düzenine ortam ışığı engelleme (ambient-occlusion) haritası üretir. Çıktı, beyaz teksellerin açık, koyu teksellerin çatlak/yarık olduğu gri tonlamalı bir görüntüdür; bu görüntü, Apply Texture To Mesh düğümünün occlusion girdisi için tasarlanmıştır. UV açılmış low-poly ağı ve onun türetildiği high-poly ağı bağlayın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Range |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | Üzerine kaplama yapılacak UV açılmış low-poly ağ. UV koordinatlarına sahip olmalıdır; eksikse düğüm bir hata verir. | MESH | Evet | - |
| `high_poly` | Low-poly ağın türetildiği high-poly ağ; ortam ışığı engelleme için kaynak geometri olarak kullanılır. | MESH | Evet | - |
| `resolution` | Piksel cinsinden doku çözünürlüğü; her teksel bir ortam ışığı engelleme değeri alır. Varsayılan: 1024. | INT | Evet | 64 ile 8192 (step 64) |
| `samples` | Teksel başına ışın sayısı. Daha fazlası = daha pürüzsüz, daha yavaş. Grenli görüntü varsa artırın. Varsayılan: 64. | INT | Evet | 4 ile 1024 (step 4) |
| `max_distance` | Sınırlama kutusu köşegeninin oranı olarak ışın uzunluğu. Daha küçük = daha sıkı, daha yerel ortam ışığı engelleme. Varsayılan: 0.5. | FLOAT | Evet | 0.01 ile 2.0 (step 0.01) |
| `strength` | Ortam ışığı engellemeyi ölçekler. >1 koyulaştırır, <1 açıklaştırır. Varsayılan: 1.0. | FLOAT | Evet | 0.0 ile 2.0 (step 0.05) |
| `bias` | Işın başlangıç noktasının yüzeyden kaldırma miktarı, sınırlama kutusu köşegeninin oranı olarak. Düz yüzeylerde koyu lekeler/delikler görünüyorsa artırın. Varsayılan: 0.01. | FLOAT | Evet | 0.0001 ile 0.2 (step 0.0005) |

Not: `low_poly` UV koordinatlarına sahip olmalıdır — bu düğüm ağı asla UV açmaz. `high_poly` yalnızca bir batch öğesi içeriyorsa, `low_poly`'nin her batch öğesi için yeniden kullanılır; yüzü olmayan `low_poly` batch öğeleri atlanır ve bir uyarı günlüğe kaydedilerek yerine tamamen beyaz bir görüntü konur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `occlusion` | Değerleri [0,1] aralığında olan gri tonlamalı ortam ışığı engelleme görüntüsü (beyaz = açık, koyu = çatlak/yarık); `low_poly`'nin her batch öğesi için bir görüntü. Apply Texture To Mesh düğümünün occlusion girdisi için tasarlanmıştır (ORM haritası / occlusionTexture içinde paketlenir). | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeAmbientOcclusion/tr.md)

---
**Source fingerprint (SHA-256):** `63ea6ce5289728d351fdd7d722e9a299ebb1283e1128262a817466ec6d23786a`
