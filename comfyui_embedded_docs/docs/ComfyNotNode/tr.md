> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNotNode/tr.md)

## Genel Bakış

Not düğümü, herhangi bir girdi değeri üzerinde mantıksal DEĞİL (NOT) işlemi gerçekleştirir. Girdi değeri yanlış (falsy) olarak kabul ediliyorsa (0, boş dize, None, False gibi) True döndürür, girdi değeri doğru (truthy) ise False döndürür. Doğruluk değerini belirlemek için Python'un standart kurallarını kullanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `değer` | ANY | Evet | Herhangi bir değer | Tersine çevrilecek girdi değeri. Herhangi bir veri türü kabul edilir ve Python'un doğruluk kuralları kullanılarak değerlendirilir. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | BOOLEAN | Girdi değerinin mantıksal tersi. Girdi yanlış (falsy) ise True, girdi doğru (truthy) ise False döndürür. |

---
**Source fingerprint (SHA-256):** `fd8f940218538fce28079bc836379703c0e3c04f80351520497855c464176877`
