# Boş Qwen Görsel Katmanlı Latent

Boş Qwen Görüntü Katmanlı Gizli (Empty Qwen Image Layered Latent) düğümü, Qwen-Image-Layered modelinin üzerine çizim yaptığı boş tuvali hazırlar. Bunu, sırayla tutturulmuş temiz aydınger kağıtlarından oluşan bir yığın gibi düşünün: model ilk kağıdı tam görselle doldurur, sonraki her kağıdı da o görselin bir parçasıyla doldurur. Bu düğüm kağıtların boyutunu ve sayısını belirler. Kendisi hiçbir şey çizmez.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Oluşturulacak gizli görüntünün genişliği. Değer 16'ya bölünebilir olmalıdır. (varsayılan: 640) | INT | Evet | 16 ile MAX_RESOLUTION arası |
| `yükseklik` | Oluşturulacak gizli görüntünün yüksekliği. Değer 16'ya bölünebilir olmalıdır. (varsayılan: 640) | INT | Evet | 16 ile MAX_RESOLUTION arası |
| `katmanlar` | Görselin kaç katmana ayrılacağını belirler. Tam görsel için her zaman fazladan bir kağıt ayrılır, bu nedenle `katmanlar` değil, `layers + 1` görsel elde edersiniz. 2 olarak ayarlarsanız tam görsel artı 2 katman elde edersiniz. 0 olarak ayarlarsanız yalnızca tam görseli elde edersiniz. (varsayılan: 3) | INT | Evet | 0 ile MAX_RESOLUTION arası |
| `toplu_boyut` | Bir grupta oluşturulacak gizli örnek sayısı. (varsayılan: 1) | INT | Hayır | 1 ile 4096 arası |

**Not:** `width` ve `height` parametreleri, çıktı gizli tensörünün uzamsal boyutlarını belirlemek için dahili olarak 8'e bölünür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Sıfırlarla dolu bir gizli tensör. Şekli `[batch_size, 16, layers + 1, height // 8, width // 8]` şeklindedir. | LATENT |

## Neden istediğinizden bir görsel daha fazla alırsınız

Qwen-Image-Layered yalnızca bir görseli parçalarına ayırmaz. Ayrıca tam görseli, katmanların yanında, kendi kağıdına yeniden çizer. Bu yüzden kağıt yığını her zaman istediğiniz katman sayısından bir kağıt daha yüksektir.

- **İlk görsel bir katman değil, tam görseldir.** Zaten sahip olduğunuz görselin aynısıdır, bu yüzden yalnızca katmanları istediğinizde onu atın.
- **Tüm katmanları üst üste koyduğunuzda tam görseli yeniden elde edersiniz.** Katmanların toplamı o ilk görsele uymuyorsa, ayırma istediğiniz gibi çalışmamıştır; bu da sonucu hızlıca kontrol etmenin bir yoludur.
- **Kağıtların sırasını koruyun.** Yığın, hangi katmanın hangisinin üzerinde olduğunu gösteren tek kayıttır. Kağıtların üzerinde nereye ait olduklarını belirten hiçbir şey yazmaz, bu nedenle görselleri yeniden sıralamak veya silmek, katmanları yeniden sıralamak veya kaybetmek anlamına gelir.
- **Katmanlar şeffaflıkla çıkar**, böylece alt katmanlar opak bir arka planın arkasında gizlenmeden üst üste dizilebilir.

## Kullanım önerileri

Çıktıyı normal bir boş gizli değişken gibi örnekleyiciye (sampler) gönderin, ardından VAE kod çözmeden önce `dim` değeri `t` olarak ayarlanmış LatentCutToBatch'i yerleştirin. Kağıt yığınını tam görselden başlayarak sırayla ayrı görsellere ayıran adım budur.

Varsayılan 3 katmanla başlayın. Daha fazla istemek daha uzun bir üretim ve daha ince bir ayrım anlamına gelir ve modelin az sayıda katmanla ne yaptığını görmeden artırmaya değmez.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `fe97966663c534dd347aa49a908a8026f2c34716631f1d17be97d74eacc3574e`
