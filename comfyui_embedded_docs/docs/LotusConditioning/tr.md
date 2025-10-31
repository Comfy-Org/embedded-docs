> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/tr.md)

LotusConditioning düğümü, Lotus modeli için önceden hesaplanmış koşullandırma gömüleri sağlar. Donmuş bir kodlayıcıyı boş koşullandırma ile kullanır ve çıkarım gerektirmeden veya büyük tensör dosyaları yüklemeden referans uygulamasıyla uyum sağlamak için sabitlenmiş prompt gömüleri döndürür. Bu düğüm, üretim hattında doğrudan kullanılabilen sabit bir koşullandırma tensörü çıktısını verir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| *Girdi yok* | - | - | - | Bu düğüm herhangi bir girdi parametresi kabul etmez. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Lotus modeli için önceden hesaplanmış koşullandırma gömüleri; sabit prompt gömülerini ve boş bir sözlük içerir. |