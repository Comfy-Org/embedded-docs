# HitPaw Genel Görüntü İyileştirme

Bu düğüm, düşük çözünürlüklü görüntüleri artefaktları ve gürültüyü gidererek süper çözünürlüğe ölçeklendirir. İşlenmesi için görüntüyü harici bir API'ye gönderir ve izin verilen çıktı sınırı içinde kalmak için girdi boyutunu otomatik olarak ayarlayabilir. İzin verilen en büyük çıktı boyutu 32 megapikseldir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak iyileştirme modeli. `generative_portrait` modeli portreler için optimize edilmiştir, `generative` ise genel amaçlı bir modeldir. | COMBO | Evet | `"generative_portrait"`<br>`"generative"` |
| `image` | İyileştirilecek girdi görüntüsü. | IMAGE | Evet | - |
| `upscale_factor` | Görüntünün boyutlarının ölçeklendirileceği faktör. 1 değeri ölçeklendirme olmadığı anlamına gelir, 2 boyutları ikiye katlar ve 4 boyutları dörde katlar. | COMBO | Evet | `1`<br>`2`<br>`4` |
| `auto_downscale` | Çıktı sınırı aşacaksa girdi görüntüsünü otomatik olarak küçültür. (varsayılan: `False`) | BOOLEAN | Hayır | - |

**Not:** Hesaplanan çıktı boyutu (girdi genişliği × `upscale_factor` × girdi yüksekliği × `upscale_factor`) 32.000.000 pikseli (32MP) aşarsa ve `auto_downscale` devre dışıysa düğüm bir hata verir. `auto_downscale` etkinleştirildiğinde, düğüm çıktının 32MP sınırına sığması için girdi görüntüsü boyutunu veya ölçekleme faktörünü (ya da her ikisini) otomatik olarak azaltır. Seçilen `model` ve `upscale_factor`, hizmete gönderilen model adında birleştirilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | İyileştirilmiş ve ölçeklendirilmiş çıktı görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/tr.md)

---
**Source fingerprint (SHA-256):** `eb9adc1ac94c5fb943e3dd8f6617b21c5d3203f0d9ddb93ba1c9d4b4e63bd421`
