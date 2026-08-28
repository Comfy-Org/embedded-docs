# KolayÖnbellek

```markdown
EasyCache düğümü, bir difüzyon modeline yerel bir önbellekleme sistemi ekler. Bu sistem, her adımı yeniden hesaplamak yerine önceden hesaplanmış adımların sonuçlarını yeniden kullanarak örneklemeyi hızlandırır. Yalnızca örnekleme sürecinin yapılandırılabilir bir başlangıç ve bitiş noktası arasında etkinleşir ve tahmini çıktı değişimi kullanıcı tanımlı bir eşiğin altında kaldığında adımları atlar. Bu, ileri düzey hata ayıklama kullanımı için tasarlanmış deneysel bir düğümdür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | EasyCache'in ekleneceği model. | MODEL | Evet | - |
| `yeniden_kullanım_eşiği` | Önbelleğe alınan adımları yeniden kullanma eşiği (varsayılan: 0.2). | FLOAT | Evet | 0.0 - 3.0 |
| `başlangıç_yüzdesi` | EasyCache kullanımına başlamak için göreli örnekleme adımı (varsayılan: 0.15). | FLOAT | Evet | 0.0 - 1.0 |
| `bitiş_yüzdesi` | EasyCache kullanımını sonlandırmak için göreli örnekleme adımı (varsayılan: 0.95). | FLOAT | Evet | 0.0 - 1.0 |
| `ayrıntılı` | Ayrıntılı bilgilerin günlüğe kaydedilip kaydedilmeyeceği (varsayılan: False). | BOOLEAN | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | EasyCache işlevi eklenmiş model. | MODEL |
```

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/tr.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
