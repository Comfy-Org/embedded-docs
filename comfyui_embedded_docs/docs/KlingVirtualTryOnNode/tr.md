> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/tr.md)

Kling Sanal Deneme Düğümü. Bir insan görseli ve bir kıyafet görseli girin; kıyafeti insan üzerinde deneyin. Birden fazla kıyafet parçası görselini beyaz arka planlı tek bir görselde birleştirebilirsiniz.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `human_image` | IMAGE | Evet | - | Kıyafet denenecek insan görseli |
| `cloth_image` | IMAGE | Evet | - | İnsan üzerinde denenecek kıyafet görseli |
| `model_name` | STRING | Evet | `"kolors-virtual-try-on-v1"` | Kullanılacak sanal deneme modeli (varsayılan: "kolors-virtual-try-on-v1") |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Kıyafet parçasının insan üzerinde denendiğini gösteren sonuç görseli |

---
**Source fingerprint (SHA-256):** `bfd0da440d3ad85e15ce16851313f2e75421a8a3eb5e4c651350432955afc731`
