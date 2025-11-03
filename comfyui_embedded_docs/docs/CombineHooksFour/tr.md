> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksFour/tr.md)

Combine Hooks [4] düğümü, en fazla dört ayrı hook grubunu tek bir birleşik hook grubunda birleştirir. Mevcut dört hook girişinin herhangi bir kombinasyonunu alır ve ComfyUI'nin hook birleştirme sistemi kullanarak bunları birleştirir. Bu, gelişmiş iş akışlarında kolaylaştırılmış işlem için birden fazla hook yapılandırmasını birleştirmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `hooks_A` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek ilk hook grubu |
| `hooks_B` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek ikinci hook grubu |
| `hooks_C` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek üçüncü hook grubu |
| `hooks_D` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek dördüncü hook grubu |

**Not:** Dört hook girişinin tümü isteğe bağlıdır. Düğüm yalnızca sağlanan hook gruplarını birleştirecek ve hiçbir giriş bağlı değilse boş bir hook grubu döndürecektir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | Sağlanan tüm hook yapılandırmalarını içeren birleşik hook grubu |