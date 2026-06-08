Bu düğüm, belirtilen bir klasörden görüntüleri ve bunlara karşılık gelen metin açıklamalarını yükler. Görüntü dosyalarını arar ve otomatik olarak aynı temel ada sahip eşleşen `.txt` dosyalarını açıklama olarak kullanmak üzere bulur. Düğüm ayrıca, alt klasörlerin çıktıda görüntülerin birden çok kez tekrarlanması gerektiğini belirtmek için bir sayı önekiyle (örneğin `10_klasor_adi`) adlandırılabildiği belirli bir klasör yapısını da destekler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `folder` | Görüntülerin yükleneceği klasör. Mevcut seçenekler, ComfyUI'nin giriş dizini içindeki alt dizinlerdir. | COMBO | Evet | *`folder_paths.get_input_subfolders()` işlevinden dinamik olarak yüklenir* |

**Not:** Düğüm belirli bir dosya yapısı bekler. Her görüntü dosyası (`.png`, `.jpg`, `.jpeg`, `.webp`) için, açıklama olarak kullanılmak üzere aynı ada sahip bir `.txt` dosyası arar. Bir açıklama dosyası bulunamazsa, boş bir dize kullanılır. Düğüm ayrıca, bir alt klasörün adının bir sayı ve alt çizgi ile başladığı (örneğin, `5_kediler`) özel bir yapıyı da destekler; bu, o alt klasördeki tüm görüntülerin nihai çıktı listesinde o sayı kadar tekrarlanmasına neden olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `texts` | Yüklenen görüntü tensörlerinin bir listesi. | IMAGE |
| `texts` | Yüklenen her görüntüye karşılık gelen metin açıklamalarının bir listesi. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/tr.md)

---
**Source fingerprint (SHA-256):** `e176f35118f08ea397c63f5b6f347d9cdb3dc1a08db7ad7a5cc8255e1526e6ca`
