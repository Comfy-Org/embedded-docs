> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/tr.md)

Bu düğüm, Rodin API'sini kullanarak 3B varlıklar oluşturur. Girdi görüntülerini alır ve bunları harici bir servis aracılığıyla 3B modellere dönüştürür. Düğüm, görev oluşturmadan nihai 3B model dosyalarının indirilmesine kadar tüm süreci yönetir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Evet | - | 3B modellere dönüştürülecek girdi görüntüleri |
| `Seed` | INT | Hayır | 0-65535 | Üretim için rastgele tohum değeri (varsayılan: 0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | Oluşturulan 3B modelin dosya yolu |