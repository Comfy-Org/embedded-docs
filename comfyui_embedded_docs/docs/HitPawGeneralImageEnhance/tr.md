# HitPaw Genel Görüntü İyileştirme

Bu düğüm, düşük çözünürlüklü görüntüleri süper çözünürlüğe yükselterek iyileştirir, artefaktları ve gürültüyü giderir. Görüntüyü işlemek için harici bir API kullanır ve işleme sınırları içinde kalmak için girdi boyutunu otomatik olarak ayarlayabilir. İzin verilen maksimum çıktı boyutu 32 megapikseldir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak iyileştirme modeli. `generative_portrait` modeli portreler için optimize edilmiştir, `generative` ise genel amaçlı bir modeldir. | COMBO | Evet | `"generative_portrait"`<br>`"generative"` |
| `görüntü` | İyileştirilecek girdi görüntüsü. | IMAGE | Evet | - |
| `büyütme_oranı` | Görüntünün boyutlarının yükseltilme faktörü. 1 faktörü yükseltme yapılmayacağı anlamına gelir, 2 boyutları iki katına, 4 ise dört katına çıkarır. | COMBO | Evet | `1`<br>`2`<br>`4` |
| `otomatik_küçültme` | Çıktı sınırı aşarsa girdi görüntüsünü otomatik olarak küçültür. (varsayılan: `False`) | BOOLEAN | Hayır | - |

**Not:** Hesaplanan çıktı boyutu (girdi genişliği × upscale_factor × girdi yüksekliği × upscale_factor) 32.000.000 pikseli (32MP) aşarsa ve `auto_downscale` devre dışıysa düğüm bir hata verir. `auto_downscale` etkinleştirildiğinde düğüm, çıktı 32MP sınırına sığacak şekilde girdi görüntüsünün boyutunu veya upscale_factor değerini (ya da her ikisini) otomatik olarak azaltır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | İyileştirilmiş ve yükseltilmiş çıktı görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/tr.md)

---
**Source fingerprint (SHA-256):** `eb9adc1ac94c5fb943e3dd8f6617b21c5d3203f0d9ddb93ba1c9d4b4e63bd421`
