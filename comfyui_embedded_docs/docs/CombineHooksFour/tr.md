> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksFour/tr.md)

**Birleştirme Kancaları [4]**

Birleştirme Kancaları [4] düğümü, en fazla dört ayrı kanca grubunu tek bir birleşik kanca grubunda birleştirir. Mevcut dört kanca girişinin herhangi bir kombinasyonunu alır ve ComfyUI'nin kanca birleştirme sistemini kullanarak bunları birleştirir. Bu, gelişmiş iş akışlarında birden fazla kanca yapılandırmasını tek bir noktada toplayarak işlemleri kolaylaştırmanıza olanak tanır.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|------------|--------|----------|
| `hooks_A` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek ilk kanca grubu |
| `hooks_B` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek ikinci kanca grubu |
| `hooks_C` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek üçüncü kanca grubu |
| `hooks_D` | HOOKS | isteğe bağlı | Yok | - | Birleştirilecek dördüncü kanca grubu |

**Not:** Dört kanca girişinin tümü isteğe bağlıdır. Düğüm, yalnızca sağlanan kanca gruplarını birleştirir ve hiçbir giriş bağlı değilse boş bir kanca grubu döndürür.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `HOOKS` | HOOKS | Sağlanan tüm kanca yapılandırmalarını içeren birleşik kanca grubu |

---
**Source fingerprint (SHA-256):** `92a8038e7b5a7491afcbd48830a1e278fe4d697321fb874821ebf7edd09d5815`
