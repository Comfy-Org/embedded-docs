> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/tr.md)

Bu düğüm, belirtilen bir klasörden görüntüler ve bunlara karşılık gelen metin açıklamalarından oluşan bir veri kümesi yükler. Görüntü dosyalarını arar ve otomatik olarak aynı temel ada sahip eşleşen `.txt` dosyalarını açıklama olarak kullanmak için bakar. Düğüm ayrıca, içindeki görüntülerin çıktıda birden çok kez tekrarlanması gerektiğini belirtmek için alt klasörlerin bir sayı önekiyle (örneğin `10_klasor_adi`) adlandırılabileceği belirli bir klasör yapısını da destekler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `folder` | COMBO | Evet | *`folder_paths.get_input_subfolders()` ile dinamik olarak yüklenir* | Görüntülerin yükleneceği klasör. Mevcut seçenekler, ComfyUI'nin giriş dizini içindeki alt dizinlerdir. |

**Not:** Düğüm belirli bir dosya yapısı bekler. Her görüntü dosyası (`.png`, `.jpg`, `.jpeg`, `.webp`) için, aynı ada sahip bir `.txt` dosyasını açıklama olarak kullanmak üzere arar. Bir açıklama dosyası bulunamazsa, boş bir dize kullanılır. Düğüm ayrıca, bir alt klasörün adının bir sayı ve alt çizgi ile başladığı (örneğin `5_kediler`) özel bir yapıyı da destekler; bu, o alt klasörün içindeki tüm görüntülerin nihai çıktı listesinde o sayı kadar tekrarlanmasına neden olur.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `images` | IMAGE | Yüklenen görüntü tensörlerinin bir listesi. |
| `texts` | STRING | Yüklenen her görüntüye karşılık gelen metin açıklamalarının bir listesi. |
