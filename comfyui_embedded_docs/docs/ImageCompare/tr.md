# Görüntü Karşılaştırma

Image Compare düğümü, iki görüntüyü sürüklenebilir bir kaydırıcı kullanarak yan yana karşılaştırmak için görsel bir arayüz sağlar. Bir çıktı düğümü olarak tasarlanmıştır; yani verileri diğer düğümlere iletmez, bunun yerine görüntüleri inceleme için doğrudan kullanıcı arayüzünde görüntüler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü_a` | Karşılaştırılacak ilk görüntü. | IMAGE | Hayır | - |
| `görüntü_b` | Karşılaştırılacak ikinci görüntü. | IMAGE | Hayır | - |
| `karşılaştırma_görünümü` | Kullanıcı arayüzünde kaydırıcı karşılaştırma görünümünü etkinleştiren kontrol. | IMAGECOMPARE | Evet | - |

**Not:** Bu düğüm bir çıktı düğümüdür. `image_a` ve `image_b` isteğe bağlı olmakla birlikte, düğümün görünür bir etkiye sahip olması için en az bir görüntü sağlanmalıdır. Düğüm, bağlı olmayan herhangi bir görüntü girdisi için boş bir alan görüntüler.

## Çıktılar

Bu düğüm bir çıktı düğümüdür ve diğer düğümlerde kullanılmak üzere herhangi bir veri çıktısı üretmez. İşlevi, sağlanan görüntüleri ComfyUI arayüzünde görüntülemektir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompare/tr.md)

---
**Source fingerprint (SHA-256):** `bc065572c5631ed80c0590aabae775c51d0f607895a87cb2cca78037ab9a6638`
