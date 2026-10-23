# Ideogram Vector Image to SVG

Bu düğüm, bir görüntüyü Ideogram Vector ile düzenlenebilir SVG'ye dönüştürür. Sonuç, raster görüntü yerine vektör işaretlemesidir; bu nedenle izlenen şekiller bir vektör düzenleyicide düzenlenebilir kalır. Alfa kanalına sahip bir görüntünün saydam alanları saydam kalır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. Varsayılan: `"ideogram-vector-1"`. | DYNAMIC_COMBO | Evet | `"ideogram-vector-1"` |
| `image` | Dönüştürülecek görüntü. Toplu girdi, her görüntü tek tek dönüştürülerek işlenir ve elde edilen SVG'ler birlikte döndürülür. | IMAGE | Evet | - |
| `mode` | `"simple"` daha az ve daha büyük şekiller izler; `"default"` daha ince ayrıntıları korur. Varsayılan: `"default"`. | COMBO | Evet | `"simple"`<br>`"default"` |

**Kısıtlamalar:**

* En uzun kenarı 2048 pikselin üzerinde olan görüntüler, yüklemeden önce ölçeklendirilerek küçültülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `SVG` | Dönüştürülen görüntü, düzenlenebilir vektör işaretlemesi olarak. | SVG |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramVectorImageToSVGApi/tr.md)

---
**Source fingerprint (SHA-256):** `6553291e9d887b31485b9cbf8f6ced4186470eb47e8621ebb0f4e5df6542123e`
