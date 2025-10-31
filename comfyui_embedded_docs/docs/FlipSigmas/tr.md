> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FlipSigmas/tr.md)

`FlipSigmas` düğümü, difüzyon modellerinde kullanılan sigma değerleri dizisini ters çevirerek ve orijinal olarak sıfır ise ilk değerin sıfır olmamasını sağlayarak manipüle etmek için tasarlanmıştır. Bu işlem, gürültü seviyelerini ters sırada uyarlamak ve verilerden kademeli olarak gürültüyü azaltarak çalışan modellerde üretim sürecini kolaylaştırmak için çok önemlidir.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `sigmas`  | `SIGMAS`    | 'sigmas' parametresi, ters çevrilecek sigma değerleri dizisini temsil eder. Bu dizi, difüzyon süreci boyunca uygulanan gürültü seviyelerini kontrol etmek için çok önemlidir ve ters çevrilmesi, ters üretim süreci için gereklidir. |

## Çıktılar

| Parametre | Veri Türu | Açıklama |
|-----------|-------------|-------------|
| `sigmas`  | `SIGMAS`    | Çıktı, sonraki difüzyon modeli işlemlerinde kullanıma hazır olacak şekilde, ters çevrilmiş ve orijinal olarak sıfır ise ilk değerin sıfır olmaması için ayarlanmış, değiştirilmiş sigma değerleri dizisidir. |