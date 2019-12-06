"""
Color sequences and scales from CARTO's CartoColors

Learn more at https://github.com/CartoDB/CartoColor

CARTOColors are made available under a Creative Commons Attribution license: https://creativecommons.org/licenses/by/3.0/us/
"""

from ._swatches import _swatches


def swatches(template=None):
    return _swatches(__name__, globals(), template)


swatches.__doc__ = _swatches.__doc__

Burg = [
    "rgb(255, 198, 196)",
    "rgb(244, 163, 168)",
    "rgb(227, 129, 145)",
    "rgb(204, 96, 125)",
    "rgb(173, 70, 108)",
    "rgb(139, 48, 88)",
    "rgb(103, 32, 68)",
]

Burgyl = [
    "rgb(251, 230, 197)",
    "rgb(245, 186, 152)",
    "rgb(238, 138, 130)",
    "rgb(220, 113, 118)",
    "rgb(200, 88, 108)",
    "rgb(156, 63, 93)",
    "rgb(112, 40, 74)",
]

Redor = [
    "rgb(246, 210, 169)",
    "rgb(245, 183, 142)",
    "rgb(241, 156, 124)",
    "rgb(234, 129, 113)",
    "rgb(221, 104, 108)",
    "rgb(202, 82, 104)",
    "rgb(177, 63, 100)",
]

Oryel = [
    "rgb(236, 218, 154)",
    "rgb(239, 196, 126)",
    "rgb(243, 173, 106)",
    "rgb(247, 148, 93)",
    "rgb(249, 123, 87)",
    "rgb(246, 99, 86)",
    "rgb(238, 77, 90)",
]

Peach = [
    "rgb(253, 224, 197)",
    "rgb(250, 203, 166)",
    "rgb(248, 181, 139)",
    "rgb(245, 158, 114)",
    "rgb(242, 133, 93)",
    "rgb(239, 106, 76)",
    "rgb(235, 74, 64)",
]

Pinkyl = [
    "rgb(254, 246, 181)",
    "rgb(255, 221, 154)",
    "rgb(255, 194, 133)",
    "rgb(255, 166, 121)",
    "rgb(250, 138, 118)",
    "rgb(241, 109, 122)",
    "rgb(225, 83, 131)",
]

Mint = [
    "rgb(228, 241, 225)",
    "rgb(180, 217, 204)",
    "rgb(137, 192, 182)",
    "rgb(99, 166, 160)",
    "rgb(68, 140, 138)",
    "rgb(40, 114, 116)",
    "rgb(13, 88, 95)",
]

Blugrn = [
    "rgb(196, 230, 195)",
    "rgb(150, 210, 164)",
    "rgb(109, 188, 144)",
    "rgb(77, 162, 132)",
    "rgb(54, 135, 122)",
    "rgb(38, 107, 110)",
    "rgb(29, 79, 96)",
]

Darkmint = [
    "rgb(210, 251, 212)",
    "rgb(165, 219, 194)",
    "rgb(123, 188, 176)",
    "rgb(85, 156, 158)",
    "rgb(58, 124, 137)",
    "rgb(35, 93, 114)",
    "rgb(18, 63, 90)",
]

Emrld = [
    "rgb(211, 242, 163)",
    "rgb(151, 225, 150)",
    "rgb(108, 192, 139)",
    "rgb(76, 155, 130)",
    "rgb(33, 122, 121)",
    "rgb(16, 89, 101)",
    "rgb(7, 64, 80)",
]

Aggrnyl = [
    "rgb(36, 86, 104)",
    "rgb(15, 114, 121)",
    "rgb(13, 143, 129)",
    "rgb(57, 171, 126)",
    "rgb(110, 197, 116)",
    "rgb(169, 220, 103)",
    "rgb(237, 239, 93)",
]

Bluyl = [
    "rgb(247, 254, 174)",
    "rgb(183, 230, 165)",
    "rgb(124, 203, 162)",
    "rgb(70, 174, 160)",
    "rgb(8, 144, 153)",
    "rgb(0, 113, 139)",
    "rgb(4, 82, 117)",
]

Teal = [
    "rgb(209, 238, 234)",
    "rgb(168, 219, 217)",
    "rgb(133, 196, 201)",
    "rgb(104, 171, 184)",
    "rgb(79, 144, 166)",
    "rgb(59, 115, 143)",
    "rgb(42, 86, 116)",
]

Tealgrn = [
    "rgb(176, 242, 188)",
    "rgb(137, 232, 172)",
    "rgb(103, 219, 165)",
    "rgb(76, 200, 163)",
    "rgb(56, 178, 163)",
    "rgb(44, 152, 160)",
    "rgb(37, 125, 152)",
]

Purp = [
    "rgb(243, 224, 247)",
    "rgb(228, 199, 241)",
    "rgb(209, 175, 232)",
    "rgb(185, 152, 221)",
    "rgb(159, 130, 206)",
    "rgb(130, 109, 186)",
    "rgb(99, 88, 159)",
]

Purpor = [
    "rgb(249, 221, 218)",
    "rgb(242, 185, 196)",
    "rgb(229, 151, 185)",
    "rgb(206, 120, 179)",
    "rgb(173, 95, 173)",
    "rgb(131, 75, 160)",
    "rgb(87, 59, 136)",
]

Sunset = [
    "rgb(243, 231, 155)",
    "rgb(250, 196, 132)",
    "rgb(248, 160, 126)",
    "rgb(235, 127, 134)",
    "rgb(206, 102, 147)",
    "rgb(160, 89, 160)",
    "rgb(92, 83, 165)",
]

Magenta = [
    "rgb(243, 203, 211)",
    "rgb(234, 169, 189)",
    "rgb(221, 136, 172)",
    "rgb(202, 105, 157)",
    "rgb(177, 77, 142)",
    "rgb(145, 53, 125)",
    "rgb(108, 33, 103)",
]

Sunsetdark = [
    "rgb(252, 222, 156)",
    "rgb(250, 164, 118)",
    "rgb(240, 116, 110)",
    "rgb(227, 79, 111)",
    "rgb(220, 57, 119)",
    "rgb(185, 37, 122)",
    "rgb(124, 29, 111)",
]

Agsunset = [
    "rgb(75, 41, 145)",
    "rgb(135, 44, 162)",
    "rgb(192, 54, 157)",
    "rgb(234, 79, 136)",
    "rgb(250, 120, 118)",
    "rgb(246, 169, 122)",
    "rgb(237, 217, 163)",
]

Brwnyl = [
    "rgb(237, 229, 207)",
    "rgb(224, 194, 162)",
    "rgb(211, 156, 131)",
    "rgb(193, 118, 111)",
    "rgb(166, 84, 97)",
    "rgb(129, 55, 83)",
    "rgb(84, 31, 63)",
]

# Diverging schemes

Armyrose = [
    "rgb(121, 130, 52)",
    "rgb(163, 173, 98)",
    "rgb(208, 211, 162)",
    "rgb(253, 251, 228)",
    "rgb(240, 198, 195)",
    "rgb(223, 145, 163)",
    "rgb(212, 103, 128)",
]

Fall = [
    "rgb(61, 89, 65)",
    "rgb(119, 136, 104)",
    "rgb(181, 185, 145)",
    "rgb(246, 237, 189)",
    "rgb(237, 187, 138)",
    "rgb(222, 138, 90)",
    "rgb(202, 86, 44)",
]

Geyser = [
    "rgb(0, 128, 128)",
    "rgb(112, 164, 148)",
    "rgb(180, 200, 168)",
    "rgb(246, 237, 189)",
    "rgb(237, 187, 138)",
    "rgb(222, 138, 90)",
    "rgb(202, 86, 44)",
]

Temps = [
    "rgb(0, 147, 146)",
    "rgb(57, 177, 133)",
    "rgb(156, 203, 134)",
    "rgb(233, 226, 156)",
    "rgb(238, 180, 121)",
    "rgb(232, 132, 113)",
    "rgb(207, 89, 126)",
]

Tealrose = [
    "rgb(0, 147, 146)",
    "rgb(114, 170, 161)",
    "rgb(177, 199, 179)",
    "rgb(241, 234, 200)",
    "rgb(229, 185, 173)",
    "rgb(217, 137, 148)",
    "rgb(208, 88, 126)",
]

Tropic = [
    "rgb(0, 155, 158)",
    "rgb(66, 183, 185)",
    "rgb(167, 211, 212)",
    "rgb(241, 241, 241)",
    "rgb(228, 193, 217)",
    "rgb(214, 145, 193)",
    "rgb(199, 93, 171)",
]

Earth = [
    "rgb(161, 105, 40)",
    "rgb(189, 146, 90)",
    "rgb(214, 189, 141)",
    "rgb(237, 234, 194)",
    "rgb(181, 200, 184)",
    "rgb(121, 167, 172)",
    "rgb(40, 135, 161)",
]

# Qualitative palettes

Antique = [
    "rgb(133, 92, 117)",
    "rgb(217, 175, 107)",
    "rgb(175, 100, 88)",
    "rgb(115, 111, 76)",
    "rgb(82, 106, 131)",
    "rgb(98, 83, 119)",
    "rgb(104, 133, 92)",
    "rgb(156, 156, 94)",
    "rgb(160, 97, 119)",
    "rgb(140, 120, 93)",
    "rgb(124, 124, 124)",
]

Bold = [
    "rgb(127, 60, 141)",
    "rgb(17, 165, 121)",
    "rgb(57, 105, 172)",
    "rgb(242, 183, 1)",
    "rgb(231, 63, 116)",
    "rgb(128, 186, 90)",
    "rgb(230, 131, 16)",
    "rgb(0, 134, 149)",
    "rgb(207, 28, 144)",
    "rgb(249, 123, 114)",
    "rgb(165, 170, 153)",
]

Pastel = [
    "rgb(102, 197, 204)",
    "rgb(246, 207, 113)",
    "rgb(248, 156, 116)",
    "rgb(220, 176, 242)",
    "rgb(135, 197, 95)",
    "rgb(158, 185, 243)",
    "rgb(254, 136, 177)",
    "rgb(201, 219, 116)",
    "rgb(139, 224, 164)",
    "rgb(180, 151, 231)",
    "rgb(179, 179, 179)",
]

Prism = [
    "rgb(95, 70, 144)",
    "rgb(29, 105, 150)",
    "rgb(56, 166, 165)",
    "rgb(15, 133, 84)",
    "rgb(115, 175, 72)",
    "rgb(237, 173, 8)",
    "rgb(225, 124, 5)",
    "rgb(204, 80, 62)",
    "rgb(148, 52, 110)",
    "rgb(111, 64, 112)",
    "rgb(102, 102, 102)",
]

Safe = [
    "rgb(136, 204, 238)",
    "rgb(204, 102, 119)",
    "rgb(221, 204, 119)",
    "rgb(17, 119, 51)",
    "rgb(51, 34, 136)",
    "rgb(170, 68, 153)",
    "rgb(68, 170, 153)",
    "rgb(153, 153, 51)",
    "rgb(136, 34, 85)",
    "rgb(102, 17, 0)",
    "rgb(136, 136, 136)",
]

Vivid = [
    "rgb(229, 134, 6)",
    "rgb(93, 105, 177)",
    "rgb(82, 188, 163)",
    "rgb(153, 201, 69)",
    "rgb(204, 97, 176)",
    "rgb(36, 121, 108)",
    "rgb(218, 165, 27)",
    "rgb(47, 138, 196)",
    "rgb(118, 78, 159)",
    "rgb(237, 100, 90)",
    "rgb(165, 170, 153)",
]

# Prefix variable names with _ so that they will not be added to the swatches
_contents = dict(globals())
for _k, _cols in _contents.items():
    if (_k.startswith("_") or _k == "swatches" or _k.endswith("_r")):
        continue
    globals()[_k + '_r'] = _cols[::-1]

