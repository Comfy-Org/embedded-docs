# Kanca Anahtar Karelerini Ayarla

Set Hook Keyframes düğümü, mevcut hook gruplarına anahtar kare zamanlaması uygulamanızı sağlar. Bir hook grubu alır ve isteğe bağlı olarak, üretim sürecinde farklı hook'ların ne zaman çalıştırılacağını kontrol etmek için anahtar kare zamanlama bilgisi uygular. Anahtar kareler sağlandığında, düğüm hook grubunu kopyalar ve gruptaki tüm hook'lara anahtar kare zamanlamasını ayarlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `kancalar` | Anahtar kare zamanlamasının uygulanacağı hook grubu | HOOKS | Evet | - |
| `kanca_kf` | Hook yürütme zamanlaması bilgilerini içeren isteğe bağlı anahtar kare grubu | HOOK_KEYFRAMES | Hayır | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `kancalar` | Anahtar kare zamanlaması uygulanmış değiştirilmiş hook grubu (anahtar kareler sağlandıysa kopyalanmıştır) | HOOKS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetHookKeyframes/tr.md)

---
**Source fingerprint (SHA-256):** `48908e5247b18e5b7b1d894c2f1adcf6403e499125b0c3eb05978584b3d5759b`
