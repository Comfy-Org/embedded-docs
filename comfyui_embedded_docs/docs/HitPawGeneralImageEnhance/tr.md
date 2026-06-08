Bu düğüm, düşük çözünürlüklü görüntüleri süper çözünürlüğe yükselterek, yapaylıkları ve gürültüyü gidererek iyileştirir. Görüntüyü işlemek için harici bir API kullanır ve işleme sınırları dahilinde kalmak için giriş boyutunu otomatik olarak ayarlayabilir. İzin verilen maksimum çıkış boyutu 4 megapikseldir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak iyileştirme modeli. `generative_portrait` modeli portreler için optimize edilmiştir, `generative` ise genel amaçlı bir modeldir. | STRING | Evet | `"generative_portrait"`<br>`"generative"` |
| `görüntü` | İyileştirilecek giriş görüntüsü. | IMAGE | Evet | - |
| `büyütme_oranı` | Görüntü boyutlarının yükseltileceği faktör. 1 faktörü yükseltme yapılmadığı, 2 boyutları ikiye katladığı ve 4 dört katına çıkardığı anlamına gelir. | INT | Evet | `1`<br>`2`<br>`4` |
| `otomatik_küçültme` | Çıkış sınırı aşılacaksa giriş görüntüsünü otomatik olarak küçültür. Etkinleştirildiğinde, düğüm istenen yükseltme faktörünü uygulamadan önce giriş görüntüsü boyutunu 4 megapiksel çıkış sınırına sığacak şekilde küçültmeye çalışır. (varsayılan: `False`) | BOOLEAN | Hayır | - |

**Not:** Hesaplanan çıkış boyutu (giriş yüksekliği × upscale_factor × giriş genişliği × upscale_factor) 4.000.000 pikseli (4MP) aşarsa ve `auto_downscale` devre dışıysa düğüm bir hata verecektir. `auto_downscale` etkinleştirildiğinde, düğüm istenen yükseltme faktörünü uygulamadan önce giriş görüntüsünü sınıra sığacak şekilde küçültmeye çalışacaktır. 2 kattan fazla küçültme gerekiyorsa, düğüm bunun yerine yükseltme faktörünü azaltacaktır.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | İyileştirilmiş ve yükseltilmiş çıkış görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/tr.md)

---
**Source fingerprint (SHA-256):** `29f927d39777acdfba2aad107027672d281c202ec78e04942e405c2cc64fcee4`
