> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompare/tr.md)

Görüntü Karşılaştırma düğümü, sürüklenebilir bir kaydırıcı kullanarak iki görüntüyü yan yana karşılaştırmak için görsel bir arayüz sağlar. Bu düğüm, bir çıktı düğümü olarak tasarlanmıştır; yani diğer düğümlere veri iletmez, bunun yerine görüntüleri doğrudan kullanıcı arayüzünde inceleme amacıyla görüntüler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `image_a` | IMAGE | Hayır | - | Karşılaştırılacak ilk görüntü. |
| `image_b` | IMAGE | Hayır | - | Karşılaştırılacak ikinci görüntü. |
| `compare_view` | IMAGECOMPARE | Evet | - | Kullanıcı arayüzünde kaydırıcı karşılaştırma görünümünü etkinleştiren kontrol. |

**Not:** Bu düğüm bir çıktı düğümüdür. `image_a` ve `image_b` isteğe bağlı olsa da, düğümün görünür bir etkiye sahip olması için en az bir görüntü sağlanmalıdır. Düğüm, bağlı olmayan herhangi bir görüntü girişi için boş bir alan görüntüleyecektir.

## Çıktılar

Bu düğüm bir çıktı düğümüdür ve diğer düğümlerde kullanılmak üzere herhangi bir veri çıktısı üretmez. İşlevi, sağlanan görüntüleri ComfyUI arayüzünde görüntülemektir.

---
**Source fingerprint (SHA-256):** `2bc980cd20aad3cf60300868599bbce8eaba1cdb21880d2b3f4cd628108d8139`
