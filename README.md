# aiohttp bad words

If you tell aiohttp a bad word, it'll get lost and can't reply. Not sure the pattern, but in general the "OK" words *always* seem to start with one of `DEFIJKQVWXYZ`. If you try to jam too many requests through (increasing `n` in `client.py`), there appear to be false-stuck methods, probably because of some overload.

## Environment

* Python 3.7.2
* aiohttp 3.5.4

## Testing

1. Start `python server.py`

2. Run the client code:

```
➜ python client.py
OK
['DESERTED', 'DEVIOUS', 'DISPROPORTIONATELY', 'DOLLIE', 'ELECTRIFY',
'ELLIPSES', 'ENTICEMENT', 'ERIKA', 'FIREPLACE', 'FLANKED', 'FOURTHLY',
'IMAGERY', 'INADEQUATELY', 'INCREASED', 'INNOCENTLY', 'JENNA',
'JUGGERNAUTS', 'JUMPIER', 'JURIES', 'KIPPER', 'KNOTTIER', 'KNOWINGS',
'KNOX', 'QUARREL', 'QUASHES', 'QUAVERING', 'QUOTABLE', 'VARIATIONS',
'VILLAGERS', 'VOCATIVES', 'VOCIFERATING', 'WANDA', 'WEER', 'WHIR',
'WRONGING', 'X', 'XIMENES', 'XUZHOU', 'XYLOPHONISTS', 'YEARBOOKS',
'YENISEI', 'YOU', 'YUCKED', 'Z', 'ZANZIBAR', 'ZUCCHINI']

STUCK
['ADOPTION', 'AUDITORY', 'AUTOMATES', 'BATTLES', 'BESIDE', 'BRAZENED',
'BUDGERIGAR', 'CACOPHONY', 'CANVASS', 'CONSTRUCTS', 'CONTRADICTS',
'GARBLING', 'GATE', 'GLIDERS', 'GRIDIRONS', 'HEARER', 'HECTOR',
'HOLSTER', 'HUNS', 'LACTOSE', 'LIQUEFACTION', 'LOFT', 'MALLEABLE',
'MASHERS', 'MERRYMAKERS', 'MONASTICS', 'NEGLIGENT', 'NICK', 'NORTH',
'NUZZLED', 'OBJECTORS', 'OLIGARCHY', 'OPERATING', 'OVERBURDENING',
'PLATENS', 'POLICE', 'PRESUMING', 'PUNISHES', 'RACKETING',
'RASTAFARIANISM', 'RESENTMENT', 'ROZELLE', 'SCANDINAVIAN', 'SEREST',
'SPURRING', 'SUMERIA', 'THRESHERS', 'TIGRESS', 'TRAVERSE',
'TRUCKLOADS', 'UNBENDS', 'UNCTIONS', 'UNDERLAY', 'UNIT']
```
