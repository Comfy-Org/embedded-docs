> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksEight/tr.md)

Combine Hooks [8] düğümü, sekiz farklı hook grubunu tek bir birleşik hook grubunda birleştirir. Birden fazla hook girdisini alır ve ComfyUI'nin hook birleştirme işlevselliğini kullanarak bunları birleştirir. Bu, gelişmiş iş akışlarında birden fazla hook yapılandırmasını birleştirerek sadeleştirilmiş işleme olanağı sağlar.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `hooks_A` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek ilk hook grubu |
| `hooks_B` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek ikinci hook grubu |
| `hooks_C` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek üçüncü hook grubu |
| `hooks_D` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek dördüncü hook grubu |
| `hooks_E` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek beşinci hook grubu |
| `hooks_F` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek altıncı hook grubu |
| `hooks_G` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek yedinci hook grubu |
| `hooks_H` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek sekizinci hook grubu |

**Not:** Tüm girdi parametreleri isteğe bağlıdır. Düğüm yalnızca sağlanan hook gruplarını birleştirecek ve boş bırakılanları yok sayacaktır. Birleştirme için bir ile sekiz arasında hook grubu sağlayabilirsiniz.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | Sağlanan tüm hook yapılandırmalarını içeren tek bir birleşik hook grubu |