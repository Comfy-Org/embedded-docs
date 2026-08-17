# ModelHesaplamaVeriTürü

ModelComputeDtype düğümü, bir modelin işleme sırasında kullandığı hesaplama veri türünü (hassasiyet) değiştirir. Girdi modelinin bir kopyasını oluşturur ve seçilen hassasiyet ayarını uygular; bu, donanımınıza bağlı olarak bellek kullanımını ve performansı optimize etmeye yardımcı olabilir. Bu, farklı hassasiyet yapılandırmalarını hata ayıklamak ve test etmek için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Yeni hesaplama veri türüyle değiştirilecek girdi modeli | MODEL | Evet | - |
| `dtype` | Modele uygulanacak hesaplama veri türü (varsayılan: "default"). Bu parametre, arayüzde gelişmiş bir ayar olarak işaretlenmiştir. | COMBO | Evet | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Yeni hesaplama veri türü uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/tr.md)

---
**Source fingerprint (SHA-256):** `ad9c39e1217fd2e343ad4f49df9d1acabbc4708966dadec5340bb975adb59854`
