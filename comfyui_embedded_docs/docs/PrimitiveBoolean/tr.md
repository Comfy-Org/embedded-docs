> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoolean/tr.md)

Boolean düğümü, iş akışınızda boolean (doğru/yanlış) değerlerini iletmek için basit bir yol sağlar. Bir boolean giriş değeri alır ve aynı değeri değiştirmeden çıktı olarak verir, böylece diğer düğümlerdeki boolean parametrelerini kontrol etmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `değer` | BOOLEAN | Evet | true<br>false | Düğümden geçirilecek boolean değeri |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | BOOLEAN | Giriş olarak sağlanan aynı boolean değeri |