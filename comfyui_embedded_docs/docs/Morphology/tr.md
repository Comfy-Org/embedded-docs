# GörüntüMorfolojisi

Morphology düğümü, görüntülerdeki şekilleri işlemek ve analiz etmek için kullanılan matematiksel işlemler olan çeşitli morfolojik işlemleri uygular. Efekt gücünü kontrol etmek için özelleştirilebilir bir çekirdek boyutu kullanarak erozyon, genişleme, açma, kapama ve daha fazlası gibi işlemleri gerçekleştirebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | İşlenecek giriş görüntüsü | IMAGE | Evet | - |
| `işlem` | Uygulanacak morfolojik işlem (varsayılan: "erode") | STRING | Evet | `"erode"`<br>`"dilate"`<br>`"open"`<br>`"close"`<br>`"gradient"`<br>`"bottom_hat"`<br>`"top_hat"` |
| `çekirdek_boyutu` | Yapılandırma elemanı çekirdeğinin boyutu (varsayılan: 3). Tek sayı olmalıdır. | INT | Evet | 3-999 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Morfolojik işlem uygulandıktan sonraki işlenmiş görüntü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/tr.md)

---
**Source fingerprint (SHA-256):** `7f6224a0e58fbb7263267b377394e119c6f8d65d16af4ce492ca9504654af7b4`
