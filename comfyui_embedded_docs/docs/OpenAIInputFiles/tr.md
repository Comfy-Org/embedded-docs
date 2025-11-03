> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIInputFiles/tr.md)

OpenAI API için giriş dosyalarını yükler ve biçimlendirir. Bu düğüm, OpenAI Chat Düğümü için bağlam girdisi olarak eklemek üzere metin ve PDF dosyalarını hazırlar. Dosyalar, yanıtlar oluşturulurken OpenAI modeli tarafından okunacaktır. Tek bir mesaja birden fazla dosya eklemek için birden fazla giriş dosyası düğümü birbirine zincirlenebilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `file` | COMBO | Evet | Birden fazla seçenek mevcut | Model için bağlam olarak eklenecek giriş dosyaları. Şu an için yalnızca metin (.txt) ve PDF (.pdf) dosyaları kabul edilir. Dosyalar 32MB'tan küçük olmalıdır. |
| `OPENAI_INPUT_FILES` | OPENAI_INPUT_FILES | Hayır | Yok | Bu düğümden yüklenen dosya ile birlikte toplu işlemek için isteğe bağlı ek dosya(lar). Giriş dosyalarının zincirlenmesine izin vererek tek bir mesajın birden fazla giriş dosyası içermesini sağlar. |

**Dosya Kısıtlamaları:**

- Yalnızca .txt ve .pdf dosyaları desteklenir
- Maksimum dosya boyutu: 32MB
- Dosyalar giriş dizininden yüklenir

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `OPENAI_INPUT_FILES` | OPENAI_INPUT_FILES | OpenAI API çağrıları için bağlam olarak kullanılmaya hazır biçimlendirilmiş giriş dosyaları. |