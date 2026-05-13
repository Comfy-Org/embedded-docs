> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/tr.md)

Morphology düğümü, görüntülerdeki şekilleri işlemek ve analiz etmek için kullanılan matematiksel işlemler olan çeşitli morfolojik işlemleri uygular. Efekt gücünü kontrol etmek için özelleştirilebilir bir çekirdek boyutu kullanarak erozyon, genişleme, açma, kapama ve daha fazlası gibi işlemleri gerçekleştirebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `görüntü` | IMAGE | Evet | - | İşlenecek giriş görüntüsü |
| `işlem` | STRING | Evet | `"erode"`<br>`"dilate"`<br>`"open"`<br>`"close"`<br>`"gradient"`<br>`"bottom_hat"`<br>`"top_hat"` | Uygulanacak morfolojik işlem (varsayılan: "erode") |
| `çekirdek_boyutu` | INT | Evet | 3-999 | Yapılandırma elemanı çekirdeğinin boyutu (varsayılan: 3). Tek sayı olmalıdır. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `görüntü` | IMAGE | Morfolojik işlem uygulandıktan sonraki işlenmiş görüntü |

---
**Source fingerprint (SHA-256):** `7f6224a0e58fbb7263267b377394e119c6f8d65d16af4ce492ca9504654af7b4`
