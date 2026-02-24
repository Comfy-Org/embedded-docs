> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanReferenceVideoApi/fr.md)

Le nœud Wan Reference to Video utilise l'apparence visuelle et la voix d'une ou plusieurs vidéos de référence en entrée, ainsi qu'une invite textuelle, pour générer une nouvelle vidéo. Il maintient la cohérence avec les personnages issus du matériel de référence tout en créant un nouveau contenu basé sur votre description.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | `"wan2.6-r2v"` | Le modèle d'IA spécifique à utiliser pour la génération vidéo. |
| `prompt` | STRING | Oui | - | Une description des éléments et des caractéristiques visuelles pour la nouvelle vidéo. Prend en charge l'anglais et le chinois. Utilisez des identifiants comme `character1` et `character2` pour faire référence aux personnages des vidéos de référence. |
| `negative_prompt` | STRING | Non | - | Une description des éléments ou caractéristiques à éviter dans la vidéo générée. |
| `reference_videos` | AUTOGROW | Oui | - | Une liste de vidéos d'entrée utilisées comme références pour l'apparence et la voix des personnages. Vous devez fournir au moins une vidéo. Chaque vidéo peut se voir attribuer un nom comme `character1`, `character2` ou `character3`. |
| `size` | COMBO | Oui | `"720p: 1:1 (960x960)"`<br>`"720p: 16:9 (1280x720)"`<br>`"720p: 9:16 (720x1280)"`<br>`"720p: 4:3 (1088x832)"`<br>`"720p: 3:4 (832x1088)"`<br>`"1080p: 1:1 (1440x1440)"`<br>`"1080p: 16:9 (1920x1080)"`<br>`"1080p: 9:16 (1080x1920)"`<br>`"1080p: 4:3 (1632x1248)"`<br>`"1080p: 3:4 (1248x1632)"` | La résolution et le format d'image pour la vidéo de sortie. |
| `duration` | INT | Oui | 5 à 10 | La durée de la vidéo générée en secondes. La valeur doit être un multiple de 5 (par défaut : 5). |
| `seed` | INT | Non | 0 à 2147483647 | Une valeur de graine aléatoire pour des résultats reproductibles. Une valeur de 0 générera une graine aléatoire. |
| `shot_type` | COMBO | Oui | `"single"`<br>`"multi"` | Spécifie si la vidéo générée est un plan unique continu ou contient plusieurs plans avec des coupures. |
| `watermark` | BOOLEAN | Non | - | Lorsqu'activé, un filigrane généré par IA est ajouté à la vidéo finale (par défaut : Faux). |

**Contraintes :**

* Chaque vidéo fournie dans `reference_videos` doit avoir une durée comprise entre 2 et 30 secondes.
* Le paramètre `duration` est limité à des valeurs spécifiques (5 ou 10 secondes).

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le nouveau fichier vidéo généré. |
