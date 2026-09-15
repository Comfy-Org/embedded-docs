# EndLoop

End Loop, bir döngü bloğunun sonunu işaretler. Döngü gövdesindeki son düğüm tarafından üretilen değeri toplar ve `accumulate` ayarına bağlı olarak yalnızca son yinelemeyi ya da her yinelemeyi döndürür; ayrıca sonraki yinelemenin başlayabilmesi için Start Loop'a bir değer geri gönderir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `output_value` | End Loop tarafından döndürülen değer. `accumulate` değerine göre son yinelemeyi veya tüm yinelemeleri döndürür. | ANY | Hayır | Herhangi bir değer türü |
| `next_iteration_value` | Sonraki yineleme için End Loop'tan Start Loop'a geri gönderilen değer. | ANY | Hayır | Herhangi bir değer türü |
| `accumulate` | Etkinleştirildiğinde her yinelemeden output_value değerini döndürür; aksi halde yalnızca son yinelemeyi döndürür. | BOOLEAN | Hayır | `true`<br>`false` (varsayılan: `false`) |
| `terminations` | Her yinelemede yürütülmesi gereken çıktıları bağlayın. Değerleri döndürülmez. `termination_1`, `termination_2` vb. adlarla büyütülebilir yuvalar. | ANY | Hayır | 0 ila 50 yuva |

Not: `terminations`, en az 0 ve en fazla 50 bağlantıya sahip büyütülebilir bir yuva listesidir. Buraya bağlanan değerler her yinelemede yürütmeyi zorlar ancak döndürülen sonucun parçası değildir.

Not: Bu düğüm bir girdi listesi düğümüdür, bu nedenle girdileri her döngü yinelemesinden toplanan değerleri alır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `outputs` | Son yinelemenin output_value değeri veya `accumulate` etkinleştirildiğinde yinelemeler boyunca biriktirilen değerler. | ANY (list) |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EndLoop/tr.md)

---
**Source fingerprint (SHA-256):** `473ba61d8e6fecdd1205297e2c602e3fd821044aff87d15a3f4b7646748d9999`
