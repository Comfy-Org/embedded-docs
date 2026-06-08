# Çift Model CFG Yönlendirici

Bu düğüm, yönlendirmeli CFG örnekleme sürecinde iki farklı model kullanmanıza olanak tanır: pozitif (koşullu) geçiş için bir model ve negatif (koşulsuz) geçiş için ayrı bir model. Negatif model sağlanmadığında, tek model kullanan standart bir CFG yönlendirici gibi davranır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `model` | Pozitif (koşullu) geçiş için kullanılan model. | MODEL | Evet | |
| `model_negative` | Negatif (koşulsuz) geçiş için kullanılan model. Sıradan CFG için aynı modeli kullanın. | MODEL | Hayır | |
| `pozitif` | Pozitif koşullandırma girişi. | CONDITIONING | Evet | |
| `cfg` | CFG ölçek değeri (varsayılan: 4.0). | FLOAT | Evet | 0.0 ile 100.0 (adım: 0.1) |
| `negatif` | Negatif model üzerinde çalıştırılan negatif koşullandırma. Metinsiz (yalnızca görüntü) koşulsuz geçiş için bağlantısız bırakın. | CONDITIONING | Hayır | |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `GUIDER` | Örneklemede kullanılmak üzere belirtilen modeller ve koşullandırma ile yapılandırılmış bir yönlendirici nesnesi. | GUIDER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualModelGuider/tr.md)

---
**Source fingerprint (SHA-256):** `a60803156e98d2ffe975d39922dfbeacafd1a2155d88dd2e285ac1426a1e7a33`
