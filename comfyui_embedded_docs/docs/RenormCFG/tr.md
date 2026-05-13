> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/tr.md)

RenormCFG düğümü, koşullu ölçeklendirme ve normalizasyon uygulayarak yayılım modellerindeki sınıflandırıcısız yönlendirme (CFG) sürecini değiştirir. Belirtilen zaman adımı eşiklerine ve yeniden normalizasyon faktörlerine dayanarak, görüntü oluşturma sırasında koşullu ve koşulsuz tahminlerin etkisini kontrol etmek için gürültü giderme sürecini ayarlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Yeniden normalleştirilmiş CFG'nin uygulanacağı yayılım modeli |
| `cfg_kesme` | FLOAT | Hayır | 0.0 - 100.0 | CFG ölçeklendirmesi için zaman adımı eşiği. Geçerli zaman adımı bu değerin altında olduğunda CFG ölçeklendirmesi uygulanır; aksi takdirde yalnızca koşullu tahmin kullanılır (varsayılan: 100.0) |
| `yenidenorm_cfg` | FLOAT | Hayır | 0.0 - 100.0 | CFG ölçeklendirmeli tahminin maksimum normunu orijinal koşullu tahmine göre sınırlayan yeniden normalizasyon faktörü. 0.0 değeri yeniden normalizasyonu devre dışı bırakır (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Yeniden normalleştirilmiş CFG işlevi uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `b59929606f7519574b7ad14a3caacee51e4f141dd6be3abb594217bcfdbc401e`
