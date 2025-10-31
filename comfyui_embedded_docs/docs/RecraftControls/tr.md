> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftControls/tr.md)

Recraft oluşturmayı özelleştirmek için Recraft Kontrolleri oluşturur. Bu düğüm, Recraft görüntü oluşturma işlemi sırasında kullanılacak renk ayarlarını yapılandırmanıza olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `colors` | COLOR | Hayır | - | Ana elemanlar için renk ayarları |
| `background_color` | COLOR | Hayır | - | Arka plan rengi ayarı |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `recraft_controls` | CONTROLS | Renk ayarlarını içeren yapılandırılmış Recraft kontrolleri |