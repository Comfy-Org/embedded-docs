# Kling Sanal Deneme

Kling Sanal Deneme Düğümü. Bir insan görseli ve bir kıyafet görseli girin; kıyafeti insan üzerinde deneyin. Birden fazla kıyafet parçası görselini beyaz arka planlı tek bir görselde birleştirebilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `insan_görüntüsü` | Kıyafet denenecek insan görseli | IMAGE | Evet | - |
| `kıyafet_görüntüsü` | İnsan üzerinde denenecek kıyafet görseli | IMAGE | Evet | - |
| `model_adı` | Kullanılacak sanal deneme modeli (varsayılan: "kolors-virtual-try-on-v1") | STRING | Evet | `"kolors-virtual-try-on-v1"` |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Kıyafet parçasının insan üzerinde denendiğini gösteren sonuç görseli | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/tr.md)

---
**Source fingerprint (SHA-256):** `bfd0da440d3ad85e15ce16851313f2e75421a8a3eb5e4c651350432955afc731`
