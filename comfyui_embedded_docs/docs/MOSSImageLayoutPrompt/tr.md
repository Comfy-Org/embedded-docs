# MOSS-Image Layout Prompt

MOSS-Image'in okuduğu düzen istemini oluşturur. Create Bounding Boxes düğümünde çizilen öğeleri alır ve her kutu için bir girdi içeren bir JSON düzeni üretir: etiketi, altyazısı ve hedef tuvalin piksel uzayındaki dikdörtgeni. `width` ve `height` değerlerini üretmeyi planladığınız görüntünün boyutuna ayarlayın, ardından çıktıyı metin kodlayıcının istem girişine bağlayın. Hiçbir öğe bağlı değilse istem metni değiştirilmeden döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Tüm görüntünün tanımı. Düzenin altyazısı olur. | STRING | Evet | - |
| `element` | Yerleştirilecek öğeler; Create Bounding Boxes düğümünden alınır. Her kutu kendi altyazısını sağlar; metin kutuları ayrıca metinlerini sağlar ve renk paleti taşıyan kutular paletini korur. | ARRAY | Evet | - |
| `width` | Üretilen görüntünün piksel cinsinden genişliği. Kutular bu piksel ızgarasına dönüştürülür; bu nedenle üretmeyi planladığınız görüntünün boyutunu kullanın (varsayılan: 1024). | INT | Evet | 16 ile 16384 arası (adım: 16) |
| `height` | Üretilen görüntünün piksel cinsinden yüksekliği. Kutular bu piksel ızgarasına dönüştürülür; bu nedenle üretmeyi planladığınız görüntünün boyutunu kullanın (varsayılan: 1024). | INT | Evet | 16 ile 16384 arası (adım: 16) |
| `character_boxes` | Nesneler yerine karakter olarak etiketlenecek kutuların numaraları; Create Bounding Boxes önizlemesinde etiketlendiği gibidir, örneğin "1, 3". Dizedeki her sayı okunur, bu nedenle herhangi bir ayırıcı çalışır (varsayılan: boş). | STRING | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `prompt` | Düzen istemi: altyazıyı, her kutu için bir girdiyi ve kutu koordinat biçimini içeren bir JSON nesnesi. Hiçbir öğe bağlı değilken giriş metni olduğu gibi geçirilir. | STRING |

## Notlar

Kutu dikdörtgenleri, Create Bounding Boxes düğümünden 0 ile 1000 arasında normalleştirilmiş koordinatlar olarak gelir ve düzene, tuvalin merkezine göre piksel cinsinden `yxyx` sırasıyla yazılır. Bu nedenle `width` ve `height` değerleri ürettiğiniz görüntüyle eşleşmelidir; aksi takdirde kutular yanlış yere konumlanır.

Metin içeren bir kutu her zaman metin olarak etiketlenir, numarası `character_boxes` içinde listelenen bir kutu karakter olarak etiketlenir ve diğer tüm kutular nesne olarak etiketlenir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MOSSImageLayoutPrompt/tr.md)

---
**Source fingerprint (SHA-256):** `da012a8d0dceaf6391110c90bd677d7929920d60fe961c00e5011b037206aa9a`
