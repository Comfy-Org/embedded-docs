# YenidenNormalleştirCFG

RenormCFG düğümü, koşullu ölçekleme ve normalizasyon uygulayarak difüzyon modellerindeki sınıflandırıcısız yönlendirme (CFG) sürecini değiştirir. Belirtilen zaman adımı eşiklerine ve yeniden normalizasyon faktörlerine dayalı olarak gürültü giderme sürecini ayarlar ve görüntü üretimi sırasında koşullu ile koşulsuz tahminlerin etkisini kontrol eder.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Yeniden normalleştirilmiş CFG'nin uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `cfg_kesme` | CFG ölçeklemenin uygulanması için zaman adımı eşiği. Geçerli zaman adımı bu değerin altındayken CFG ölçekleme uygulanır; aksi takdirde yalnızca koşullu tahmin kullanılır (varsayılan: 100.0) | FLOAT | Hayır | 0.0 - 100.0 |
| `yenidenorm_cfg` | CFG ile ölçeklenmiş tahminin, orijinal koşullu tahmine göre maksimum normunu sınırlayan yeniden normalizasyon faktörü. 0.0 değeri yeniden normalizasyonu devre dışı bırakır (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Yeniden normalleştirilmiş CFG işlevi uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/tr.md)

---
**Source fingerprint (SHA-256):** `5925bdfe2d62ef7261d73cda661834102ae6600b1afe53f4093568a6e83ec2ab`
