> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimAudioDuration/tr.md)

TrimAudioDuration düğümü, bir ses dosyasından belirli bir zaman dilimini kesmenize olanak tanır. Kırpma işleminin ne zaman başlayacağını ve sonuçta oluşacak ses klibinin ne kadar uzun olacağını belirtebilirsiniz. Düğüm, zaman değerlerini ses karesi konumlarına dönüştürerek ve ses dalga formunun ilgili bölümünü çıkararak çalışır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Evet | - | Kırpılacak ses girişi |
| `start_index` | FLOAT | Evet | -0xffffffffffffffff - 0xffffffffffffffff | Saniye cinsinden başlangıç zamanı, sondan saymak için negatif olabilir (saniyenin kesirlerini destekler). Varsayılan: 0.0 |
| `duration` | FLOAT | Evet | 0.0 - 0xffffffffffffffff | Saniye cinsinden süre. Varsayılan: 60.0 |

**Not:** Başlangıç zamanı, bitiş zamanından küçük ve ses uzunluğu dahilinde olmalıdır. Negatif başlangıç değerleri sesin sonundan geriye doğru sayar.

## Çıkışlar

| Çıkış Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `audio` | AUDIO | Belirtilen başlangıç zamanı ve süreye sahip kırpılmış ses parçası |