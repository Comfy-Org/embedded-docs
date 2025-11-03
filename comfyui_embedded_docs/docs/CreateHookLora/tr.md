> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLora/tr.md)

Create Hook LoRA düğümü, modellere LoRA (Düşük Ranklı Adaptasyon) değişiklikleri uygulamak için kanca nesneleri oluşturur. Belirtilen bir LoRA dosyasını yükler ve model ile CLIP güçlerini ayarlayabilen kancalar oluşturur, ardından bu kancaları kendisine iletilen mevcut kancalarla birleştirir. Düğüm, gereksiz işlemleri önlemek için önceden yüklenmiş LoRA dosyalarını önbelleğe alarak LoRA yüklemesini verimli bir şekilde yönetir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `lora_adı` | STRING | Evet | Birden fazla seçenek mevcut | loras dizininden yüklenecek LoRA dosyasının adı |
| `model_gücü` | FLOAT | Evet | -20.0 ile 20.0 arası | Model ayarlamaları için güç çarpanı (varsayılan: 1.0) |
| `clip_gücü` | FLOAT | Evet | -20.0 ile 20.0 arası | CLIP ayarlamaları için güç çarpanı (varsayılan: 1.0) |
| `önceki_kancalar` | HOOKS | Hayır | Yok | Yeni LoRA kancalarıyla birleştirilecek isteğe bağlı mevcut kanca grubu |

**Parametre Kısıtlamaları:**

- Hem `strength_model` hem de `strength_clip` 0 olarak ayarlandıysa, düğüm yeni LoRA kancaları oluşturmayı atlayacak ve mevcut kancaları değiştirmeden döndürecektir
- Düğüm, aynı LoRA tekrar tekrar kullanıldığında performansı optimize etmek için en son yüklenen LoRA dosyasını önbelleğe alır

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | Birleştirilmiş LoRA kancalarını ve varsa önceki kancaları içeren bir kanca grubu |