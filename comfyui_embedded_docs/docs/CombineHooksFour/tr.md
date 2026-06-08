**Birleştirme Kancaları [4]**

Birleştirme Kancaları [4] düğümü, en fazla dört ayrı kanca grubunu tek bir birleşik kanca grubunda birleştirir. Mevcut dört kanca girişinin herhangi bir kombinasyonunu alır ve ComfyUI'nin kanca birleştirme sistemini kullanarak bunları birleştirir. Bu, gelişmiş iş akışlarında birden fazla kanca yapılandırmasını tek bir noktada toplayarak işlemleri kolaylaştırmanıza olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Giriş Türü | Varsayılan | Aralık |
| --- | --- | --- | --- | --- | --- |
| `hooks_A` | Birleştirilecek ilk kanca grubu | HOOKS | isteğe bağlı | Yok | - |
| `hooks_B` | Birleştirilecek ikinci kanca grubu | HOOKS | isteğe bağlı | Yok | - |
| `hooks_C` | Birleştirilecek üçüncü kanca grubu | HOOKS | isteğe bağlı | Yok | - |
| `hooks_D` | Birleştirilecek dördüncü kanca grubu | HOOKS | isteğe bağlı | Yok | - |

**Not:** Dört kanca girişinin tümü isteğe bağlıdır. Düğüm, yalnızca sağlanan kanca gruplarını birleştirir ve hiçbir giriş bağlı değilse boş bir kanca grubu döndürür.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `HOOKS` | Sağlanan tüm kanca yapılandırmalarını içeren birleşik kanca grubu | HOOKS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksFour/tr.md)

---
**Source fingerprint (SHA-256):** `92a8038e7b5a7491afcbd48830a1e278fe4d697321fb874821ebf7edd09d5815`
