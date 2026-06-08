ByteDance Seedream 4.5 & 5.0 düğümü, 4K çözünürlüğe kadar birleşik metin-görüntü oluşturma ve hassas tek cümle düzenleme yetenekleri sağlar. Metin istemlerinden yeni görüntüler oluşturabilir veya metin talimatlarını kullanarak mevcut görüntüleri düzenleyebilir. Düğüm, hem tek görüntü oluşturmayı hem de birden çok ilgili görüntünün sıralı oluşturulmasını destekler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Oluşturma için kullanılacak Seedream modeli. Mevcut modeller arasında seedream-4-0, seedream-4-5 ve seedream-5-0 varyantları bulunur. | STRING | Evet | Açıklamaya Bakın |
| `prompt` | Görüntü oluşturma veya düzenleme için metin istemi. En az 1 karakter uzunluğunda olmalıdır. | STRING | Evet | - |
| `görüntü` | Görüntüden görüntüye oluşturma için giriş görüntüsü/görüntüleri. Tek veya çoklu referans oluşturma için referans görüntüsü/görüntüleri. Çoğu model için maksimum 10 referans görüntüsü veya seedream-5-0-260128 için 14 referans görüntüsü. | IMAGE | Hayır | - |
| `boyut önayarı` | Önerilen bir boyut seçin. Aşağıdaki genişlik ve yüksekliği kullanmak için Özel'i seçin. Varsayılan: RECOMMENDED_PRESETS_SEEDREAM_4'ten ilk ön ayar. | STRING | Hayır | Birden çok seçenek mevcut |
| `genişlik` | Görüntü için özel genişlik. Değer yalnızca `boyut önayarı` "Özel" olarak ayarlandığında çalışır. Varsayılan: 2048. | INT | Hayır | 1024 ila 6240 (adım 2) |
| `yükseklik` | Görüntü için özel yükseklik. Değer yalnızca `boyut önayarı` "Özel" olarak ayarlandığında çalışır. Varsayılan: 2048. | INT | Hayır | 1024 ila 4992 (adım 2) |
| `sıralı_resim_oluşturma` | Grup görüntü oluşturma modu. "disabled" tek bir görüntü oluşturur. "auto" modelin birden çok ilgili görüntü (ör. hikaye sahneleri, karakter varyasyonları) oluşturup oluşturmayacağına karar vermesini sağlar. Varsayılan: "disabled". | STRING | Hayır | "disabled"<br>"auto" |
| `maks_resim` | sequential_image_generation='auto' olduğunda oluşturulacak maksimum görüntü sayısı. Toplam görüntü (giriş + oluşturulan) 15'i geçemez. Varsayılan: 1. | INT | Hayır | 1 ila 15 (adım 1) |
| `tohum` | Oluşturma için kullanılacak tohum. Varsayılan: 0. | INT | Hayır | 0 ila 2147483647 (adım 1) |
| `filigran` | Görüntüye "AI tarafından oluşturuldu" filigranı eklenip eklenmeyeceği. Varsayılan: Yanlış. | BOOLEAN | Hayır | - |
| `kısmi_hatada_durdur` | Etkinleştirilirse, istenen görüntülerden herhangi biri eksikse veya bir hata döndürürse yürütmeyi durdurun. Varsayılan: Doğru. | BOOLEAN | Hayır | - |

**Parametre kısıtlamalarına ilişkin notlar:**
- Minimum görüntü çözünürlüğü seçilen modele bağlıdır: seedream-4-5 ve seedream-5-0 modelleri için 3,68MP, seedream-4-0 modelleri için 0,92MP.
- Maksimum görüntü çözünürlüğü seedream-5-0 modelleri için 10,4MP ve diğer modeller için 16,78MP'dir.
- Referans görüntüleri 1:3 ile 3:1 arasında bir en boy oranına sahip olmalıdır.
- `sequential_image_generation` "auto" olarak ayarlandığında, giriş görüntülerinin toplam sayısı artı `max_images` 15'i geçemez.
- `width` ve `height` parametreleri yalnızca `size_preset` "Özel" olarak ayarlandığında kullanılır.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Giriş parametrelerine ve isteme dayalı olarak oluşturulan görüntü(ler). Birden çok görüntü oluşturulursa tek bir görüntü tensörü veya bir grup görüntü tensörü döndürür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNode/tr.md)

---
**Source fingerprint (SHA-256):** `ce130246026e0f5036e137bea4e193f51097e0812459586dcbeb87ef01975630`
