# FreeU_V2

FreeU_V2 düğümü, bir difüzyon modelinin U-Net mimarisine frekans tabanlı değişiklikler uygulayarak görüntü üretim kalitesini artırır. Farklı bloklardaki özellik kanallarını ayarlamak için yapılandırılabilir ölçekleme faktörleri kullanır; ek eğitim gerektirmeden çıktıyı iyileştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | FreeU iyileştirmesinin uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `b1` | İlk blok için backbone özellik ölçekleme faktörü (varsayılan: 1.3) | FLOAT | Evet | 0.0 - 10.0 |
| `b2` | İkinci blok için backbone özellik ölçekleme faktörü (varsayılan: 1.4) | FLOAT | Evet | 0.0 - 10.0 |
| `s1` | İlk blok için skip özellik ölçekleme faktörü (varsayılan: 0.9) | FLOAT | Evet | 0.0 - 10.0 |
| `s2` | İkinci blok için skip özellik ölçekleme faktörü (varsayılan: 0.2) | FLOAT | Evet | 0.0 - 10.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | FreeU değişiklikleri uygulanmış geliştirilmiş difüzyon modeli | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/tr.md)

---
**Source fingerprint (SHA-256):** `4cef2af9b04164a8ead25bea9c9bb3311be9224f2539a5cc6edbe97ad8465d65`
