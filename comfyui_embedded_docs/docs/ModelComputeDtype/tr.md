> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/tr.md)

ModelComputeDtype düğümü, bir modelin işleme sırasında kullandığı hesaplama veri türünü (hassasiyetini) değiştirir. Giriş modelinin bir kopyasını oluşturur ve seçilen hassasiyet ayarını uygular; bu, donanımınıza bağlı olarak bellek kullanımını ve performansı optimize etmeye yardımcı olabilir. Farklı hassasiyet yapılandırmalarını hata ayıklama ve test etme için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | MODEL | Evet | - | Yeni bir hesaplama veri türüyle değiştirilecek giriş modeli |
| `veri_türü` | STRING | Evet | "default"<br>"fp32"<br>"fp16"<br>"bf16" | Modele uygulanacak hesaplama veri türü (varsayılan: "default") |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | Yeni hesaplama veri türü uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `bc65f1e452d0122ad175a8b95f38a36503253c9908157037c516496e65c828e6`
