> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAdd/tr.md)

CLIPAdd düğümü, iki CLIP modelini anahtar yamalarını birleştirerek bir araya getirir. İlk CLIP modelinin bir kopyasını oluşturur ve ardından ikinci modelden, konum kimlikleri ve logit ölçek parametreleri hariç, anahtar yamalarının çoğunu ekler. Bu sayede, ilk modelin yapısını korurken farklı CLIP modellerinden özellikleri harmanlamanıza olanak tanır.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|------------|--------|----------|
| `clip1` | CLIP | Zorunlu | - | - | Birleştirme için temel olarak kullanılacak birincil CLIP modeli |
| `clip2` | CLIP | Zorunlu | - | - | Eklenecek ek yamaları sağlayan ikincil CLIP modeli |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `CLIP` | CLIP | Her iki giriş modelinin özelliklerini birleştiren birleştirilmiş bir CLIP modeli döndürür |

---
**Source fingerprint (SHA-256):** `935d450d25d90dc623e3f2b39b251359a9066c9e1fdd2a70384982fb26a21864`
