> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FlipSigmas/tr.md)

`FlipSigmas` düğümü, difüzyon modellerinde kullanılan sigma değerleri dizisini tersine çevirerek ve ilk değer sıfırsa sıfır olmayacak şekilde ayarlayarak bu diziyi değiştirmek için tasarlanmıştır. Bu işlem, gürültü seviyelerini ters sıraya uyarlamak ve verilerden gürültüyü kademeli olarak azaltarak çalışan modellerde üretim sürecini kolaylaştırmak için çok önemlidir.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `sigmalar`  | `SIGMAS`    | 'sigmas' parametresi, tersine çevrilecek sigma değerleri dizisini temsil eder. Bu dizi, difüzyon işlemi sırasında uygulanan gürültü seviyelerini kontrol etmek için çok önemlidir ve tersine çevrilmesi, ters üretim süreci için gereklidir. |

## Çıkışlar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `sigmalar`  | `SIGMAS`    | Çıktı, tersine çevrilmiş ve ilk değer sıfırsa sıfır olmayacak şekilde ayarlanmış, sonraki difüzyon modeli işlemlerinde kullanıma hazır değiştirilmiş sigma değerleri dizisidir. |