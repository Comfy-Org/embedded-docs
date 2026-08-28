# Klasörden Görsel ve Metin Veri Kümesi Yükle

Bu düğüm, seçilen bir klasörden görüntü-metin açıklama çiftlerinden oluşan bir veri kümesi yükler ve bunları bir liste olarak döndürür. PNG, JPG, JPEG ve WEBP görüntülerini destekler ve her görüntü için aynı temel ada sahip bir `.txt` dosyasında açıklama arar. Düğüm ayrıca kohya-ss/sd-scripts klasör yapısını da destekler; burada bir sayıyla başlayan alt klasör adı (örn. `10_cats`), o alt klasördeki görüntüleri çıktıda bu sayı kadar tekrarlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `folder` | Görüntülerin ve metin açıklamalarının yükleneceği klasör. | COMBO | Evet | ComfyUI'nin input dizinindeki alt klasörler (dinamik olarak yüklenir) |

**Not:** Seçilen klasör, ComfyUI'nin input dizininin bir alt klasörü olmalıdır. Düğüm, her görüntü için bir `.txt` açıklama dosyası bekler: her görüntü dosyası (`.png`, `.jpg`, `.jpeg`, `.webp`) için aynı konumda aynı temel ada sahip bir `.txt` dosyası arar ve kırpılmış içeriğini açıklama olarak kullanır. Açıklama dosyası bulunamazsa boş bir dize kullanılır. Düğüm ayrıca kohya-ss/sd-scripts klasör yapısını da destekler: adı bir sayı ve alt çizgi ile başlayan alt klasörler (örn. `5_cats`), içlerindeki görüntüleri nihai çıktı listesinde bu sayı kadar tekrarlar. Seçilen klasörde geçerli görüntü yoksa düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Yüklenen görüntülerin listesi. Görüntüler RGB'ye dönüştürülür ve 0–1 float aralığına normalleştirilir. | IMAGE |
| `texts` | Yüklenen her görüntü için bir tane olmak üzere metin açıklamalarının listesi. Açıklamalar, eşleşen `.txt` dosyasının kırpılmış içeriğidir veya açıklama dosyası yoksa boş bir dizedir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/tr.md)

---
**Source fingerprint (SHA-256):** `d34494d59a65edb38d7e6a5f12c241fb0093371db0b0bf1e52789e84209ad3f5`
