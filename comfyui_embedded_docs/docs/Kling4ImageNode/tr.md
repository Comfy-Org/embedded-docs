# Kling 4.0 Image

Kling 4.0 ile bir metin isteminden ve en fazla 10 referans görüntüsünden görüntüler oluşturun veya düzenleyin. Tek bir görüntü isteyin ya da düğümün aynı karakterleri ve stili koruyan bir dizi ilgili görüntü döndürmesine izin verin.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `referans_görüntüleri` | Referans görüntüleri için büyütülebilir yuvalar (`image_1` ... `image_10`). İstemde bunlara `@Image1`, `@Image2` ve benzeri şekilde başvurun. | AUTOGROW | Hayır | 0 ile 10 görsel arası |
| `istem` | Görüntünün açıklaması. Bağlı görüntülere `@Image1`, `@Image2`, ... olarak başvurun. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `çözünürlük` | Çıktı görüntüsünün çözünürlüğü. Varsayılan: `"2K"`. | COMBO | Evet | `"2K"`<br>`"4K"`<br>`"8K"` |
| `en_boy_oranı` | Çıktı görüntüsünün en-boy oranı. `"auto"` referans görüntülerini, aksi takdirde istemi izler. Varsayılan: `"auto"`. | COMBO | Evet | `"auto"`<br>`"9:16"`<br>`"2:3"`<br>`"3:4"`<br>`"1:1"`<br>`"4:3"`<br>`"3:2"`<br>`"16:9"`<br>`"21:9"` |
| `seri_miktarı` | Aynı karakterleri ve stili koruyan bir dizi ilgili görüntü oluşturun. `"auto"` modelin 2 ile 10 görsel arasında seçim yapmasına izin verir. Varsayılan: `"disabled"`. | COMBO | Evet | `"disabled"`<br>`"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `tohum` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

**Kısıtlamalar ve davranış:**

* En fazla 10 referans görüntüsü bağlanabilir.
* Her görüntü en az 300x300 piksel olmalı ve en-boy oranı 2:5 ile 5:2 arasında olmalıdır.
* `@ImageN` ifadesini içeren bir istem, N'den az görüntü bağlandığında hata verir.
* `series_amount` `"disabled"` olarak ayarlandığında düğüm bir görüntü döndürür; diğer herhangi bir değer, o sayıda görüntüden oluşan bir grup döndürür.
* Bir çağrının fiyatı çözünürlüğe, referans görüntüsü sayısına ve serideki görüntü sayısına göre ölçeklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Oluşturulan görüntü veya `series_amount` etkinleştirildiğinde bir görüntü grubu. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `7840b108419e759942aed332456cab73e748d9f018462011da3b1293646a4ffe`
