# Boş Qwen Görsel Katmanlı Latent

Empty Qwen Image Layered Latent, Qwen-Image-Layered modelinin üzerine çizim yaptığı boş tuvali hazırlar. Bunu, birbirine sırayla tutturulmuş temiz aydınger kağıtlarından oluşan bir yığın gibi düşünün: model ilk kağıda tam resmi çizer ve sonraki her kağıda resmin bir bölümünü çizer. Bu düğüm, kağıtların boyutunu ve kaç tane olduğunu belirler. Kendisi hiçbir şey çizmez.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Oluşturulacak latent görselin genişliği. Değer 16'ya tam bölünebilir olmalıdır. (varsayılan: 640) | INT | Evet | 16 to MAX_RESOLUTION (step 16) |
| `yükseklik` | Oluşturulacak latent görselin yüksekliği. Değer 16'ya tam bölünebilir olmalıdır. (varsayılan: 640) | INT | Evet | 16 to MAX_RESOLUTION (step 16) |
| `katmanlar` | Resmin kaç katmana ayrılacağını belirler. Tam resim için her zaman fazladan bir sayfa ayrıldığından, `layers` değil, `layers + 1` görsel elde edersiniz. 2'ye ayarlarsanız tam resim artı 2 katman elde edersiniz. 0'a ayarlarsanız yalnızca tam resmi elde edersiniz. (varsayılan: 3) | INT | Evet | 0 to MAX_RESOLUTION (step 1) |
| `toplu_boyut` | Bir batch içinde üretilecek latent örnek sayısı. (varsayılan: 1) | INT | Evet | 1 ile 4096 |

**Not:** `width` ve `height` parametreleri, çıktı latent tensörünün uzamsal boyutlarını belirlemek için dahili olarak 8'e bölünür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Sıfırlarla dolu bir latent tensörü. Şekli `[batch_size, 16, layers + 1, height // 8, width // 8]` biçimindedir. | LATENT |

## Neden İstediğinizden Bir Görsel Daha Alırsınız?

Qwen-Image-Layered resmi yalnızca parçalara ayırmaz. Ayrıca tam resmi, katmanların yanında kendi sayfasına yeniden çizer. Bu yüzden yığın, istediğiniz katman sayısından her zaman bir sayfa daha yüksektir.

- **İlk görsel tam resimdir, bir katman değildir.** Zaten sahip olduğunuz resmin aynısıdır; yalnızca katmanları istiyorsanız bunu atın.
- **Tüm katmanları tekrar üst üste koyduğunuzda tam resmi yeniden elde edersiniz.** Katmanlar toplandığında ilk görsele ulaşmıyorsa, ayırma işlemi istediğiniz gibi çalışmamıştır. Bu, sonucu kontrol etmenin hızlı bir yoludur.
- **Sayfaların sırasını koruyun.** Yığın, hangi katmanın hangisinin üzerinde olduğunun tek kaydıdır. Sayfaların üzerinde nereye ait olduklarını belirten hiçbir yazı yoktur; bu nedenle görselleri yeniden sıralamak veya çıkarmak, katmanları yeniden sıralamak veya kaybetmek anlamına gelir.
- **Katmanlar şeffaf olarak üretilir**, böylece alt katmanlar opak bir arka planın arkasında gizlenmeden üst üste yerleştirilebilir.

## Kullanım Önerileri

Çıktıyı, normal bir boş latent gibi örnekleyiciye iletin; ardından VAE Decode'dan önce `dim` değeri `t` olarak ayarlanmış LatentCutToBatch düğümünü ekleyin. Bu adım, yığını tam resimden başlayarak sırayla ayrı görsellere ayırır.

Varsayılan 3 katmanla başlayın. Daha fazla katman istemek, daha uzun bir üretim ve daha ince bir ayrım anlamına gelir; modelin az sayıda katmanla neler yaptığını görmeden bu sayıyı artırmaya değmez.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `5ccac979fcbcefb65f28867a89401c095cb330e09c13270008c32feeeafb1287`
