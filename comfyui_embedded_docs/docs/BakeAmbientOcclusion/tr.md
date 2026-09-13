# Ortam Tıkanıklığını İşle

Yüksek poligonlu bir ağdan düşük poligonlu bir ağın UV düzenine ortam kapanması (ambient occlusion) haritası pişirir. Çıktı, beyaz texel'lerin açık, koyu texel'lerin çatlaklarda olduğu gri tonlamalı bir görüntüdür; Apply Texture To Mesh düğümünün occlusion girdisi için tasarlanmıştır. UV'si açılmış düşük poligonlu ağı ve ondan decimate edildiği yüksek poligonlu ağı bağlayın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | İçine pişirme yapılacak UV'si açılmış düşük poligonlu ağ. UV'lere sahip olmalıdır; eksikse düğüm hata verir. | MESH | Evet | - |
| `high_poly` | Düşük poligonlu ağın decimate edildiği, kapanma için kaynak geometri olarak kullanılan yüksek poligonlu ağ. | MESH | Evet | - |
| `resolution` | Piksel cinsinden doku çözünürlüğü; her texel bir kapanma değeri alır. Varsayılan: 1024. | INT | Evet | 64 ile 8192 (adım: 64) |
| `samples` | Texel başına ışın sayısı. Daha fazlası = daha yumuşak, daha yavaş. Grenliyse artırın. Varsayılan: 64. | INT | Evet | 4 ile 1024 (adım: 4) |
| `max_distance` | Işın uzunluğu, sınırlayıcı kutu köşegeninin bir kesri olarak. Daha küçük = daha sıkı, daha yerel kapanma. Varsayılan: 0.5. | FLOAT | Evet | 0.01 ile 2.0 (adım: 0.01) |
| `strength` | Kapanmayı ölçekler. >1 koyulaştırır, <1 aydınlatır. Varsayılan: 1.0. | FLOAT | Evet | 0.0 ile 2.0 (adım: 0.05) |
| `bias` | Işın başlangıcının yüzeyden yukarı kaldırılması, sınırlayıcı kutu köşegeninin bir kesri olarak. Düz yüzeylerde bile koyu lekeler/delikler görünüyorsa artırın. Varsayılan: 0.01. | FLOAT | Evet | 0.0001 ile 0.2 (adım: 0.0005) |

Not: `low_poly` UV koordinatlarına sahip olmalıdır — bu düğüm ağı asla UV açmaz. `high_poly` yalnızca bir toplu iş öğesi içeriyorsa, `low_poly` toplu iş öğelerinin her biri için yeniden kullanılır; yüz içermeyen `low_poly` toplu iş öğeleri atlanır ve tamamen beyaz bir görüntüyle değiştirilir; bir uyarı günlüğe kaydedilir. `low_poly` UV'leri 0-1 aralığının dışına taşarsa, bunlar eşit şekilde bu aralığa geri sığdırılır ve döşemeli/UDIM tarzı bir düzen algılandığında bir uyarı günlüğe kaydedilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `occlusion` | Değerleri [0,1] aralığında olan gri tonlamalı ortam kapanması görüntüsü (beyaz = açık, koyu = çatlaklar), `low_poly` toplu iş öğelerinin her biri için bir görüntü. Apply Texture To Mesh düğümünün occlusion girdisi için tasarlanmıştır (ORM haritasına / occlusionTexture'a paketlenir). | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeAmbientOcclusion/tr.md)

---
**Source fingerprint (SHA-256):** `63ea6ce5289728d351fdd7d722e9a299ebb1283e1128262a817466ec6d23786a`
