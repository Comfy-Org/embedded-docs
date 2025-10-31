> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/tr.md)

ModelComputeDtype düğümü, bir modelin çıkarım sırasında kullandığı hesaplama veri türünü değiştirmenize olanak tanır. Girdi modelinin bir kopyasını oluşturur ve belirtilen veri türü ayarını uygular; bu, donanım özelliklerinize bağlı olarak bellek kullanımını ve performansı optimize etmenize yardımcı olabilir. Bu özellik özellikle farklı hassasiyet ayarlarını hata ayıklama ve test etme için kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Yeni bir hesaplama veri türü uygulanacak girdi modeli |
| `dtype` | STRING | Evet | "default"<br>"fp32"<br>"fp16"<br>"bf16" | Modele uygulanacak hesaplama veri türü |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Yeni hesaplama veri türü uygulanmış değiştirilmiş model |