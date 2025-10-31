> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/tr.md)

FreeU_V2 düğümü, U-Net mimarisini değiştirerek difüzyon modellerine frekans tabanlı bir iyileştirme uygular. Görüntü oluşturma kalitesini ek eğitim gerektirmeden iyileştirmek için yapılandırılabilir parametreler kullanarak farklı özellik kanallarını ölçeklendirir. Düğüm, belirli kanal boyutlarına ölçeklendirme faktörleri uygulamak için modelin çıktı bloklarını yamayarak çalışır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | FreeU iyileştirmesinin uygulanacağı difüzyon modeli |
| `b1` | FLOAT | Evet | 0.0 - 10.0 | İlk blok için omurga özellik ölçeklendirme faktörü (varsayılan: 1.3) |
| `b2` | FLOAT | Evet | 0.0 - 10.0 | İkinci blok için omurga özellik ölçeklendirme faktörü (varsayılan: 1.4) |
| `s1` | FLOAT | Evet | 0.0 - 10.0 | İlk blok için atlama özellik ölçeklendirme faktörü (varsayılan: 0.9) |
| `s2` | FLOAT | Evet | 0.0 - 10.0 | İkinci blok için atlama özellik ölçeklendirme faktörü (varsayılan: 0.2) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | FreeU değişiklikleri uygulanmış iyileştirilmiş difüzyon modeli |