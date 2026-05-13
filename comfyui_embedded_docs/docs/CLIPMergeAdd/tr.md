> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/tr.md)

CLIPMergeAdd düğümü, ikinci modelden gelen yamaları birinci modele ekleyerek iki CLIP modelini birleştirir. İlk CLIP modelinin bir kopyasını oluşturur ve konum kimlikleri ile logit ölçek parametreleri hariç, ikinci modelden gelen anahtar yamaları seçici olarak dahil eder. Bu, temel modelin yapısını korurken CLIP model bileşenlerini birleştirmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `clip1` | CLIP | Evet | - | Kopyalanacak ve birleştirme için temel olarak kullanılacak ana CLIP modeli |
| `clip2` | CLIP | Evet | - | Temel modele eklenecek anahtar yamaları sağlayan ikincil CLIP modeli |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `CLIP` | CLIP | İkincil modelden eklenen yamalarla birlikte temel model yapısını içeren birleştirilmiş CLIP modeli |

---
**Source fingerprint (SHA-256):** `f212c2750f317ad51516a10a1a03a838b75bc878333381348d5eb388a2faf516`
