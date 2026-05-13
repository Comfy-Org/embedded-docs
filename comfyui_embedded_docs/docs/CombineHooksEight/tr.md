> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksEight/tr.md)

Birleştirme Kancaları [8] düğümü, en fazla sekiz farklı kanca grubunu tek bir birleşik kanca grubunda birleştirir. Birden fazla kanca girişi alır ve bunları ComfyUI'nin kanca birleştirme işlevselliğini kullanarak birleştirir. Bu, gelişmiş iş akışlarında daha verimli işleme için birden fazla kanca yapılandırmasını tek bir noktada toplamanıza olanak tanır.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `hooks_A` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek ilk kanca grubu |
| `hooks_B` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek ikinci kanca grubu |
| `hooks_C` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek üçüncü kanca grubu |
| `hooks_D` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek dördüncü kanca grubu |
| `hooks_E` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek beşinci kanca grubu |
| `hooks_F` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek altıncı kanca grubu |
| `hooks_G` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek yedinci kanca grubu |
| `hooks_H` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek sekizinci kanca grubu |

**Not:** Tüm giriş parametreleri isteğe bağlıdır. Düğüm, yalnızca sağlanan kanca gruplarını birleştirir ve boş bırakılanları yok sayar. Birleştirme için bir ila sekiz arasında kanca grubu sağlayabilirsiniz.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | Sağlanan tüm kanca yapılandırmalarını içeren tek bir birleşik kanca grubu |

---
**Source fingerprint (SHA-256):** `8cd13ec6710a9b2905c14301cfd15be616c00f1b4140451cdf0915f091c77197`
