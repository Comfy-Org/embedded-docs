> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/tr.md)

SaveWEBM düğümü, bir dizi görüntüyü WEBM video dosyası olarak kaydeder. Birden fazla girdi görüntüsünü alır ve yapılandırılabilir kalite ayarları ve kare hızı ile VP9 veya AV1 codec'ini kullanarak bir videoya kodlar. Ortaya çıkan video dosyası, prompt bilgileri de dahil olmak üzere meta verilerle birlikte çıktı dizinine kaydedilir.

## Girdiler

| Parametre | Veri Tipi | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntüler` | IMAGE | Evet | - | Video kareleri olarak kodlanacak girdi görüntülerinin dizisi |
| `dosyaadı_öneki` | STRING | Hayır | - | Çıktı dosya adı için önek (varsayılan: "ComfyUI") |
| `codec` | COMBO | Evet | "vp9"<br>"av1" | Kodlama için kullanılacak video codec'i |
| `fps` | FLOAT | Hayır | 0.01-1000.0 | Çıktı videosu için kare hızı (varsayılan: 24.0) |
| `crf` | FLOAT | Hayır | 0-63.0 | Daha yüksek crf'nin daha düşük kalite ve daha küçük dosya boyutu, daha düşük crf'nin ise daha yüksek kalite ve daha büyük dosya boyutu anlamına geldiği kalite ayarı (varsayılan: 32.0) |

## Çıktılar

| Çıktı Adı | Veri Tipi | Açıklama |
|-------------|-----------|-------------|
| `ui` | PREVIEW | Kaydedilen WEBM dosyasını gösteren video önizlemesi |