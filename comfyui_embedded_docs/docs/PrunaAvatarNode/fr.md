# Pruna P-Video-2 Pro Avatar

Transformez un portrait en vidéo parlante avec Pruna P-Video-2 Pro Avatar. Faites lire un script par synthèse vocale, ou connectez votre propre audio et la personne y synchronisera ses lèvres.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Portrait à partir duquel la vidéo démarre. Les ratios d'aspect de 1:2 à 4:1 sont conservés ; les images plus extrêmes, comme 1:5, sont recadrées en 9:16 ou 16:9. | IMAGE | Oui | - |
| `parole` | Pilote la vidéo avec un script lu par synthèse vocale ou avec votre propre audio. La sélection d'une option affiche ses entrées ci-dessous. | DYNAMIC_COMBO | Oui | `"script"`<br>`"audio"` |
| `prompt` | Décrit ce que montre la vidéo (par défaut : "The person is talking."). Jusqu'à 5000 caractères. | STRING | Oui | Jusqu'à 5000 caractères |
| `résolution` | Résolution de sortie (par défaut : `"768p"`). Les résolutions 1080p, 2k et 4k augmentent la résolution de la vidéo générée en 768p. | COMBO | Oui | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `enhance_prompt` | Ajoute au prompt le mouvement observé dans le portrait, tel que l'arrière-plan, les lumières et les mouvements du corps (par défaut : True). Paramètre avancé. | BOOLEAN | Oui | `True`<br>`False` |
| `seed` | Graine de génération (par défaut : 42). La même graine ne reproduit un résultat à l'identique que lorsque `enhance_prompt` est désactivé. | INT | Oui | 0 à 2147483647<br>Pas : 1 |

### Entrées `"script"`

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `script` | Mots prononcés par la personne. La vidéo correspond à la durée de la parole, et une parole de plus de 3 minutes est coupée à 3 minutes. | STRING | Oui | Texte libre |
| `voix` | Voix utilisée pour la parole (par défaut : `"Zephyr (Female)"`). | COMBO | Oui | 30 voix prédéfinies |
| `langue` | Langue dans laquelle le script est prononcé (par défaut : `"English (US)"`). | COMBO | Oui | `"English (US)"`<br>`"English (UK)"`<br>`"Spanish"`<br>`"French"`<br>`"German"`<br>`"Italian"`<br>`"Portuguese (Brazil)"`<br>`"Japanese"`<br>`"Korean"`<br>`"Hindi"` |
| `voice_prompt` | Comment le script est prononcé : ton, rythme, accent, émotion (par défaut : "Say the following."). Ce texte n'est pas prononcé. | STRING | Oui | Texte libre |

### Entrées `"audio"`

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `speech.audio` | Parole que la personne synchronise avec ses lèvres. La vidéo correspond à sa durée. | AUDIO | Oui | Au moins 1 seconde |

**Remarques :**

- Une résolution de sortie plus élevée limite la durée de l'audio : la 2k accepte jusqu'à 150 secondes d'audio et la 4k jusqu'à 60 secondes. Un audio plus long à ces résolutions arrête le nœud avec une erreur ; utilisez donc une résolution plus basse ou un extrait plus court.
- Le ratio d'aspect du portrait détermine la forme de la sortie. Les portraits très hauts ou très larges sont recadrés plutôt que complétés par des marges ; gardez donc le sujet éloigné des bords.
- Lorsque `enhance_prompt` est désactivé, le prompt est utilisé tel qu'écrit, ce qui permet à la même graine de reproduire un résultat à l'identique.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo parlante générée à partir du portrait. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaAvatarNode/fr.md)

---
**Source fingerprint (SHA-256):** `58efc7a110734f8da0a771371c5230908bf8226a946d69c5315e51e259630043`
