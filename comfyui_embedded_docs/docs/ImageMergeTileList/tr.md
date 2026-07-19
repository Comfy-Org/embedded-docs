# Döşeme Listesini Görüntüye Birleştir

Bu düğüm, bir görüntü döşeme listesini alır ve bunları tek, daha büyük bir görüntü halinde birleştirir. Daha önce bir ızgaraya bölünmüş, üst üste binen döşemelerden oluşan bir görüntüyü yeniden oluşturmak için tasarlanmıştır ve kesintisiz bir nihai sonuç oluşturmak için ağırlıklı bir harmanlama tekniği kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image_list` | Birleştirilecek görüntü döşemelerinin listesi. Listedeki ilk döşeme, tüm işlem için döşeme boyutlarını ve veri türünü belirlemek amacıyla kullanılır. | IMAGE | Evet | Yok |
| `final_width` | Nihai birleştirilmiş görüntünün piksel cinsinden genişliği (varsayılan: 1024). | INT | Evet | 64 - 32768 |
| `final_height` | Nihai birleştirilmiş görüntünün piksel cinsinden yüksekliği (varsayılan: 1024). | INT | Evet | 64 - 32768 |
| `overlap` | Bitişik döşemeler arasındaki piksel cinsinden örtüşme miktarı. 0'dan büyük bir değer, döşeme birleşim yerlerinde yumuşak bir harmanlama efekti sağlar (varsayılan: 128). | INT | Evet | 0 - 4096 |

**Not:** `image_list` dinamik bir giriş listesidir. Düğüm, döşemeleri sağlandıkları sırayla işleyecek ve `final_width`, `final_height` ve ilk döşemenin boyutları tarafından tanımlanan ızgarayı doldurmak için gereken sayıya kadar işleme devam edecektir. Liste gerekenden daha fazla döşeme içeriyorsa, fazla döşemeler yok sayılır.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Giriş döşemelerinden yeniden oluşturulan nihai birleştirilmiş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageMergeTileList/tr.md)

---
**Source fingerprint (SHA-256):** `f8f770ca2e9806d2feb55bb1dfe2c26b09d7a3506caf664990d8536ec5660c92`
