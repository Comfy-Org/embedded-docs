# Görüntü Karşılaştırma

Görüntü Karşılaştırma düğümü, sürüklenebilir bir kaydırıcı kullanarak iki görüntüyü yan yana karşılaştırmak için görsel bir arayüz sağlar. Bu düğüm, bir çıktı düğümü olarak tasarlanmıştır; yani diğer düğümlere veri iletmez, bunun yerine görüntüleri doğrudan kullanıcı arayüzünde inceleme amacıyla görüntüler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü_a` | Karşılaştırılacak ilk görüntü. | IMAGE | Hayır | - |
| `görüntü_b` | Karşılaştırılacak ikinci görüntü. | IMAGE | Hayır | - |
| `karşılaştırma_görünümü` | Kullanıcı arayüzünde kaydırıcı karşılaştırma görünümünü etkinleştiren kontrol. | IMAGECOMPARE | Evet | - |

**Not:** Bu düğüm bir çıktı düğümüdür. `image_a` ve `image_b` isteğe bağlı olsa da, düğümün görünür bir etkiye sahip olması için en az bir görüntü sağlanmalıdır. Düğüm, bağlı olmayan herhangi bir görüntü girişi için boş bir alan görüntüleyecektir.

## Çıktılar

Bu düğüm bir çıktı düğümüdür ve diğer düğümlerde kullanılmak üzere herhangi bir veri çıktısı üretmez. İşlevi, sağlanan görüntüleri ComfyUI arayüzünde görüntülemektir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompare/tr.md)

---
**Source fingerprint (SHA-256):** `2bc980cd20aad3cf60300868599bbce8eaba1cdb21880d2b3f4cd628108d8139`
