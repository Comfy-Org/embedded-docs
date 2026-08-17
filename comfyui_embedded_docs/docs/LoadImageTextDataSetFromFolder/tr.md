# Klasörden Görsel ve Metin Veri Kümesi Yükle

Bu düğüm, belirtilen bir klasörden görsel ve metin altyazılarından oluşan bir veri kümesi yükler ve bunları bir liste olarak döndürür. Desteklenen biçimler: PNG, JPG, JPEG, WEBP. Her görsel dosyası için düğüm, altyazı olarak kullanmak üzere aynı temel ada sahip eşleşen bir `.txt` dosyasını otomatik olarak arar. Düğüm ayrıca, alt klasör adlarının bir sayı önekiyle başladığı (ör. `10_folder_name`) ve bu alt klasördeki görsellerin çıktıda o sayı kadar tekrarlanmasına neden olan bir klasör yapısını da destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `folder` | Görsellerin ve metin altyazılarının yükleneceği klasör. Mevcut seçenekler, ComfyUI giriş dizini içindeki alt klasörlerdir. | COMBO | Evet | *`folder_paths.get_input_subfolders()` işlevinden dinamik olarak yüklenir* |

**Not:** Düğüm belirli bir dosya yapısı bekler. Her görsel dosyası için (`.png`, `.jpg`, `.jpeg`, `.webp`), altyazı olarak kullanmak üzere aynı ada sahip bir `.txt` dosyası arar. Bir altyazı dosyası bulunamazsa, boş bir dize kullanılır. Düğüm ayrıca, bir alt klasörün adının bir sayı ve alt çizgi ile başladığı (örn. `5_cats`) özel bir yapıyı da destekler; bu, o alt klasördeki tüm görsellerin nihai çıktı listesinde o sayı kadar tekrarlanmasına neden olur. Seçilen klasör ComfyUI'nin giriş dizini içinde olmalıdır; dışarıya çözümlenen klasör adları reddedilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Yüklenen görsel tensörlerinin bir listesi. | IMAGE |
| `texts` | Yüklenen her görsele karşılık gelen metin altyazılarının bir listesi. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/tr.md)

---
**Source fingerprint (SHA-256):** `d34494d59a65edb38d7e6a5f12c241fb0093371db0b0bf1e52789e84209ad3f5`
