> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/tr.md)

Bu düğüm, Recraft V4 veya V4 Pro AI modellerini kullanarak metin açıklamalarından görüntüler oluşturur. İsteğinizi harici bir API'ye gönderir ve oluşturulan görüntüleri döndürür. Çıktıyı model, görüntü boyutu ve oluşturulacak görüntü sayısını belirterek kontrol edebilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | Görüntü oluşturma için istek. Maksimum 10.000 karakter. |
| `negative_prompt` | STRING | Hayır | Yok | Bir görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması. |
| `model` | COMBO | Evet | `"recraftv4"`<br>`"recraftv4_pro"` | Oluşturma için kullanılacak model. Bir model seçmek, mevcut görüntü boyutlarını belirler. |
| `size` | COMBO | Evet | Modele göre değişir | Oluşturulan görüntünün boyutu. Mevcut seçenekler seçilen modele bağlıdır. `recraftv4` için varsayılan "1024x1024"tür. `recraftv4_pro` için varsayılan "2048x2048"dir. |
| `n` | INT | Evet | 1 ile 6 | Oluşturulacak görüntü sayısı (varsayılan: 1). |
| `seed` | INT | Evet | 0 ile 18446744073709551615 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirlemek için tohum; gerçek sonuçlar tohumdan bağımsız olarak belirleyici değildir (varsayılan: 0). |
| `recraft_controls` | CUSTOM | Hayır | Yok | Recraft Kontroller düğümü aracılığıyla oluşturma üzerinde isteğe bağlı ek kontroller. |

**Not:** `size` parametresi, mevcut seçenekleri seçilen `model`e göre değişen dinamik bir girdidir. `seed` değeri, tekrarlanabilir görüntü çıktılarını garanti etmez.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Oluşturulan görüntü veya görüntü grubu. |