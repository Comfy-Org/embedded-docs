# YenidenNormalleştirCFG

RenormCFG düğümü, difüzyon modellerinde sınıflandırıcısız yönlendirme (CFG) sürecini koşullu ölçekleme ve normalleştirme uygulayarak değiştirir. Belirtilen bir zaman adımı eşiğine ve bir yeniden normalleştirme faktörüne göre gürültü giderme sürecini ayarlar; görüntü oluşturma sırasında koşullu ve koşulsuz tahminlerin etkisini kontrol eder. Sonuçta elde edilen model, bu yamalanmış CFG davranışıyla döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Yeniden normalleştirilmiş CFG'nin uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `cfg_kesme` | CFG ölçeklemesini uygulamak için zaman adımı eşiği. Geçerli zaman adımı bu değerin altında olduğunda CFG ölçeklemesi ve yeniden normalleştirme uygulanır; aksi halde yalnızca koşullu tahmin kullanılır (varsayılan: 100.0) | FLOAT | Hayır | 0.0 - 100.0 (adım 0.01) |
| `yenidenorm_cfg` | CFG ile ölçeklenmiş tahminin maksimum normunu orijinal koşullu tahmine göre sınırlayan yeniden normalleştirme faktörü. 0.0 değeri yeniden normalleştirmeyi devre dışı bırakır (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 100.0 (adım 0.01) |

Not: `cfg_trunc` ve `renorm_cfg` gelişmiş parametrelerdir. Yeniden normalleştirme yalnızca `renorm_cfg` 0.0'dan büyük olduğunda ve geçerli zaman adımı `cfg_trunc` değerinin altında olduğunda etkili olur; yeni tahmin normu hesaplanan maksimumun altındaysa yeniden ölçekleme yapılmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Yeniden normalleştirilmiş CFG işlevi uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/tr.md)

---
**Source fingerprint (SHA-256):** `5925bdfe2d62ef7261d73cda661834102ae6600b1afe53f4093568a6e83ec2ab`
