> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxGuidance/tr.md)

## Girişler

| Parametre | Veri Türü | Açıklama |
|----------------|-----------|-------------|
| `koşullandırma` | CONDITIONING | Girdi koşullandırma verisi, genellikle önceki kodlama veya işleme adımlarından gelir |
| `rehberlik` | FLOAT | Metin ipuçlarının görüntü oluşturma üzerindeki etkisini kontrol eder, 0.0 ile 100.0 arasında ayarlanabilir bir aralık |

## Çıkışlar

| Parametre | Veri Türü | Açıklama |
|----------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Yeni kılavuz değerini içeren güncellenmiş koşullandırma verisi |