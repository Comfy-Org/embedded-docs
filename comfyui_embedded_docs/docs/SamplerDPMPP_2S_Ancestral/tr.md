> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/tr.md)

SamplerDPMPP_2S_Ancestral düğümü, görüntü oluşturmak için DPM++ 2S Ancestral örnekleme yöntemini kullanan bir örnekleyici oluşturur. Bu örnekleyici, belirli bir tutarlılığı korurken çeşitli sonuçlar üretmek için deterministik ve stokastik unsurları birleştirir. Örnekleme süreci boyunca rastgelelik ve gürültü seviyelerini kontrol etmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme sırasında eklenen stokastik gürültü miktarını kontrol eder (varsayılan: 1.0) |
| `s_gürültü` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme işlemi sırasında uygulanan gürültünün ölçeğini kontrol eder (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Örnekleme işlem hattında kullanılabilecek yapılandırılmış bir örnekleyici nesnesi döndürür |