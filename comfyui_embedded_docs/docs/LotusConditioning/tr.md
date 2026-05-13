> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/tr.md)

LotusConditioning düğümü, Lotus modeli için önceden hesaplanmış koşullandırma gömmeleri (conditioning embeddings) sağlar. Donmuş bir kodlayıcı (frozen encoder) kullanarak boş koşullandırma (null conditioning) ile çalışır ve referans uygulamayla eşdeğerlik sağlamak için, çıkarım (inference) yapmaya veya büyük tensör dosyaları yüklemeye gerek kalmadan sabit kodlanmış (hardcoded) prompt gömmeleri döndürür. Bu düğüm, doğrudan üretim hattında (generation pipeline) kullanılabilecek sabit bir koşullandırma tensörü çıktısı verir.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| *Giriş yok* | - | - | - | Bu düğüm herhangi bir giriş parametresi kabul etmez. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `conditioning` | CONDITIONING | Lotus modeli için önceden hesaplanmış koşullandırma gömmeleri; sabit prompt gömmeleri ve boş bir sözlük içerir. |

---
**Source fingerprint (SHA-256):** `aa428f8c355e2840dadbf634fe27d20c7c323dbe8c21255b40f4dafa12e4a0d0`
