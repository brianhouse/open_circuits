
def translate(q, lang):
    import urllib, urllib2, json
    # For language codes, see https://sites.google.com/site/opti365/translate_codes
    TRANSLATE_KEY = "XXXXXXXX"
    try:
        url = "https://translation.googleapis.com/language/translate/v2?key=" + TRANSLATE_KEY + "&q=" + urllib.quote_plus(q.encode('utf-8')) + "&target=" + lang
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        result = json.loads(response.read())
        return result['data']['translations'][0]['translatedText']
    except Exception as e:
        print(e)
        return None
