# VEED Clean Audio

Retirez le bruit de fond des enregistrements vocaux avec VEED. Il est conçu pour la parole dans n'importe quelle langue : le bruit sous la voix est nettoyé, les pauses sont complètement nettoyées, et la musique et les effets sonores sont supprimés plutôt que préservés. La sortie est un audio mono à 48 kHz.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | Enregistrement vocal, d'une durée inférieure à 30 minutes. | AUDIO | Oui | Jusqu'à 1799 secondes |
| `strength` | Quantité de bruit supprimée sous la parole. Une valeur plus faible conserve davantage de bruit de fond derrière la voix ; les pauses entre les mots sont toujours entièrement nettoyées, et les valeurs supérieures à la valeur par défaut changent peu. (par défaut : 0.874) | FLOAT | Oui | 0.0 à 1.0 (pas 0.001) |
| `loudness` | Indique s'il faut normaliser la sonie de la sortie. `"normalize"` définit la sortie sur `target_lufs` ; `"keep input level"` laisse le niveau tel quel. La sélection d'une option révèle ses paramètres. (par défaut : `"normalize"`) | DYNAMIC_COMBO | Oui | `"normalize"`<br>`"keep input level"` |
| `target_lufs` | Sonie intégrée de la sortie en LUFS. Les crêtes sont plafonnées à -1.1 dBTP, de sorte que les cibles élevées s'arrêtent prématurément (environ -15 LUFS pour une parole typique). Disponible lorsque `loudness` est `"normalize"` (par défaut : -19.0). | FLOAT | Oui | -40.0 à -8.0 (pas 0.1) |

Le nœud s'arrête avec une erreur lorsque l'enregistrement dure plus de 1799 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `AUDIO` | La parole nettoyée en audio mono à 48 kHz. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedCleanAudioNode/fr.md)

---
**Source fingerprint (SHA-256):** `c85949385109a5d320e52619e9df17c245b19f8f16cc1a0b69a37ae2e7bb5b6d`
