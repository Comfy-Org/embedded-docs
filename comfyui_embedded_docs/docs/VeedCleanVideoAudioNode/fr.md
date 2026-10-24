# VEED Clean Audio (in Video)

Supprimez le bruit de fond de la parole dans une vidéo avec VEED. Seule la bande-son change : elle est remplacée par la parole nettoyée en mono à 48 kHz, tandis que l'image, la résolution et la fréquence d'images restent inchangées. Ce traitement est conçu pour la parole dans n'importe quelle langue ; la musique et les effets sonores sont supprimés plutôt que conservés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `video` | Vidéo avec une bande-son de parole, d'une durée inférieure à 30 minutes. La vidéo doit avoir une piste audio. | VIDEO | Oui | Jusqu'à 1799 secondes |
| `strength` | Quantité de bruit supprimée sous la parole. Une valeur plus faible conserve davantage de bruit ambiant derrière la voix ; les pauses entre les mots sont toujours entièrement nettoyées, et les valeurs supérieures à la valeur par défaut modifient peu le résultat. (valeur par défaut : 0.874) | FLOAT | Oui | 0.0 à 1.0 (incrément de 0.001) |
| `loudness` | Indique s'il faut normaliser l'intensité sonore de la parole. `"normalize"` la définit sur `target_lufs` ; `"keep input level"` laisse le niveau tel quel. La sélection d'une option révèle ses paramètres. (valeur par défaut : `"normalize"`) | DYNAMIC_COMBO | Oui | `"normalize"`<br>`"keep input level"` |
| `target_lufs` | Intensité sonore intégrée de la parole nettoyée en LUFS. Les crêtes sont plafonnées à -1.1 dBTP, de sorte que les cibles fortes s'arrêtent tôt (environ -15 LUFS pour une parole typique). Disponible lorsque `loudness` vaut `"normalize"` (valeur par défaut : -19.0). | FLOAT | Oui | -40.0 à -8.0 (incrément de 0.1) |

Le nœud s'arrête avec une erreur lorsque le clip dure plus de 1799 secondes et lorsque la vidéo ne contient pas de piste audio.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `VIDEO` | La vidéo d'entrée dont la bande-son a été remplacée par la parole nettoyée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedCleanVideoAudioNode/fr.md)

---
**Source fingerprint (SHA-256):** `b8ff533f3ce45691cccd3449596252b0216178fdef0e7e728ccccbc9a8712217`
