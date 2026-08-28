# VaeDecodeStructureTrellis2

Bu düğüm, VAE'nin yapı çözücüsünü kullanarak Trellis yapısı latent örneklerini 3B voxel ızgarasına dönüştürür. Latentin yalnızca ilk 8 kanalını okur, voxel doluluğunu yeniden yapılandırır ve isteğe bağlı olarak çıktı çözünürlüğünü 32 veya 64'e ayarlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `samples` | Çözülecek yapının latent temsili. Kod çözme için latentin yalnızca ilk 8 kanalı kullanılır. | LATENT | Evet | - |
| `vae` | Yapı çözücüsü latentini bir voxel ızgarasına dönüştüren VAE. Kod çözme gruplar halinde gerçekleştirilir. | VAE | Evet | - |
| `resolution` | Çıktı voxel ızgarasının hedef uzamsal çözünürlüğü (varsayılan: "32"). Kod çözülen ızgara farklı bir çözünürlükteyse, eşleşmesi için alt örneklenir. | COMBO | Evet | "32"<br>"64" |

Not: Kod çözülen voxel ızgarasının çözünürlüğü seçilen `resolution` değerinden farklıysa, ızgara istenen boyuta 3B maksimum havuzlama kullanılarak alt örneklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `voxel` | [batch, depth, height, width] boyutlarına sahip bir kayan nokta tensörü olarak ikili voxel doluluk ızgarası. Dolu voxeller için değerler 1.0, boş voxeller için 0.0'dır. | VOXEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeStructureTrellis2/tr.md)

---
**Source fingerprint (SHA-256):** `37764ef7351b3619d4cddb57b11d9a0da24dadeedc0fc0f70d089038d37e03b0`
