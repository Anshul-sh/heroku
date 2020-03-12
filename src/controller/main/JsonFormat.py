import json
import pandas as pd
def PrCrisisResult():
    with open('Output/Output.json') as data_file:
        d = json.load(data_file)

    textStr = []
    tones = [0 for c in range(len(d['sentences_tone']))]
    docTone = d['document_tone']
    i = 0
    while  i < len(d['sentences_tone']):
        textStr.append(d['sentences_tone'][i]['text'])

        j = 0
        tones[i] = []

        while j< len(d['sentences_tone'][i]['tones']):
            tones[i].append(d['sentences_tone'][i]['tones'][j]['tone_name'])
            j = j + 1
        i = i + 1
    data = pd.DataFrame()
    data['Text'] = textStr
    data['Tones'] = tones
    str = data.to_html()
    return docTone,str


if __name__ == '__main__':
    PrCrisisResult()