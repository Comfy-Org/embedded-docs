> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InvertBooleanNode/tr.md)

Bu düğüm, tek bir boolean (doğru/yanlış) girişi alır ve bunun ters değerini çıktı olarak verir. Mantıksal bir DEĞİL (NOT) işlemi gerçekleştirir; `true` değerini `false`, `false` değerini ise `true` yapar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `boolean` | BOOLEAN | Evet | `true`<br>`false` | Tersine çevrilecek olan giriş boolean değeri. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | BOOLEAN | Tersine çevrilmiş boolean değeri. |
