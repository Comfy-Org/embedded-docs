> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetHookKeyframes/tr.md)

Set Hook Keyframes düğümü, mevcut hook gruplarına kare animasyonu planlama uygulamanızı sağlar. Bir hook grubu alır ve isteğe bağlı olarak, üretim süreci boyunca farklı hook'ların ne zaman çalıştırılacağını kontrol etmek için kare animasyonu zamanlama bilgisi uygular. Kare animasyonları sağlandığında, düğüm hook grubunu klonlar ve gruptaki tüm hook'lara kare animasyonu zamanlamasını ayarlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `hooks` | HOOKS | Evet | - | Kare animasyonu planlamasının uygulanacağı hook grubu |
| `hook_kf` | HOOK_KEYFRAMES | Hayır | - | Hook çalıştırma için zamanlama bilgisi içeren isteğe bağlı kare animasyonu grubu |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `hooks` | HOOKS | Kare animasyonu planlaması uygulanmış değiştirilmiş hook grubu (kare animasyonları sağlandıysa klonlanmış) |