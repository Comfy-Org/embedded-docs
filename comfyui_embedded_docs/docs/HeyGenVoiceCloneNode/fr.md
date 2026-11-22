# HeyGen Voice 1.0 Instant Clone

Clonez une voix à partir d’un enregistrement d’un seul locuteur avec le moteur Voice 1.0 de HeyGen. Le nœud téléverse l’enregistrement, crée un clone vocal instantané, attend que HeyGen termine son traitement, puis renvoie le `voice_id`. Connectez-le à HeyGen Voice 1.0 Text to Speech, ou à `custom_voice_id` dans HeyGen Avatar Video et HeyGen Talking Photo. La création du clone est gratuite ; la synthèse vocale générée avec la voix est facturée.

**Remarque :** Ce nœud est marqué comme obsolète dans le code source. Utilisez HeyGen Voice 1.0 Instant Clone Text to Speech pour cloner une voix et prononcer du texte dans un seul nœud.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | Enregistrement d’un seul locuteur. Utilisez au moins 10 secondes de parole claire ; seules les 3 premières minutes sont utilisées. | AUDIO | Oui | N/A |
| `langue` | Langue parlée dans l’enregistrement (par défaut : "auto"). | COMBO | Oui | `"auto"`<br>Plusieurs préréglages de langue |
| `similarité` | Degré de fidélité de la voix à l’enregistrement (par défaut : "max"). | COMBO | Oui | `"medium"`<br>`"high"`<br>`"extra_high"`<br>`"max"` |
| `remove_background_noise` | Nettoyer le bruit de fond dans l’enregistrement avant le clonage (par défaut : True). | BOOLEAN | Oui | True<br>False |
| `graine` | Modifiez la `seed` pour cloner à nouveau l’enregistrement ; chaque clone est une voix légèrement différente (par défaut : 42). | INT | Oui | 0 à 2147483647 |

**Remarque :** La voix est créée sous le nom « ComfyUI Voice » dans votre compte HeyGen, et le `voice_id` apparaît dans sa sortie : connectez un nœud d’affichage de texte pour le lire. Laissez `language` sur « auto » sauf si le locuteur parle une langue facilement confondue avec une langue étroitement apparentée. L’entrée `seed` inclut un contrôle fixe Control After Generate dans l’interface ; modifiez-la manuellement lorsque vous souhaitez un autre clone.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `voice_id` | ID de la voix clonée, à réutiliser dans le nœud HeyGen Voice 1.0 Text to Speech ou comme `custom_voice_id`. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceCloneNode/fr.md)

---
**Source fingerprint (SHA-256):** `a44924942311ca520e8d77d89119cb56c1b8030124ce608ae89efd72a0e2ad28`
