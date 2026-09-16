# EndLoop

End Loop, bir döngü bloğunun sonunu işaret eder. Döngü gövdesindeki son düğüm tarafından üretilen değeri toplar ve `accumulate` ayarına bağlı olarak ya yalnızca son yinelemeyi ya da tüm yinelemeleri döndürür; ayrıca bir sonraki yinelemenin başlayabilmesi için Start Loop'a bir değer geri iletir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `output_value` | End Loop tarafından döndürülen değer. `accumulate` ayarına göre son yinelemeyi veya tüm yinelemeleri döndürür. | ANY | Hayır | Herhangi bir değer türü |
| `next_iteration_value` | Bir sonraki yineleme için End Loop'tan Start Loop'a geri gönderilen değer. | ANY | Hayır | Herhangi bir değer türü |
| `accumulate` | Etkinleştirildiğinde her yinelemeden `output_value` döndürür; aksi halde yalnızca son yinelemeyi döndürür. | BOOLEAN | Hayır | `true`<br>`false` (varsayılan: `false`) |
| `terminations` | Her yinelemede yürütülmesi gereken çıktıları bağlayın. Değerleri döndürülmez. `termination_1`, `termination_2` vb. adlandırılmış büyütülebilir yuvalar. | ANY | Hayır | 0 ile 50 arası yuva |

Not: `terminations`, en az 0 ve en fazla 50 bağlantı içeren büyütülebilir bir yuva listesidir. Buraya bağlanan değerler her yinelemede yürütmeyi zorlar ancak döndürülen sonucun parçası değildir.

Not: Bu düğüm bir girdi listesi düğümüdür; bu nedenle girdileri her döngü yinelemesinden toplanan değerleri alır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `outputs` | Son yinelemenin `output_value` değeri veya `accumulate` etkinleştirildiğinde yinelemeler boyunca biriken değerler. | ANY (list) |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EndLoop/tr.md)

---
**Source fingerprint (SHA-256):** `142840dca7f238eb00c72074d265478c548ad5c047e05744d0c3715e452f795a`
