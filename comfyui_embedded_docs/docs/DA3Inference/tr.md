# Run Depth Anything 3

Bu düğüm, bir görüntü üzerinde Depth Anything 3 modelini çalıştırarak derinlik ve geometri bilgilerini tahmin eder. Çoklu görünüm modunda, birden fazla görüntü aynı sahnenin farklı görünümleri olarak birlikte işlenir ve geometrik olarak tutarlı derinlik haritaları ile kamera konumları üretilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `da3_model` | Çıkarım için kullanılacak Depth Anything 3 modeli | DA3_MODEL | Evet | - |
| `image` | İşlenecek giriş görüntüsü veya görüntüleri | IMAGE | Evet | - |
| `resolution` | Modelin çalıştığı çözünürlük (en uzun kenar, 14'ün katı). Düşük değerler daha hızlıdır ve daha az VRAM kullanır. Yüksek değerler daha fazla ayrıntı üretir. Çıktı, orijinal boyuta yükseltilir (varsayılan: 504) | INT | Evet | 140 ila 2520 (adım: 14) |
| `resize_method` | upper_bound_resize: en uzun kenar çözünürlüğe eşit olacak şekilde ölçekler (belleği sınırlar, varsayılan). lower_bound_resize: en kısa kenar çözünürlüğe eşit olacak şekilde ölçekler (uzun/geniş görüntülerde daha fazla ayrıntı korur, daha fazla bellek kullanır) | COMBO | Evet | `"upper_bound_resize"`<br>`"lower_bound_resize"` |
| `mode` | mono: tek görünümlü görüntü işleme (herhangi bir model çeşidiyle çalışır). multiview: tüm görüntüler geometrik tutarlılık ve kamera konumu tahmini için birlikte işlenir (yalnızca Small ve Base modeller için) | COMBO | Evet | `"mono"`<br>`"multiview"` |
| `ref_view_strategy` | Çoklu görünüm modunda hangi görünümün geometrik çapa olarak işlev göreceği. saddle_balanced: diğerlerine en yakın ortalama görünüm (en iyi genel seçenek). saddle_sim_range: diğerlerinden en farklı görsel görünüm. first / middle: sabit sıralı seçimler | COMBO | Hayır (koşullu) | `"saddle_balanced"`<br>`"saddle_sim_range"`<br>`"first"`<br>`"middle"` |
| `pose_method` | Kamera görüş alanının nasıl tahmin edileceği (yalnızca Small ve Base modeller için). cam_dec: görüntü özelliklerinden öğrenilir. ray_pose: modelin 3D ışın çıktısından geometrik olarak türetilir. 3D çıktının perspektif doğruluğunu etkiler | COMBO | Hayır (koşullu) | `"cam_dec"`<br>`"ray_pose"` |

**Parametre kısıtlamaları hakkında notlar:**
- `ref_view_strategy` ve `pose_method` parametreleri yalnızca `mode` değeri `"multiview"` olarak ayarlandığında kullanılabilir
- Çoklu görünüm modu, Small veya Base model çeşidi gerektirir. Diğer başlık türlerine sahip modeller (Metric veya Mono gibi) çapraz görünüm dikkati veya kamera konumu tahminini desteklemez
- `pose_method` değeri `"cam_dec"` olarak ayarlandığında, modelin bir kamera kod çözücüsü olmalıdır. `"ray_pose"` olarak ayarlandığında, modelin bir DualDPT başlığı olmalıdır
- Seçilen `pose_method` yüklenen modelle uyumlu değilse, bir hata oluşturulur

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `da3_geometry` | Normalleştirilmemiş tensörler sözlüğü. Her zaman şu anahtarları içerir: depth, image, mode. İsteğe bağlı anahtarlar şunları içerir: sky (Mono/Metric modeller için), confidence (Small/Base modeller için), extrinsics ve intrinsics (çoklu görünüm modu için) | DA3_GEOMETRY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3Inference/tr.md)

---
**Source fingerprint (SHA-256):** `e91dd47e6a01719cdd6b6ce8a9bcc45933cac72c5e147ac42906d2f83ab7c250`
