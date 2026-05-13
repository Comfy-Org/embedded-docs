> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxGuidance/tr.md)

## Girişler

| Parametre | Veri Türü | Açıklama |
|----------------|-----------|-------------|
| conditioning | CONDITIONING | Önceki kodlama veya işleme adımlarından gelen giriş koşullandırma verileri |
| guidance | FLOAT | Metin istemlerinin görüntü oluşturma üzerindeki etkisini kontrol eder, 0.0 ile 100.0 arasında ayarlanabilir aralık |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|----------------|-----------|-------------|
| CONDITIONING | CONDITIONING | Yeni guidance değerini içeren güncellenmiş koşullandırma verileri |