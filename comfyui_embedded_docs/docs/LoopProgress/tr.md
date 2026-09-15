# LoopProgress

LoopProgress, bir döngünün ilerlemesini ComfyUI sunucu arayüzüne bildiren yalnızca geliştirme amaçlı bir yardımcı düğümdür. Her yürütmede istemciye "Iteration X / Y" metnini gönderir ve mevcut yineleme konumunu değiştirmeden döndürür; bu sayede veri akışını değiştirmeden bir döngünün içine satır içi olarak yerleştirilebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `start_id` | İlerleme mesajının ait olduğu istem/döngü örneğinin tanımlayıcısı. Sağlanan listenin ilk öğesi, ilerleme metnini doğru çalışan yürütmeye yönlendirmek için kullanılır. | STRING | Evet | - |
| `position` | Mevcut yineleme konumu (dizin). Sağlanan listenin ilk öğesi ilerleme mesajında kullanılır ve çıktı olarak da döndürülür. | INT | Evet | - |
| `total` | Toplam yineleme sayısı. "Iteration X / Y" ilerleme mesajını oluşturmak için `position` ile birlikte kullanılır. | INT | Evet | - |

Not: Bu düğüm liste girdileriyle (`is_input_list=True`) tanımlanmıştır ve tüm girdileri kabul eder; bu nedenle bağlanan her değer bir liste olarak işlenir ve yalnızca ilk öğesi okunur. Düğüm her zaman çalışır (girdi parmak izi sabittir), dolayısıyla her döngü geçişinde yeniden yürütülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `position` | Mevcut yineleme konumu; `position` girdisinden değiştirilmeden geçirilir. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopProgress/tr.md)

---
**Source fingerprint (SHA-256):** `505ba814b93533679516b4f4239f5eee0dbac125d7ea16746c6cdbb7a68f803d`
