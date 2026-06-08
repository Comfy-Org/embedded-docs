Birleştirme Kancaları [8] düğümü, en fazla sekiz farklı kanca grubunu tek bir birleşik kanca grubunda birleştirir. Birden fazla kanca girişi alır ve bunları ComfyUI'nin kanca birleştirme işlevselliğini kullanarak birleştirir. Bu, gelişmiş iş akışlarında daha verimli işleme için birden fazla kanca yapılandırmasını tek bir noktada toplamanıza olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Giriş Türü | Varsayılan | Aralık |
| --- | --- | --- | --- | --- | --- |
| `hooks_A` | Birleştirilecek ilk kanca grubu | HOOKS | isteğe bağlı | Yok | - |
| `hooks_B` | Birleştirilecek ikinci kanca grubu | HOOKS | isteğe bağlı | Yok | - |
| `hooks_C` | Birleştirilecek üçüncü kanca grubu | HOOKS | isteğe bağlı | Yok | - |
| `hooks_D` | Birleştirilecek dördüncü kanca grubu | HOOKS | isteğe bağlı | Yok | - |
| `hooks_E` | Birleştirilecek beşinci kanca grubu | HOOKS | isteğe bağlı | Yok | - |
| `hooks_F` | Birleştirilecek altıncı kanca grubu | HOOKS | isteğe bağlı | Yok | - |
| `hooks_G` | Birleştirilecek yedinci kanca grubu | HOOKS | isteğe bağlı | Yok | - |
| `hooks_H` | Birleştirilecek sekizinci kanca grubu | HOOKS | isteğe bağlı | Yok | - |

**Not:** Tüm giriş parametreleri isteğe bağlıdır. Düğüm, yalnızca sağlanan kanca gruplarını birleştirir ve boş bırakılanları yok sayar. Birleştirme için bir ila sekiz arasında kanca grubu sağlayabilirsiniz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `HOOKS` | Sağlanan tüm kanca yapılandırmalarını içeren tek bir birleşik kanca grubu | HOOKS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksEight/tr.md)

---
**Source fingerprint (SHA-256):** `8cd13ec6710a9b2905c14301cfd15be616c00f1b4140451cdf0915f091c77197`
