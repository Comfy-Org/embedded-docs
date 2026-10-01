# Flux 3 Image

Flux 3 Image, bir istemden FLUX 3 ile görsel üretir veya referans görselleri düzenleyip birleştirir. Ne istediğinizi bir talimat olarak yazın, ardından en fazla 10 referans görsel bağlayın ve istemde bunlara image 1, image 2 vb. olarak başvurun. İstem, üretimden önce yorumlanır ve genişletilir; sonuç, seçtiğiniz en-boy oranı ve çözünürlükte oluşturulur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Ne üretileceği veya yapılacak düzenleme. İstem, üretimden önce yorumlanır ve genişletilir. Bağlı referans görsellere image 1, image 2 vb. olarak başvurun. (varsayılan: "") | STRING | Evet | 1 ile 15000 karakter |
| `images` | Referans görseller için büyütülebilir yuva; toplamda en fazla 10 tane bağlayın. Her görsel en az 256x256 piksel olmalıdır ve en-boy oranı 64:1'den daha uç olamaz. | IMAGE | Hayır | 0 ile 10 görsel |
| `bounding_boxes` | Çıktıda nesneleri veya metni yerleştiren Create Bounding Boxes düğümünden isteğe bağlı kutular. Konumlar tuvale göredir; bu nedenle düğüme çıktının en-boy oranını verin. | ARRAY | Hayır | - |
| `aspect_ratio` | Üretilen görselin en-boy oranı. "auto" ilk referans görseli izler veya istemden bir oran seçer. (varsayılan: "auto") | COMBO | Evet | `"auto"`<br>`"21:9"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"7:5"`<br>`"4:3"`<br>`"5:4"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"5:7"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"9:21"` |
| `resolution` | Seçilen en-boy oranındaki çıktı boyutu: 0.75K yaklaşık 0,6 megapiksel, 1K 1 MP, 1.5K 2,4 MP, 2K 4,2 MP, 4K 16,8 MP. (varsayılan: "2K") | COMBO | Evet | `"0.75K"`<br>`"1K"`<br>`"1.5K"`<br>`"2K"`<br>`"4K"` |
| `grounding` | Modelin, üretimden önce istemi web ve görsel aramasıyla araştırmasına izin verin. (varsayılan: True) | BOOLEAN | Evet | True<br>False |
| `safety_tolerance` | Moderasyon toleransı; 0 en katıdır. (varsayılan: 4) | INT | Evet | 0 ile 4 |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum; FLUX 3 kendi tohumunu seçer, bu nedenle gerçek sonuçlar bu değerden bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ile 4294967295 |

`safety_tolerance` gelişmiş bir girdidir ve `seed`, arayüzde Control After Generate kontrollerini içerir.

Referans görseller, istek gönderilmeden önce yüklenir. Tek bir yuva bir toplu iş taşıyabilir ve her toplu işin her karesi 10 görsel sınırına sayılır.

`bounding_boxes` satırları isteme eklenir; bu nedenle istem ve kutu açıklamaları birlikte 15000 karakter veya daha az olmalıdır.

Görüntülenen fiyat `resolution` değerine bağlıdır: 0.75K için $0.05863, 1K için $0.06864, 1.5K için $0.1001, 2K için $0.143 ve 4K için $0.86801.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | FLUX 3 sonucundan indirilen üretilmiş görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `f32a90887227f9ce9e6ed04a76cde452a70f36fb97d8c36d7c55140855c1f593`
