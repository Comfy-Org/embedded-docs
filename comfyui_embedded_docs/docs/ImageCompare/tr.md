# Görüntü Karşılaştırma

## Genel Bakış

Image Compare düğümü, sürüklenebilir bir kaydırıcı kullanarak iki görüntüyü yan yana karşılaştırmak için görsel bir arayüz sağlar. Bir çıktı düğümü olarak tasarlanmıştır; yani diğer düğümlere veri aktarmaz, bunun yerine görüntüleri inceleme için doğrudan kullanıcı arayüzünde görüntüler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image_a` | Karşılaştırılacak ilk görüntü. | IMAGE | Hayır | - |
| `image_b` | Karşılaştırılacak ikinci görüntü. | IMAGE | Hayır | - |
| `compare_view` | Kullanıcı arayüzünde kaydırıcılı karşılaştırma görünümünü etkinleştiren kontrol. | IMAGECOMPARE | Evet | - |

**Not:** Bu düğüm bir çıktı düğümüdür. `image_a` ve `image_b` isteğe bağlı olsa da düğümün görünür bir etkisi olması için en az bir görüntü sağlanmalıdır. Düğüm, bağlı olmayan her görüntü girişi için boş bir alan görüntüler. Sağlanan her görüntü grubu, sırasıyla `comfy.compare.a` ve `comfy.compare.b` önekleri altında geçici depolamaya kaydedilir ve ardından kaydırıcı görünümünde gösterilir.

## Çıktılar

Bu düğüm bir çıktı düğümüdür ve diğer düğümlerde kullanılmak üzere herhangi bir veri çıktısı üretmez. İşlevi, sağlanan görüntüleri ComfyUI arayüzünde görüntülemektir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompare/tr.md)

---
**Source fingerprint (SHA-256):** `bc065572c5631ed80c0590aabae775c51d0f607895a87cb2cca78037ab9a6638`
