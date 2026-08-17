# Görüntü Veri Setini Klasöre Kaydet

Bu düğüm, bir görüntü listesini ComfyUI'nin çıktı dizinindeki belirtilen bir klasöre PNG dosyaları olarak kaydeder. Kullanımdan kaldırılmıştır: gereksizdir ve yerini, hedef klasörün dosya adı önekinde belirtilebildiği mevcut Save Image düğümleri almıştır. Düğüm, alınan her görüntüyü özelleştirilebilir bir dosya adı öneki kullanarak diske yazar ve mevcut dosyaların üzerine yazabilir veya üzerine yazılmasını önlemek için artan dosya adları oluşturabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `images` | Kaydedilecek görüntülerin listesi. | IMAGE | Evet | N/A |
| `folder_name` | Görüntülerin kaydedileceği klasörün adı (çıktı dizini içinde). Varsayılan değer "dataset"tir. | STRING | Hayır | N/A |
| `filename_prefix` | Kaydedilen görüntü dosya adları için önek. Varsayılan değer "image"dır. | STRING | Hayır | N/A |
| `mode` | Mevcut dosyaların üzerine yazılıp yazılmayacağını veya üzerine yazılmasını önlemek için dosya adlarının artırılıp artırılmayacağını belirtir. Varsayılan değer "overwrite"dır. | COMBO | Hayır | "overwrite"<br>"increment" |

**Not:** `images` girdisi bir listedir; yani aynı anda birden fazla görüntü alabilir ve işleyebilir. Tüm girdiler liste olarak alınır; `folder_name`, `filename_prefix` ve `mode` için bağlı listeden yalnızca ilk değer kullanılır. `folder_name`, ComfyUI'nin çıktı dizini içinde bir klasöre karşılık gelmelidir; bu dizinin dışına çıkan klasör adları (örneğin ".." kullanmak, mutlak bir yol veya sürücü harfi gibi) bir hatayla reddedilir. Görüntüler her zaman PNG formatında kaydedilir. `filename_prefix` parametresi gelişmiş bir seçenektir.

## Çıktılar

Bu düğümün herhangi bir veri çıktısı yoktur. Dosya sistemine kaydetme işlemi gerçekleştiren bir çıktı düğümüdür.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/tr.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`
