#!/usr/bin/env python

import goslate
import urllib

proxy_handler = urllib.request.ProxyHandler({"http" : "http://172.21.101.204:3129"})
proxy_opener = urllib.request.build_opener(urllib.request.HTTPHandler(proxy_handler),
                                    urllib.request.HTTPSHandler(proxy_handler))
gs_with_proxy = goslate.Goslate(opener=proxy_opener)
translation = gs_with_proxy.translate("hello world", "de")

#gs = goslate.Goslate()
#print(gs.translate('hello', 'ko'))

# German: Beschwerde
#print(gs.translate('Beschwerde', 'ko', source_language=u'de'))
# Polish: Skarga
#print(gs.translate('Skarga', 'ko', source_language=u'pl'))


#print (gs.get_languages())
#{'uz': 'Uzbek', 'ne': 'Nepali', 'fa': 'Persian', 'bg': 'Bulgarian', 'bn': 'Bengali', 'az': 'Azerbaijani', 'it': 'Italian', 'kn': 'Kannada', 'zh': 'Chinese', 'jw': 'Javanese', 'ceb': 'Cebuano', 'ht': 'Haitian Creole', 'hmn': 'Hmong', 'hu': 'Hungarian', 'no': 'Norwegian', 'ro': 'Romanian', 'tl': 'Filipino', 'lv': 'Latvian', 'gl': 'Galician', 'st': 'Sesotho', 'sw': 'Swahili', 'mn': 'Mongolian', 'el': 'Greek', 'sm': 'Samoan', 'tg': 'Tajik', 'en': 'English', 'km': 'Khmer', 'ig': 'Igbo', 'cy': 'Welsh', 'ja': 'Japanese', 'es': 'Spanish', 'mt': 'Maltese', 'lo': 'Lao', 'eu': 'Basque', 'zh-CN': 'Chinese (Simplified)', 'fr': 'French', 'iw': 'Hebrew', 'so': 'Somali', 'haw': 'Hawaiian', 'ko': 'Korean', 'fi': 'Finnish', 'sk': 'Slovak', 'ny': 'Chichewa', 'ku': 'Kurdish (Kurmanji)', 'nl': 'Dutch', 'ru': 'Russian', 'mi': 'Maori', 'gu': 'Gujarati', 'be': 'Belarusian', 'uk': 'Ukrainian', 'su': 'Sundanese', 'th': 'Thai', 'lb': 'Luxembourgish', 'fy': 'Frisian', 'ta': 'Tamil', 'ms': 'Malay', 'la': 'Latin', 'hy': 'Armenian', 'pa': 'Punjabi', 'ky': 'Kyrgyz', 'te': 'Telugu', 'tr': 'Turkish', 'xh': 'Xhosa', 'my': 'Myanmar (Burmese)', 'yi': 'Yiddish', 'sd': 'Sindhi', 'co': 'Corsican', 'de': 'German', 'mr': 'Marathi', 'sv': 'Swedish', 'ps': 'Pashto', 'mk': 'Macedonian', 'sr': 'Serbian', 'af': 'Afrikaans', 'hr': 'Croatian', 'pt': 'Portuguese', 'is': 'Icelandic', 'ga': 'Irish', 'ca': 'Catalan', 'ha': 'Hausa', 'ml': 'Malayalam', 'id': 'Indonesian', 'cs': 'Czech', 'zu': 'Zulu', 'sl': 'Slovenian', 'am': 'Amharic', 'da': 'Danish', 'vi': 'Vietnamese', 'eo': 'Esperanto', 'hi': 'Hindi', 'mg': 'Malagasy', 'kk': 'Kazakh', 'ur': 'Urdu', 'ar': 'Arabic', 'lt': 'Lithuanian', 'ka': 'Georgian', 'yo': 'Yoruba', 'sq': 'Albanian', 'zh-TW': 'Chinese (Traditional)', 'et': 'Estonian', 'sn': 'Shona', 'gd': 'Scots Gaelic', 'pl': 'Polish', 'bs': 'Bosnian', 'si': 'Sinhala'}

