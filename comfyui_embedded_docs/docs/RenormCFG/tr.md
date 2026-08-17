# YenidenNormalleştirCFG

RenormCFG düğümü, difüzyon modellerinde sınıflandırıcısız rehberlik (CFG) sürecini, koşullu ölçekleme ve normalizasyon uygulayarak değiştirir. Belirtilen zaman adımı eşiklerine ve yeniden normalizasyon faktörlerine dayanarak gürültü giderme sürecini ayarlar; böylece görüntü üretimi sırasında koşullu ve koşulsuz tahminlerin etkisini kontrol eder.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Yeniden normalizasyonlu CFG'nin uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `cfg_trunc` | CFG ölçeklemesinin uygulanacağı zaman adımı eşiği. Geçerli zaman adımı bu değerin altındayken CFG ölçeklemesi uygulanır; aksi takdirde yalnızca koşullu tahmin kullanılır (varsayılan: 100.0) | FLOAT | Hayır | 0.0 - 100.0 |
| `renorm_cfg` | CFG ölçeklenmiş tahminin, orijinal koşullu tahmine göre maksimum normunu sınırlayan yeniden normalizasyon faktörü. 0.0 değeri yeniden normalizasyonu devre dışı bırakır (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Yeniden normalizasyonlu CFG işlevi uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/tr.md)

---
**Source fingerprint (SHA-256):** `5925bdfe2d62ef7261d73cda661834102ae6600b1afe53f4093568a6e83ec2ab`
