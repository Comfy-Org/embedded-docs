> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/tr.md)

## Genel Bakış

FreeU_V2 düğümü, bir difüzyon modelinin U-Net mimarisine frekans tabanlı değişiklikler uygulayarak görüntü üretim kalitesini artırır. Farklı bloklardaki özellik kanallarını ayarlamak için yapılandırılabilir ölçekleme faktörleri kullanır ve ek eğitim gerektirmeden çıktı kalitesini iyileştirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | MODEL | Evet | - | FreeU iyileştirmesinin uygulanacağı difüzyon modeli |
| `b1` | FLOAT | Evet | 0.0 - 10.0 | Birinci blok için omurga özellik ölçekleme faktörü (varsayılan: 1.3) |
| `b2` | FLOAT | Evet | 0.0 - 10.0 | İkinci blok için omurga özellik ölçekleme faktörü (varsayılan: 1.4) |
| `s1` | FLOAT | Evet | 0.0 - 10.0 | Birinci blok için atlama özellik ölçekleme faktörü (varsayılan: 0.9) |
| `s2` | FLOAT | Evet | 0.0 - 10.0 | İkinci blok için atlama özellik ölçekleme faktörü (varsayılan: 0.2) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | FreeU değişiklikleri uygulanmış, iyileştirilmiş difüzyon modeli |

---
**Source fingerprint (SHA-256):** `40ded64177e8e00cc5d8d5dde35c20958a77c500dada725572b64484c5ce1045`
