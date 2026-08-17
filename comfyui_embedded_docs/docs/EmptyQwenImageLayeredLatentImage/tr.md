# Boş Qwen Görsel Katmanlı Latent

Empty Qwen Image Layered Latent düğümü, Qwen-Image-Layered modelinin üzerine çizim yaptığı boş tuvali hazırlar. Bunu, sırayla birbirine tutturulmuş temiz aydınger kağıtlarından oluşan bir yığın olarak düşünün: model ilk kağıdı tam resimle doldurur ve sonraki her kağıdı da o resmin bir parçasıyla doldurur. Bu düğüm kağıtların ne kadar büyük olduğuna ve kaç tane olduğuna karar verir, ancak kendisi hiçbir şey çizmez.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Oluşturulacak latent görüntünün genişliği. Değer 16'ya bölünebilir olmalıdır. (varsayılan: 640) | INT | Evet | 16 ila MAX_RESOLUTION (adım 16) |
| `height` | Oluşturulacak latent görüntünün yüksekliği. Değer 16'ya bölünebilir olmalıdır. (varsayılan: 640) | INT | Evet | 16 ila MAX_RESOLUTION (adım 16) |
| `layers` | Resmin kaç katmana ayrılacağını belirler. Tam resim için her zaman fazladan bir kağıt ayrılır; bu nedenle `layers` değil, `layers + 1` görüntü elde edersiniz. 2 olarak ayarlarsanız tam resim artı 2 katman elde edersiniz. 0 olarak ayarlarsanız yalnızca tam resmi elde edersiniz. (varsayılan: 3) | INT | Evet | 0 ila MAX_RESOLUTION (adım 1) |
| `batch_size` | Bir toplu işlemde (batch) oluşturulacak latent örnek sayısı. (varsayılan: 1) | INT | Evet | 1 ila 4096 |

**Not:** `width` ve `height` parametreleri, çıktı latent tensörünün uzamsal boyutlarını belirlemek için dahili olarak 8'e bölünür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Sıfırlarla doldurulmuş bir latent tensör. Şekli `[batch_size, 16, layers + 1, height // 8, width // 8]` biçimindedir. | LATENT |

## Neden istediğinizden bir görüntü fazla alırsınız

Qwen-Image-Layered yalnızca bir resmi parçalara ayırmakla kalmaz. Ayrıca katmanların yanında, kendi kağıdı üzerinde tam resmi de yeniden boyar. Bu yüzden yığın her zaman, istediğiniz katman sayısından bir kağıt daha fazla içerir.

- **İlk görüntü tam resimdir, bir katman değildir.** Zaten sahip olduğunuz resmin aynısıdır; bu yüzden yalnızca katmanları istiyorsanız onu atın.
- **Tüm katmanları üst üste yerleştirdiğinizde tam resmi yeniden elde edersiniz.** İlk görüntüye eklenerek toplamı tutmuyorlarsa, ayırma istediğiniz gibi çalışmamış demektir; bu, sonucu kontrol etmenin hızlı bir yoludur.
- **Kağıtları sırayla saklayın.** Yığın, hangi katmanın hangisinin üzerinde olduğunu gösteren tek kayıttır. Kağıtların üzerinde nereye ait olduklarını belirten hiçbir şey yazmaz; bu yüzden görüntüleri yeniden sıralamak veya atmak, katmanları yeniden sıralamak veya kaybetmek anlamına gelir.
- **Katmanlar şeffaf olarak çıkar**, böylece alt katmanlar opak bir arka plan tarafından gizlenmeden üst üste istiflenebilir.

## Kullanım önerileri

Çıktıyı, normal boş bir latent görüntüde olduğu gibi örnekleyiciye gönderin, ardından VAE Decode'dan önce `dim` değeri `t` olarak ayarlanmış LatentCutToBatch düğümünü ekleyin. Yığını, tam resimden başlayarak sırayla ayrı görüntülere ayıran adım budur.

Varsayılan 3 katmanla başlayın. Daha fazla istemek daha uzun bir üretim ve daha ince bir ayrım anlamına gelir; modelin az sayıda katmanla neler yaptığını görmeden artırmaya değmez.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `5ccac979fcbcefb65f28867a89401c095cb330e09c13270008c32feeeafb1287`
