# LotusKoşullandırma

LotusConditioning düğümü, Lotus modeli için sabit, önceden hesaplanmış koşullandırma gömmeleri sağlar. Lotus, null koşullandırmalı dondurulmuş bir kodlayıcı kullandığından, düğüm çıkarım çalıştırmak veya büyük tensör dosyaları yüklemek yerine ortaya çıkan istem gömmelerini doğrudan satır içine yerleştirir; bu nedenle çıktısı asla değişmez. Döndürülen koşullandırma, Lotus uyumlu koşullandırma bekleyen bir üretim işlem hattına doğrudan takılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| *Girdi yok* | Bu düğüm herhangi bir girdi parametresi kabul etmez. | - | - | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | Lotus modeli için önceden hesaplanmış koşullandırma gömmeleri. Sabit istem gömmelerini boş bir sözlükle birlikte tutan bir koşullandırma listesi olarak döndürülür. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `1fcb6530850341253c8acb47b2f26ee79d93f51eca84bef03a1fa5de33d6bc8d`
