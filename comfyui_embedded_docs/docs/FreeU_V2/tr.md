# FreeU_V2

FreeU_V2, bir difüzyon modelinin U-Net mimarisine frekans tabanlı değişiklikler uygulayarak görüntü üretim kalitesini artırır. Ek eğitim gerektirmeden çıktıyı iyileştirmek için farklı bloklardaki özellik kanallarını ayarlamak üzere yapılandırılabilir ölçekleme faktörleri kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | FreeU iyileştirmesinin uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `b1` | İlk blok için omurga özelliği ölçekleme faktörü (varsayılan: 1.3) | FLOAT | Evet | 0.0 - 10.0 |
| `b2` | İkinci blok için omurga özelliği ölçekleme faktörü (varsayılan: 1.4) | FLOAT | Evet | 0.0 - 10.0 |
| `s1` | İlk blok için atlama özelliği ölçekleme faktörü (varsayılan: 0.9) | FLOAT | Evet | 0.0 - 10.0 |
| `s2` | İkinci blok için atlama özelliği ölçekleme faktörü (varsayılan: 0.2) | FLOAT | Evet | 0.0 - 10.0 |

Not: `b1`, `b2`, `s1` ve `s2`, düğümün arayüzünde varsayılan olarak gizlenen gelişmiş parametrelerdir. 0.0 - 10.0 aralığında 0.01 adımlarla ayarlanabilirler. `b1` ve `s1`, en fazla kanala sahip U-Net bloğunu kontrol ederken, `b2` ve `s2` yarısı kadar kanala sahip bloğu kontrol eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | FreeU değişiklikleri uygulanmış geliştirilmiş difüzyon modeli | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/tr.md)

---
**Source fingerprint (SHA-256):** `4cef2af9b04164a8ead25bea9c9bb3311be9224f2539a5cc6edbe97ad8465d65`
